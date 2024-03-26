from flask import *
from database_interact import *
from create_database import create_database
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from python_classes.user import User
from python_classes.wine import Wine
import hashlib
import re

app = Flask(__name__)


# create_database()
db = sqlite3.connect("database.db")

### INITIAL VARIABLES
logged = False
app.secret_key = 'lvivske_rizdviane'
### INITIAL VARIABLES

@app.route('/')
def index():
    return render_template('index.html', logged=logged)

@app.route('/map_of_wines')
def map_of_wines():
    try:
        with open('static/js/mapdata.js', 'r', encoding='utf-8') as file_:
            info = file_.readlines()
        res = ''
        unlocked = False
        regions = get_user_information(u_id)['unlocked_regions']
        for line in info:
            if line.startswith('      name:') and line.split(':')[-1].strip() in regions:
                unlocked = True
                res += line
            elif line.startswith('      color') and unlocked:
                res += '      color: "blue"\n'
                unlocked = False
            else:
                res += line
            
        js_code = res

        return render_template('map_of_wines.html', logged=logged, js_code = js_code)
    except:
        return render_template('login.html', logged=logged, user_exists=True, password = True)

@app.route('/map_of_wines/<country>', methods=['GET', 'POST'])
def info_about_country(country):
    try:
        global u_id
        with open('static/js/mapdata.js', 'r', encoding='utf-8') as file_:
            info = file_.readlines()
        res = ''
        unlocked = False
        regions = get_user_information(u_id)['unlocked_regions']
        for line in info:
            if line.startswith('      name:') and line.split(':')[-1].strip(' ""') in regions:
                unlocked = True
                res += line
            elif line.startswith('      color') and unlocked:
                res += '      color: "blue"\n'
                unlocked = False
            else:
                res += line
            
        js_code = res


        wines = get_wine_id(country)
        wines_info = list(map(get_wine_info, wines))
        info_shortage = ''
        wine_1_review = ''
        wine_2_review = ''
        if request.method =='POST':
            form_name = request.form.get('wine')
            if form_name == '1st wine':
                text = request.form['review1']
                rate = request.form['rating1']
                add_review(u_id, wines[0], text, int(rate))
                print(get_user_information(u_id)['unlocked_regions'])


            for review in get_reviews(u_id):
                if review['wine_id'] == wines[0]:
                    wine_1_review = review['review']

            if form_name == '2nd wine':
                text = request.form['review2']
                rate = request.form['rating2']
                add_review(u_id, wines[1], text, int(rate))
            
            for review in get_reviews(u_id):
                    if review['wine_id'] == wines[1]:
                        wine_2_review = review['review']
                
            return render_template('map_of_wines.html', info_shortage = info_shortage, logged=logged,
                                    wine_1 = wines_info[0], wine_2 = wines_info[1],
                                    review_1 = wine_1_review, review_2 = wine_2_review,
                                    js_code = js_code)

        for review in get_reviews(u_id):
            if review['wine_id'] == wines[0]:
                wine_1_review = review['review']

        for review in get_reviews(u_id):
            if review['wine_id'] == wines[1]:
                wine_2_review = review['review']

        return render_template('map_of_wines.html', logged=logged,
                                wine_1 = wines_info[0], wine_2 = wines_info[1],
                                review_1 = wine_1_review, review_2 = wine_2_review,
                                js_code = js_code)
    except KeyError:
        return render_template('fail.html', message='Please add both review and rating')
    except NameError:
        return render_template('fail.html', message='Please sign in first')


@app.route('/info_best_for')
def etiquette():
    return render_template('info_best_for.html', logged=logged)

@app.route('/info_best_for/glasses')
def glasses():
    return render_template('glass.html', logged=logged)

@app.route('/info_best_for/snacks')
def snacks():
    return render_template('snacks.html', logged=logged)

@app.route('/about')
def about():
    return render_template('about.html', logged=logged)

@app.route('/register', methods=['POST', 'GET'])
def register():
    global logged
    global u_id
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        password_conf = request.form['password confirmation']
        if user_password != password_conf:
            return render_template('register.html', logged=logged, pass_conf = False)
        if not re.match(r"^(?=.*[a-z].*[a-z])(?=.*[A-Z])(?=.*\d.*\d.*\d).*$", user_password):
            return render_template('register.html', logged=logged, pass_conf = True, re=True)
        new_user = User(user_email, user_password)
        if get_id(new_user):
            return render_template('register.html', logged=logged, pass_conf = True, user_exists = True)
        add_new_user(new_user)
        new_user.u_id = get_id(new_user)
        u_id = get_id(new_user)
        # session['current_user'] = jsonify(new_user)
        print(get_user_information(u_id)['username'])
        logged = True
        return redirect(f'/profile')
    return render_template('register.html', logged=logged, pass_conf = True)


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    global logged
    global u_id
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        new_user = User(user_email, user_password)
        if not get_id(new_user):
            return render_template('login.html', logged=logged, user_exists = False, password=True)
            ## do an html for this
        u_id = get_id(new_user)
        pass_bytes = user_password.encode('utf-8')
        password_hash = hashlib.sha256(pass_bytes).hexdigest()
        if get_user_information(u_id)['password'] != password_hash:
            return  render_template('login.html', logged=logged, user_exists = True, password=False)
        new_user.my_map.unlocked_regions = {region:get_wine_id(region) for region in get_user_information(u_id)['unlocked_regions']}
        new_user.my_reviews = {Wine(wine['wine_id']):wine['review'] for wine in get_reviews(u_id)}
        new_user.wine_rating = {Wine(wine['wine_id']):wine['rating'] for wine in get_reviews(u_id)}
        # session['current_user'] = jsonify(new_user)
        logged = True
        print(get_user_information(u_id))
        return redirect('/profile') #do the user id here? but how?
    return render_template('login.html', logged=logged, user_exists=True, password = True)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # try:
        # u = session.get('current_user')
    # except:
    #     return render_template('error_page.html', message='Youare not logged in yet')
    
    # reviews = [{'name':wine.name, 'review':u.my_reviews[wine], 'rating':u.wine_rating[wine]} for wine in u.my_reviews]
    try:
        global u_id
        global logged
        if request.method == 'POST':
            form_name = request.form.get('prof_button')
            if form_name == 'Settings':
                return redirect('/profile/settings')
            u_id = None
            logged = None
            return redirect('/')
        print(get_user_information(u_id))
        username = get_user_information(u_id)['username']
        print(username)
        reviews = get_reviews(u_id)[:3]
        return render_template('my_profile.html', username=username, logged=logged, reviews=reviews)
    except:
        return render_template('fail.html', message='Please sign in first')


@app.route('/profile/settings', methods=['GET', 'POST'])
def settings():
### we got rid of user photo
    # u = session.get['current user']
    try:
        if request.method == 'POST':
            username = request.form.get("new_username")
            change_username(u_id, username)
        
        username = get_user_information(u_id)['username']
        return render_template('settings.html', logged=logged, username=username)
    except:
        return render_template('fail.html', message='Please sign in first')

@app.route('/settings/delete account')
def deleting():
    try:
        global logged
        info = statistics(u_id)
        del_user(u_id)
        logged=False
        return render_template('deleteacc.html', info=info)
    except:
        return render_template('fail.html', message='Please sign in first')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('fail.html')
@app.route('/dont_change_rewiev')
def dont_change_rewiev():
    return render_template('dont_change_rewiev.html')
if __name__ == '__main__':
    app.run(debug=True)

import sqlite3
from datetime import datetime
from python_classes.user import User

def add_new_user(user:User):
    """
    Adds a new user into the database
    isinstance(user, User)
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (user.username, user._User__email, user._User__password))
        
def del_user(user_id:int):
    """
    Deletes the user from the database
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM users WHERE user_id = ?",
                  (user_id,))
        c.execute("DELETE FROM friends WHERE user_id = ? or friend_id = ?",
                  (user_id, user_id))
        c.execute("DELETE FROM reviews WHERE user_id = ?",
                  (user_id,))
        c.execute("DELETE FROM tasted_wines WHERE user_id = ?",
                  (user_id,))
        c.execute("DELETE FROM wishlist WHERE user_id = ?",
                  (user_id,))
        c.execute("DELETE FROM unlocked_regions WHERE user_id = ?",
                  (user_id,))

def get_id(user) -> int:
    """
    Returns the user's id if he is registered in the database
    if not the function returns None
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT user_id FROM users WHERE email = ?",
                  (user._User__email,))
        try:
            return c.fetchone()[0]
        except TypeError:
            return None

def change_username(user_id:int, new_name:str):
    """
    Changes the username
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("UPDATE users SET username = ? WHERE user_id = ?",
                  (new_name, user_id))

def get_user_information(user_id:int) -> dict:
    """
    Gets user information
        returns:
        {'username': usernname, 'password': 'SJ11bbq$9h', 'email': username@gmail.com, 'unlocked_regions': ['Italy', 'Germany']}
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT username, password, email FROM users WHERE user_id = ?",
                  (user_id,))
        inf1 = c.fetchone()
        c.execute("SELECT country FROM unlocked_regions WHERE user_id = ?",
                  (user_id,))
        inf2 = c.fetchall()
        inf2 = [item[0] for item in inf2]
        res_dic = {'username': inf1[0], 'password': inf1[1], 'email': inf1[2], 'unlocked_regions': inf2}
        return res_dic

def statistics(user_id:int) -> str:
    """
    Return the string of information about user

    RETURN EXAMPLE:
        Thank you for being a part of our community.
        Your presence has truly made a difference, and we appreciate the time you've spent with us.
        Here are your stats:
        You've rated 2 wines
        You've unlocked the following countries: Italy, Germany
        Favourite wine color: white
        Favourite wine attribute: semisweet
    OR:
        Thank you for being a part of our community.
        Your presence has truly made a difference, and we appreciate the time you've spent with us.
        Here are your stats:
        You've rated 0 wines
        Explore more wines to get more personal data
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT wine_id FROM tasted_wines WHERE user_id = ?",
                  (user_id,))
        wine_ids = c.fetchall()
        c.execute("SELECT country FROM unlocked_regions WHERE user_id = ?",
                  (user_id,))
        unlocked_countries = c.fetchall()
        unlocked_countries = [item[0] for item in unlocked_countries]
        c.execute("SELECT wine_id FROM reviews WHERE user_id = ?",
                  (user_id,))
        num_of_reviews = len(c.fetchall())

    color_dic = {'red': 0, 'white': 0, 'yellow': 0, 'dark ruby': 0, 'pink': 0}
    attribute_dic = {'sweet': 0, 'dry': 0, 'medium-dry': 0}
    for wine_id in wine_ids:
        wine_inf = get_wine_info(wine_id[0])

        color = wine_inf['color']
        color_dic[color] += 1

        attribute = wine_inf['attribute']
        attribute_dic[attribute] += 1

    max_color_value = max(color_dic.values())
    max_colors = [key for key, value in color_dic.items() if value == max_color_value]
    max_attribute_value = max(attribute_dic.values())
    max_attributes = [key for key, value in attribute_dic.items() if value == max_attribute_value]

    unlocked_countries_str = ''
    num_of_reviews_str = f"You've rated {num_of_reviews} wine{'' if num_of_reviews == 1 else 's'}"
    start_str = "Thank you for being a part of our community.\nYour presence has truly made a difference, and we appreciate the time you've spent with us.\nHere are your stats:"
    if len(unlocked_countries) >= 1:
        unlocked_countries_str = f"You've unlocked the following countr{'ies' if len(unlocked_countries) > 1 else 'y'}: {', '.join(unlocked_countries)}"
    if unlocked_countries_str == '':
        addittional_str = "Explore more wines to get more personal data"
        final_str = f'{start_str}\n{num_of_reviews_str}\n{addittional_str}'
    else:
        fav_color_str = f"Favourite wine color{'s' if len(max_colors) > 1 else ''}: {', '.join(max_colors)}"
        fav_attribute_str = f"Favourite wine attribute{'s' if len(max_attributes) > 1 else ''}: {', '.join(max_attributes)}"
        final_str = f'{start_str}\n{num_of_reviews_str}\n{unlocked_countries_str}\n{fav_color_str}\n{fav_attribute_str}'

    return final_str

def get_wine_id(country:str) -> list:
    """
    Input: a country
    Output: a list of wine ids originated from the country

    RETURN EXAMPLE:
        [2, 5, 13]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT wine_id FROM wines WHERE country = ?",
                  (country,))
        inf = c.fetchall()
        inf_wt = [item[0] for item in inf]
        return inf_wt

def get_wine_info(wine_id:str) -> dict:
    """
    Gets all info about a wine

    RETURN EXAMPLE:
        {'name': 'Solicello Merlot', 'taste': 'fruity', 'attribute': 'dry', 'color': 'red', 'country': 'Italy'}
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT name, taste, attribute, color, country FROM wines WHERE wine_id = ?",
                  (wine_id,))
        inf = c.fetchone()
        inf_dict = {'name': inf[0], 'taste': inf[1], 'attribute': inf[2], 'color': inf[3], 'country': inf[4]}
        return inf_dict
    
def add_tasted_wine(user_id:int, wine_id:int):
    """
    Adds a new user's tasted wine to the database
    [inside help function]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO tasted_wines (user_id, wine_id) VALUES (?, ?)",
                  (user_id, wine_id))
        wine_country = get_wine_info(wine_id)['country']
        c.execute("SELECT country FROM unlocked_regions WHERE user_id = ?",
                  (user_id,))
        user_countries = c.fetchall()
        user_countries = [item[0] for item in user_countries]
        if not wine_country in user_countries:
            c.execute("INSERT INTO unlocked_regions (user_id, country) VALUES (?, ?)",
                      (user_id, wine_country))

def remove_tasted_wine(user_id:int, wine_id:int):
    """
    Removes user's tasted wine from the database
    [inside help function]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM tasted_wines WHERE user_id = ? and wine_id = ?",
                  (user_id, wine_id))
        wine_country = get_wine_info(wine_id)['country']
        c.execute("SELECT wine_id FROM wines WHERE country = ? and wine_id != ?",
                  (wine_country, wine_id))
        wine_ids = c.fetchall()
        wine_ids = [wine[0] for wine in wine_ids]
        c.execute("SELECT wine_id FROM tasted_wines WHERE user_id = ?",
                  (user_id,))
        tasted_wines = c.fetchall()
        tasted_wines = [wine[0] for wine in tasted_wines]
        wine_from_same_country_tasted = False
        for wine in wine_ids:
            if wine in tasted_wines:
                wine_from_same_country_tasted = True
                break
        if not wine_from_same_country_tasted:
            c.execute("DELETE FROM unlocked_regions WHERE user_id = ? and country = ?",
                        (user_id, wine_country))

def get_reviews(user_id:int) -> list[dict]:
    """
    Returns reviews of the user from latest to oldest

    RETURN EXAMPLE:
        [{'wine_id': 1, 'name': 'Livin da vida loca', 'review': 'It was ok', 'rating': 3, 'time': '2024-03-13'}, 
        {'wine_id': 2, 'name': 'Deutsch wine', 'review': 'LOVE IT', 'rating': 5, 'time': '2024-03-13'}, 
        {'wine_id': 4, 'name': 'Best wine 2020', 'review': 'Amazing wine', 'rating': 5, 'time': '2024-03-13'}]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("SELECT wine_id, review, rating, time FROM reviews WHERE user_id = ?",
                  (user_id,))
        inf = c.fetchall()[-1::-1]
        res_lst = []
        for review in inf:
            c.execute("SELECT name FROM wines WHERE wine_id = ?",
                      (review[0],))
            wine_name = c.fetchone()[0]
            temp_dict = {'wine_id': review[0], 'name': wine_name, 'review': review[1], 'rating': review[2], 'time': review[3]}
            res_lst.append(temp_dict)
        return res_lst

def add_review(user_id:int, wine_id:int, text:str, rating:int):
    """
    Adds a review to the database

    text - text of the review
    rating - the rating of the wine on a scale from 1 to 5 (with 0.5 interval)
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    time_to_insert = datetime.now().date()
    with conn:
        c.execute("SELECT user_id FROM reviews WHERE user_id = ? and wine_id = ?",
                  (user_id, wine_id))
        wine_review = c.fetchone()
        if wine_review is None:
            c.execute("INSERT INTO reviews (user_id, wine_id, review, rating, time) VALUES (?, ?, ?, ?, ?)",
                      (user_id, wine_id, text, rating, time_to_insert))
        else:
            c.execute("DELETE from reviews WHERE user_id = ? and wine_id = ?",
                      (user_id, wine_id))
            c.execute("INSERT INTO reviews (user_id, wine_id, review, rating, time) VALUES (?, ?, ?, ?, ?)",
                      (user_id, wine_id, text, rating, time_to_insert))
            return
    add_tasted_wine(user_id, wine_id)

def del_review(user_id:int, wine_id:int):
    """
    Deletes the review of the wine from the user from database
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM reviews WHERE user_id = ? and wine_id = ?",
                  (user_id, wine_id))
    remove_tasted_wine(user_id, wine_id)

def add_friend(user1_id:int, user2_id:int):
    """
    Adds new friends
    [not used]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)",
                  (user1_id, user2_id))
        c.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)",
            (user2_id, user1_id))

def remove_friend(user1_id:int, user2_id:int):
    """
    Deletes friends
    [not used]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM friends (user_id, friend_id) VALUES (?, ?)",
                  (user1_id, user2_id))
        c.execute("DELETE FROM friends (user_id, friend_id) VALUES (?, ?)",
                  (user2_id, user1_id))

def add_wine_to_wishlist(user_id:int, wine_id:int):
    """
    Adds a wine to the user's wishlist
    [not used]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO wishlist (user_id, wine_id) VALUES (?, ?)",
                  (user_id, wine_id))
  
def del_wine_from_wishlist(user_id:int, wine_id:int):
    """
    Removes the wine from the user's wishlist
    [not used]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM wishlist WHERE user_id = ? and wine_id = ?",
                  (user_id, wine_id))
        
def get_glasses_info():
    """
    access the base with glasses
    
    RETURN EXAMPLE:
    [{"img":"v52_542 custom-button", "name":"Bordeaux Glass", "link":"https://dimposudu.ua/...", "description":"Бокал має велику глибоку чашу..."}]
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    glasses_info = []
    with conn:
        c.execute("SELECT photo, name, link, description FROM glass")
        for row in c.fetchall():
            inf_dict = {'img': row[0], 'name': row[1], 'link': row[2], 'description': row[3]}
            glasses_info.append(inf_dict)
        return glasses_info

# user1 = User('d.tsymbl.pn@ucu.edu.ua', '2198721987')
# add_new_user(user1)
# add_review(1, 6, 'Splendid wine', 5)
# add_review(1, 18, "Worst wine ive tried", 1)
# add_review(1, 17, "Worst wine ive tried", 1)
# add_review(1, 11, "It's ok", 3)
# add_review(1, 9, "Love it", 4)
# del_review(1, 18)
# print(get_reviews(1))
# print(get_glasses_info())
# conn = sqlite3.connect("database.db")
# c = conn.cursor()
# c.execute("SELECT * FROM users")
# print(c.fetchall())
# print(get_id(user1))
# change_username(1, 'oleh')
# c.execute("SELECT * FROM users")
# print(c.fetchall())
# del_user(1)
# add_tasted_wine(2, 1)
# add_tasted_wine(2, 2)
# remove_tasted_wine(2, 1)
# c.execute("SELECT * FROM users")
# print(c.fetchall())
# print(get_user_information(2))
# print(get_wine_info(2))
# # print(statistics(2))
# # print(statistics(1))
# print(get_wine_id('Italy'))
# add_review(2, 2, 'Amazing wine', 5)
# add_review(2, 1, 'Amazing wine LOVE IT', 5)
# add_review(2, 2, 'LOVE IT', 4)
# del_review(2, 1)
# print(get_latest_reviews(2))
# add_review(2, 1, 'pss', 3)
# print(get_latest_reviews(2))

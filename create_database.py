import sqlite3

def create_database():
    """
    Creates a database for further usage
    note: needs to be run only one time
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE users (
              user_id integer PRIMARY KEY,
              username text,
              email text,
              password text
            )""")

    c.execute("""CREATE TABLE reviews (
              user_id integer,
              wine_id integer,
              review text,
              rating integer,
              time date,

              foreign key (user_id) references users(user_id),
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute(
        """CREATE TABLE friends (
              user_id integer,
              friend_id integer,
              
              foreign key (user_id) references users(user_id)
              foreign key (friend_id) references users(user_id)
            )""")

    c.execute("""CREATE TABLE tasted_wines (
              user_id integer,
              wine_id integer,

              foreign key (user_id) references users(user_id)
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute("""CREATE TABLE wines (
              wine_id integer PRIMARY KEY,
              name text,
              taste text,
              attribute text,
              color text,
              country text
            )""")
    
    c.execute("""CREATE TABLE glass (
              photo text,
              name text,
              link text,
              description text
            )""")
    
    c.execute("""CREATE TABLE unlocked_regions (
              user_id integer,
              country text,

              foreign key (user_id) references users(user_id)
            )""")

    c.execute("""CREATE TABLE wishlist (
              user_id integer,
              wine_id integer,

              foreign key (user_id) references users(user_id)
              foreign key (wine_id) references wines(wine_id)
            )""")

    c.execute("""CREATE TABLE snack (
              wine_id integer,
              snack text,

              foreign key (wine_id) references wines(wine_id)
            )""")

    # c.execute("CREATE INDEX idx_user_id_reviews ON reviews(user_id)")
    # c.execute("CREATE INDEX idx_wine_id_reviews ON reviews(wine_id)")
    # c.execute("CREATE INDEX idx_user_id_friends ON friends(user_id)")
    # c.execute("CREATE INDEX idx_user_id_tasted_wines ON tasted_wines(user_id)")
    # c.execute("CREATE INDEX idx_user_id_wishlist ON wishlist(user_id)")

    with open("wine.csv", 'r', encoding='utf-8') as file:
        # imports wines
        for wine in file:
            wine = wine.split(',')
            if wine[0] == "country":
                continue
            c.execute("INSERT INTO wines (name, taste, attribute, color, country) VALUES (?, ?, ?, ?, ?)",
                      (wine[1], wine[5], wine[4], wine[3], wine[0]))
            
    with open("glass.csv", "r", encoding='utf-8') as file:
        # imports glasses
        for glass in file:
            glass = glass.split(',')
            if glass[0] == 'photo':
                continue
            glass[3] = f"{','.join(glass[3:])}"
            c.execute("INSERT INTO glass (photo, name, link, description) VALUES (?, ?, ?, ?)",
                      (glass[0], glass[1], glass[2], glass[3]))

    conn.commit()
    conn.close()

# !!!!!!!!! run this:
    
# create_database()

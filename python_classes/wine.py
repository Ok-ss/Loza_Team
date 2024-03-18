import sqlite3
import json

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

class Wine:
    # __rating = {}

    def __init__(self, wine_id:int) -> None:
        self.w_id = wine_id
        self.name = get_wine_info(wine_id)['name']
        # self.region = data.Wine_data[name]['region']
        self.country = get_wine_info(wine_id)['country']
        self.taste = get_wine_info(wine_id)['taste']
        self.color = get_wine_info(wine_id)['color']
        self.attribute = get_wine_info(wine_id)['attribute']
        # self.recomendations:dict[User:str] = {}
        # self.reviews:dict[User:str] = {}
        # self.user_ratings:dict[User:float] = {}
        # Wine.__rating[self] = 0

    def __json__(self):
        return self.w_id

    # def rated_by_user(self, user):
    #     return self.user_ratings[user]

    # def find_out_which_glass(self):
    #     for el, lst in data.Glass_data.items():
    #         if self.name in lst:
    #             return el

    # def find_out_which_snack(self):
    #     for wine, snacks in data.Snacks_data.items():
    #         if self.name == wine:
    #             return snacks

    # def is_highly_rated(self):
    #     return sum(self.user_ratings.values())/len(self.user_ratings.values()) >= 4.1

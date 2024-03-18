from python_classes.wine import Wine
from python_classes.map import Map
import json
# from python_classes.database import Database

# class Achievment:
#     def __init__(self, name:str, call, bar:int, lower=False) -> None:
#         self.name = name
#         self.call = call #atribute needed ex: friends, reviewed_wines...
#         self.bar = bar
#         self.lower = lower

#     def satisfied(self, user):
#         if self.lower:
#             if (len(user.self.call) < self.bar and self.lower)\
#                   or (len(user.self.call) > self.bar and not self.lower):
#                 return True
#         return False


class User:
    # rating_of_users = []
    # all_achievments:list[Achievment] = [] #add achievments here
    
    def __init__(self, email:str, password:str) -> None:
        self.u_id = 0
        self.__email = email
        self.__password = password
        self.username = email.split('@')[0]
        # self.reviewed_wines:list[Wine] = [] #do we need that if we have my_reviews
        self.my_reviews:dict[Wine:str] = {}
        self.wine_rating:dict[Wine:int] = {}
        # self._userphoto = None
        # self._username:str = 'username'#f'user#{Database.userlist.index(self)+1}'
        # #might rename because 'friends' is a mutual thing
        # self._friends:list[User] = []
        self.my_map = Map()
        # self.wishlist = []
    
    def __repr__(self) -> str:
        return f'{self.u_id}'
    
    def __json__(self):
        return {"u_id":self.u_id,
                '__email':self.__email,
                '__password':self.__password,
                'username':self.username,
                'my_reviews':{wine.__json__():review for wine, review in self.my_reviews.items()},
                'wine_rating':{wine.__json__():rate for wine, rate in self.wine_rating.items()},
                'my_map':self.my_map.__json__()}

# user = User('aomeone@gmail.com', '43nfore943#')
# print(user.__json__())

# #### starting useless
#     @property
#     def username(self):
#         return self._username

#     @username.setter
#     def username(self, new_name):
#         self._username = new_name


#     @property
#     def userphoto(self):
#         return self._userphoto

#     @userphoto.setter
#     def userphoto(self, photo):
#         self._userphoto = photo #how do we work with files here?

#     @property
#     def friends(self):
#         return self._friends

#     @friends.setter
#     def friends(self, new_list):
#         self._friends = new_list

# ##### finishing useless

#     @property
#     def podium(self):
#         #maybe make a whole class for achievments
#         my_achievments = []
#         for ach in self.all_achievments:
#             if ach.satisfied(self):
#                 my_achievments.append(ach)
#         return my_achievments


#     def user_bye(self):
#         # Database.delete_user(self)
#         return self.all_statistic()     ###is that it?


#     def add_friend(self, smb:'User'):
#         if smb not in self.friends:
#             self.friends.append(smb)

#     def delete_friend(self, smb:'User'):
#         if smb in self.friends:
#             self.friends.remove(smb)

#     def recommend_wine(self, wine, text='I recommend this wine'):
# ### shouldnt here be a condition to be able to recommend?
#         wine.recomendations[self] = text

#     def all_statistic(self):
#         res = ''
#         res += f'You have reviewed {len(self.reviewed_wines)} wines \n'
#         res += f'You have opened {len(self.my_map.unlocked_regions)} regions'
#         res += f'You have unlocked such achievments: {self.podium}'
#         #write more here
#         return res

#     def rate(self, wine:'Wine', rate):
#         wine.user_ratings[self] = rate
#         Wine.__rating[wine] = sum(wine.user_ratings.values())/len(wine.user_ratings)

#     def add_to_reviews(self, wine:'Wine', review):
#         wine.reviews[self] = review
#         self.my_reviws[wine] = review
#         self.reviewed_wines.append(wine)

# # make rate & add_to_reviews one function?

#     def add_to_wishlist(self, wine):
#         self.wishlist.append(wine)

#     def remove_from_reviews(self, wine):
#         if wine in self.reviewed_wines:
#             wine.reviews[self] = None
#             self.my_reviws[wine] = None
#             self.reviewed_wines.remove(wine)

#     def remove_from_wishlist(self, wine):
#         if wine in self.wishlist:
#             self.wishlist.remove(wine)

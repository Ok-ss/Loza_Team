from user import User
from wine import Wine

class Database:
    def __init__(self, url, pswd, user) -> None:
        self.__url = url
        self.__password = pswd
        self.__user = user

    userlist = [] #how else am I going to access that?
    winelist = []

    @classmethod
    def delete_user(cls, user:'User'):
        cls.userlist.remove(user)

    @classmethod
    def create_user(cls, user:'User'):
        cls.userlist.append(user)

    @classmethod
    def new_wine(cls, wine:'Wine'):
        cls.winelist.append(wine)

    def save_new_inform(self):
        pass
####


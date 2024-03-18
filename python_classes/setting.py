"""
The Setting class, which provides the ability to change the application interface
"""
from python_classes.user import User
from python_classes.map import Map
from python_classes.database import Database

class Setting:
    """Setting class"""
    def __init__(self, notecolor='Yellow', icons='glasses'):
        self.notecolor = notecolor
        self.icons = icons
        self.avalible_colors = []

    def change_colour_note(self, new_color):
        """User clicks on a colour and the note changes colour"""
        if new_color in self.avalible_colors:
            self.notecolor = new_color

    def change_icons_of_rate(self, stars):
        """User clicks anf rating icons become stars insted of glasses"""
        self.icons = stars

    def change_background_map(self, new_colour):
        """Add/change the background for the wine map"""
        Map.background_colour = new_colour
        pass

    def change_theme(self, param):
        """Поки не шарю шо воно має робити"""
        pass

    def reset_settings(self):
        """User clicks on a "restore" button and all settings restore to their original state"""
        self.notecolor = 'Yellow'
        self.icons = 'glasses'

    def delete_account(self):
        """
        1) We're asking if cliens is sure
        2) Generating him/her a general description of his/her
            achievements while using the application
        3) Deleting info about his/her account
        """
        print('Are you sure you want to delete your account?\
All your progress will be deleted.')
        button = ["No", "Yes"]
        # висвітлюється кнопка
        if button == 'Yes':
            print(f'While using the app, you have discovered the following regions {Map.user}, tasted {User.wish_list} wines, and viewed your list for the last time()\
Thank you for choosing us')
        print("*opportunity to take a survey about why you are deleting your account")
        Database.delete_user(self)

    def __str__(self):
        return f"Сurrently you have following setting:{self.notecolor, self.icons}"

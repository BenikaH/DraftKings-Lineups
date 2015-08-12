from PyQt4 import QtGui
from ui.following_ui import Ui_Dialog
import os

"""
Module to add/remove players to follow.

Notes -
- remove cmd-A key binding, used for select all in many applications and don't think
this menu will be used often enough to need a shortcut.

"""


class FollowingWin(QtGui.QDialog):

    # define path here as well so can use with static method.
    name_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'usernames.txt')

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_add.setShortcut('Return')

        self.add_signals()
        self.add_names(FollowingWin.load_players())

    def add_names(self, names):
        """
        Adds a list of names to the list widget
        """
        self.ui.list_names.addItems(names)

    def add_names_to_file(self, name):
        """Adds names entered to usernames.txt"""
        with open(self.name_file, 'a') as f:
            f.write(name + '\n')

    def add_signals(self):
        """Adds the widget signals"""
        self.ui.btn_add.pressed.connect(self.get_entry_name)
        self.ui.btn_del.pressed.connect(self.del_names)

    def del_names(self):
        """Deletes names from list widget"""
        del_item = self.ui.list_names.currentRow()
        del_name = self.ui.list_names.takeItem(del_item)

        if del_name:
            return self.del_names_from_file(del_name.text())

    def del_names_from_file(self, name):
        """Removes players from usernames.txt"""
        current_names = self.load_players()
        current_names.remove(name)

        with open(self.name_file, 'w') as f:
            for name in current_names:
                f.write(name + '\n')

    def get_entry_name(self):
        """Gets the name from the line edit when add button is pressed"""
        name = self.ui.le_names.text()

        self.ui.le_names.setText('')

        # Return in list format to be compatible with self.add_names
        if name and name not in self.load_players():
            self.add_names_to_file(name)
            return self.add_names([name])

    @staticmethod
    def load_players():
        """Loads players from file, will often be used by other modules."""
        fname = FollowingWin.name_file
        if not os.path.isfile(fname):
            with open(fname, 'w') as f:
                f.write('')

        usernames = []
        with open(fname, 'r') as f:
            for line in f.readlines():
                usernames.append(line.strip('\n'))

        return usernames
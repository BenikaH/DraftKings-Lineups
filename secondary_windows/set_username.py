from ui.username_ui import Ui_Dialog
from PyQt4 import QtGui
import os

class NameWin(QtGui.QDialog):
    name_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'myname.txt')

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #self.filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'myname.txt')

        # Set current name as name set in file.
        try:
            self.cur_name = self.get_cur_name()
        except:
            self.write_cur_name('')
            self.cur_name = ''

        self.update_name()

    def accept(self):
        new_name = self.ui.le_name.text()
        if new_name:
            self.write_cur_name(new_name)
            QtGui.QDialog.accept(self)

    def reject(self):
        QtGui.QDialog.reject(self)

    @staticmethod
    def get_cur_name():
        """Gets the current username listed"""
        with open(NameWin.name_file, 'r') as f:
            name = f.read()
            return name

    def update_name(self):
        """Updates the current name label."""
        self.ui.var_name.setText(self.cur_name)

    def write_cur_name(self, new_name):
        """Writes new name as player name"""
        with open (self.name_file, 'w') as f:
            f.write(new_name)

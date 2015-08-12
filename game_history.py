import sys
from PyQt4 import QtGui
from general.file_container import InFiles
from main_window.main_window import Main
from secondary_windows.game_info_view import TourneyInfoWindow
from secondary_windows.game_info_controller import game_info


class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main = Main()
        self.main.show()

        self.check_in_files()

    def check_in_files(self):
        """
        Checks the in_files directory to see if there are any files to be
        uploaded.  If files are present, the tourney info window is shown.
        """
        if len(InFiles().list_files()) > 0:
            new_tourneys = TourneyInfoWindow(game_info, self.main)
            new_tourneys.exec_()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
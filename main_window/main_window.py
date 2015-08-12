import sys
from PyQt4 import QtGui, QtCore
from ui.main_raw import Ui_MainWindow
from secondary_windows import following
import ownership_barchart, graph_frame, my_players
from general.game import Game
from general.db import DB
from secondary_windows import game_info_view
from secondary_windows.set_username import NameWin
import timeit



"""
Controller of the main window.

Notes -
- Remove park factor button
- remove single entries/num entries
"""


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = DB()

        self.plot_frame = graph_frame.PercentBar(self.ui.tab_1)

        self.my_name = self.load_myname()

        # Holds the tourney indexes listed in the combobox.
        self.cb_indexes = []

        self.load_combobox()
        self.add_signals()

        self.change_tourney(0)


    def add_signals(self):
        """Adds signals to buttons and menu items."""
        self.ui.actionAdd_To_Following.triggered.connect(self.open_following)
        self.ui.actionEdit_Tourney_Info.triggered.connect(self.open_tourney_info)
        self.ui.cb_ids.currentIndexChanged.connect(self.change_tourney)
        self.ui.actionSet_My_Name.triggered.connect(self.open_myname)

    def change_tourney(self, idx=None):
        """
        Calls the delete method of the frame class and reloads new tournament when
        changing selection in the combobox.
        :return:
        """
        if idx == None:
            idx = self.ui.cb_ids.currentIndex()
        id_ = self.cb_indexes[idx]
        self.plot_frame.del_layout()
        self.load_summary(id_)
        self.make_game(idx)
        self.make_barcharts()
        self.load_playertable()

    def load_myname(self):
        """Loads my username"""
        try:
            name = NameWin.get_cur_name()
            assert name
            return name
        except:
            # If there is no username file or file is blank, open dialog to create it, then reload.
            self.open_myname()
            self.load_myname()

    def load_combobox(self):
        """
        Querys the database for the tournament info and returns a list of tournament
        name strings to be listed in the combobox.

        Also adds the tournament IDs to a list in the order that the tourneys are shown
        in the combobox.  Because the names can be the same, the indexes of the combobox
        will be used instead of the string so can access the tourney IDs with the index
        and this list.

        Finally adds names to the combobox.
        """
        vals = self.model.query("""SELECT buyin, game_type, game_date, id FROM games
        ORDER BY game_date DESC""")

        tourney_names = []
        for (buyin, type_, date, id_) in vals:
            self.cb_indexes.append(id_)
            tourney_names.append("{} {} {}".format(buyin, type_, date))

        self.ui.cb_ids.addItems(tourney_names)

    def load_summary(self, id_):
        info = self.model.query("""SELECT * FROM games WHERE id = %s""", (id_, ))[0]
        vars = [self.ui.var_date, self.ui.var_buyin, self.ui.var_type, self.ui.var_entries]
        for x in range(len(info)-1):
            vars[x].setText(str(info[x+1]))

    def load_playertable(self):
        """
        Loads the player table that will show the players that I have selected for a
        given tournament.

        This will be inserted into the frame under the ownership graphs.
        :return:
        """
        pt = my_players.PlayerTable(self.ui.widget_table, self.game)

    def make_barcharts(self):
        """
        Creates the scrollable bar charts appearing in tab 1.
        :return:
        """
        for position, player_dict in self.game.get_all_ownership().items():
            bar = ownership_barchart.BarChart(self.plot_frame, position, player_dict)
            self.plot_frame.add_top_chart(bar)

        for position, player_dict in self.game.get_following_ownership().items():
            bar = ownership_barchart.BarChart(self.plot_frame, position, player_dict)
            self.plot_frame.add_bot_chart(bar)

    def make_game(self, idx):
        """
        Makes the Game object to access the stats.
        Called when starting application or changing the touranement in the combobox.
        """
        self.game = Game(self.model, self.cb_indexes[idx])

    def open_following(self):
        """Add players to follow menu"""
        gw = following.FollowingWin(self)
        gw.exec_()

    def open_myname(self):
        nw = NameWin(self)
        nw.exec_()

    def open_tourney_info(self):
        """
        Opens window to add tournament info of new tourneys.
        :return:
        """
        tourney_info_window = game_info_view.TourneyInfoWindow(self)
        tourney_info_window.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
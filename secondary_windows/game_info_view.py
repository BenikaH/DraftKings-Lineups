from PyQt4 import QtGui, QtCore
from ui.tourney_info_ui import Ui_Dialog
from general import file_container

"""
Notes -

"""

"""
About -
This window will take a new tournament summary and add the info to the contest_summary.csv file
and move the tournament file to the out folder to be used by the main program.
"""


class TourneyInfoWindow(QtGui.QDialog):
    def __init__(self, controller, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.controller = controller
        self.in_files = file_container.InFiles()
        self.tournaments = {}

        self.update_tourneys()
        self.update_cb_values()
        self.add_signals()
        self.set_current_date()

    def add_signals(self):
        """
        Adds signals to widgets to call methods on interaction.
        :return:
        """
        self.ui.cb_tourneyid.currentIndexChanged.connect(self.clear_fields)
        self.ui.btn_submit.pressed.connect(self.make_tournament)
        self.ui.btn_close.pressed.connect(self.closewin)
        self.ui.btn_refresh.pressed.connect(self.new_tourneys)

    def clear_fields(self):
        """Resets the values of the fields"""
        self.ui.le_name.setText('')
        self.ui.cb_buyin.setCurrentIndex(0)
        self.ui.cb_type.setCurrentIndex(0)
        self.set_current_date()

    def closewin(self):
        """Closes the dialog window"""
        self.close()

    def get_vals(self):
        """Returns all the field values"""
        keys = ['id', 'buyin', 'game_date', 'game_type']

        values = [
            self.ui.cb_tourneyid.currentText(),
            self.ui.cb_buyin.currentText(),
            self.ui.cb_date.date().toPyDate(),
            self.ui.cb_type.currentText()
        ]

        return {k: str(v) for k, v in zip(keys, values)}

    def make_tournament(self):
        """Makes the new csv file and removes old from list and dir"""

        values = self.get_vals()
        self.controller(values)
        self.in_files.del_file(values['id'])
        self.update_tourneys()
        self.update_cb_values()

    def new_tourneys(self):
        self.update_tourneys()
        self.update_cb_values()

    def set_current_date(self):
        """
        Sets the cb_date to the current date - 1 (yesterday).
        :return:
        """
        current = QtCore.QDate.currentDate()
        current = current.addDays(-1)
        self.ui.cb_date.setDate(current)

    def update_cb_values(self):
        """
        Adds the tourney values to the cb_tourneyid
        :return:
        """
        tourney_ids = self.tournaments.keys()

        # clear previous values for updating.
        self.ui.cb_tourneyid.clear()
        self.ui.cb_tourneyid.addItems(tourney_ids)

    def update_tourneys(self):
        """
        Adds tournaments to dict of tourneys.
        :return:
        """
        tourney_ids = self.in_files.list_ids()
        self.tournaments = {id_:TourneyInfo(id_) for id_ in tourney_ids}


class TourneyInfo(object):
    def __init__(self, id_):
        self.id_ = id_
        self.name = ''
        self.date = ''
        self.buyin = ''
        self.type = ''

    def format_date(self, date):
        y, m, d = date.strip('()').replace(' ', '').split(',')

        # Add 0 to single digit dates
        return y + m.zfill(2) + d.zfill(2)

    def get_file_lines(self):
        """
        Will get the necessary info for a tournament to be written to the top of the file.
        :return:
            A list of lines to write to the file.
        """
        return [self.id_, self.name, self.date, self.buyin, self.type]

    def set_values(self, value_list):
        methods = {0: self.update_name, 1: self.update_buyin, 2: self.update_date, 3: self.update_type}
        for idx in range(len(value_list)):
            methods[idx](value_list[idx])

    def update_buyin(self, buyin):
        self.buyin = buyin

    def update_date(self, date):
        self.date = self.format_date(date)

    def update_name(self, name):
        self.name = name

    def update_type(self, type):
        self.type = type
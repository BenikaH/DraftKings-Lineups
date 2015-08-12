from PyQt4 import QtCore, QtGui
from ownership_barchart import BarChart

class ChartFrame(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.resize(800,585)

        self.scroll_area = QtGui.QScrollArea(self)
        self.scroll_area.resize(795,570)

        self.contents = QtGui.QWidget()
        self.contents.resize(2000, 550)

        self.scroll_area.setWidget(self.contents)

        self.main_box = QtGui.QVBoxLayout(self.contents)


class PercentBar(ChartFrame):
    """
    The frame for the bar charts with a horizontal scroll
    """
    def __init__(self, parent=None):
        ChartFrame.__init__(self, parent)

        self.top_frame = QtGui.QHBoxLayout()
        self.main_box.addLayout(self.top_frame)

        self.bot_frame = QtGui.QHBoxLayout()
        self.main_box.addLayout(self.bot_frame)

    def add_top_chart(self, chart):
        self.top_frame.addWidget(chart)

    def add_bot_chart(self, chart):
        self.bot_frame.addWidget(chart)

    def del_layout(self):
        """
        Clears the layouts so can reload new tournaments.
        :return:
        """
        for layout in [self.top_frame, self.bot_frame]:
            for i in range(layout.count()):
                layout.itemAt(i).widget().close()

class LineupScatter(ChartFrame):
    """
    The frame for the scatter plot showing individual player selections.
    """
    def __init__(self, parent=None):
        ChartFrame.__init__(self, parent)

    def add_chart(self, chart):
        self.main_box.addWidget(chart)

    def del_layout(self):
        for i in range(self.main_box.count()):
            self.main_box.itemAt(i).widget().close()
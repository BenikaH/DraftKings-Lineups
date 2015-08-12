from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.cm as cm

class BarChart(FigureCanvas):
    baseball_cols = {'P':5, 'C':3, '1B':3, '2B':3, 'SS':3, '3B':3, 'OF':6}
    pos_order = ['P', 'C', '1B', '2B', '3B', 'SS', 'OF']

    def __init__(self, parent, position, ownership_dict):
        self.ncols = self.baseball_cols[position]
        self.position = position

        width = self.ncols
        height = 2.75
        dpi = 100
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.subplots_adjust(bottom=0.35)

        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Fixed,
                                   QtGui.QSizePolicy.Fixed)
        FigureCanvas.updateGeometry(self)

        names, perc_owned = self.get_axes_vals(ownership_dict)
        self.plot_figure(names, perc_owned)

    def get_axes_vals(self, ownerships):
        """
        Gets the values for the axes used in the bar chart from
        the ownership dictionary.
        :param ownerships:
            Dictionary given to the class of ownership percentages
            by position.
        :return:
            A list of player names (x-axis labels)
            A list of percentages as floats (y-axis values)
        """
        names = []
        perc_owned = []
        for n, (name, perc) in enumerate(sorted(ownerships.items(),
                key= lambda x: x[1], reverse=True), start=1):
            names.append(name)
            perc_owned.append(perc)
            if n == self.ncols:
                break

        # Fill in blank values.
        fill_needed = self.ncols - len(names)
        names += [''] * fill_needed
        perc_owned += [0.0 for i in range(fill_needed)]

        return names, perc_owned

    def plot_figure(self, x_labels, y_vals):
        """
        Creates the plot with the given x and y values.
        Also sets the visual params.
        :param x_labels:
            names of players (used for labels)
        :param y_vals:
            values of ownership.
        :return:
        """
        width = 0.35
        x_vals = range(self.ncols)
        for i in range(self.ncols):
            color_val = y_vals[i]/100.0 + 0.4
            if color_val > 1.0:
                color_val = 1.0
            self.axes.bar(x_vals[i]+width, y_vals[i], width=width, color=cm.Reds(color_val))

        # Set the visual options of the plots
        self.axes.set_xticks([x+width*3/2 for x in x_vals])
        self.axes.set_xticklabels(x_labels, rotation=90, size=7)
        self.axes.set_yticks(range(0, 110, 10))
        self.axes.tick_params(axis='y', labelsize=8)
        self.axes.set_title(self.position, fontsize=10)
        self.axes.set_axis_bgcolor('#242426')
        self.axes.grid(axis='y', color='w', linestyle='-')
        self.axes.set_axisbelow(True)
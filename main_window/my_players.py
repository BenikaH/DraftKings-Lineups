from PyQt4 import QtGui, QtCore

class PlayerTable(QtGui.QTableWidget):
    def __init__(self, parent, game):
        QtGui.QTableWidget.__init__(self, parent)
        self.parent = parent
        self.game = game

        self.setup()

    def clear_frame(self):
        """Clears the frame on each update (choosing new tournament)"""
        layout = self.parent.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().close()

    def create_table(self, player_list):
        """
        Creates the TableWidget from the list of players.
        """
        columns = ['Pos', 'Player', 'All%', 'Select%']

        nrows = len(player_list)
        ncols = len(columns)
        table = QtGui.QTableWidget(nrows, ncols, self.parent)

        table.setHorizontalHeaderLabels(columns)

        for n, record in enumerate(player_list):
            for m, col in enumerate(columns):
                cell = QtGui.QTableWidgetItem(record[m])
                if m >= 2:
                    cell.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                # Set the cell as enabled and selectable, but not editable.
                cell.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                table.setItem(n, m, cell)

        table.resizeColumnsToContents()
        table.setColumnWidth(1, 200)
        self.parent.layout().addWidget(table)

    def format_players(self):
        """
        Formats the players in a list that will be easier to use
        with QTableWidget
        """
        all_ownership = self.game.get_all_ownership()
        followed_ownership = self.game.get_following_ownership()

        results = []
        for team in self.game.my_players:
            for n, player in enumerate(team):
                if player in [name[1] for name in results]:
                    continue
                pos = self.game.POSITIONS[n]
                ownership = [str(all_ownership[pos].get(player, 0.0)),
                             str(followed_ownership[pos].get(player, 0.0))]
                results.append([pos, player] + ownership)

        return results

    def no_result(self, parent):
        """
        Will display a label notifying that there is no data instead of
        inserting the player table.
        """
        label = QtGui.QLabel('No data for this tournament', parent)
        label.setAlignment(QtCore.Qt.AlignCenter)
        parent.layout().addWidget(label)

    def setup(self):
        self.clear_frame()
        if not self.game.my_players:
            return self.no_result(self.parent)
        else:
            return self.create_table(self.format_players())




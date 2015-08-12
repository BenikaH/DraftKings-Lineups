# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_raw.ui'
#
# Created: Wed Aug 12 15:13:55 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1058, 876)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(255, 220, 161, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.var_entries = QtGui.QLabel(self.centralwidget)
        self.var_entries.setText(_fromUtf8(""))
        self.var_entries.setObjectName(_fromUtf8("var_entries"))
        self.gridLayout_2.addWidget(self.var_entries, 5, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.cb_ids = QtGui.QComboBox(self.centralwidget)
        self.cb_ids.setObjectName(_fromUtf8("cb_ids"))
        self.gridLayout_2.addWidget(self.cb_ids, 1, 0, 1, 2)
        self.var_date = QtGui.QLabel(self.centralwidget)
        self.var_date.setText(_fromUtf8(""))
        self.var_date.setObjectName(_fromUtf8("var_date"))
        self.gridLayout_2.addWidget(self.var_date, 2, 1, 1, 1)
        self.var_buyin = QtGui.QLabel(self.centralwidget)
        self.var_buyin.setText(_fromUtf8(""))
        self.var_buyin.setObjectName(_fromUtf8("var_buyin"))
        self.gridLayout_2.addWidget(self.var_buyin, 3, 1, 1, 1)
        self.var_type = QtGui.QLabel(self.centralwidget)
        self.var_type.setText(_fromUtf8(""))
        self.var_type.setObjectName(_fromUtf8("var_type"))
        self.gridLayout_2.addWidget(self.var_type, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 2, 1)
        self.groupBox_mystats = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_mystats.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_mystats.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_mystats.setFlat(False)
        self.groupBox_mystats.setCheckable(False)
        self.groupBox_mystats.setObjectName(_fromUtf8("groupBox_mystats"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_mystats)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_table = QtGui.QWidget(self.groupBox_mystats)
        self.widget_table.setObjectName(_fromUtf8("widget_table"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_table)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3.addWidget(self.widget_table)
        self.gridLayout.addWidget(self.groupBox_mystats, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_To_Following = QtGui.QAction(MainWindow)
        self.actionAdd_To_Following.setObjectName(_fromUtf8("actionAdd_To_Following"))
        self.actionEdit_Tourney_Info = QtGui.QAction(MainWindow)
        self.actionEdit_Tourney_Info.setObjectName(_fromUtf8("actionEdit_Tourney_Info"))
        self.actionSet_My_Name = QtGui.QAction(MainWindow)
        self.actionSet_My_Name.setObjectName(_fromUtf8("actionSet_My_Name"))
        self.menuSettings.addAction(self.actionAdd_To_Following)
        self.menuSettings.addAction(self.actionEdit_Tourney_Info)
        self.menuSettings.addAction(self.actionSet_My_Name)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Graphs", None))
        self.label_2.setText(_translate("MainWindow", "For future use.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Future", None))
        self.label_5.setText(_translate("MainWindow", "Buy In:", None))
        self.label.setText(_translate("MainWindow", "Tourney Info", None))
        self.label_3.setText(_translate("MainWindow", "Date:", None))
        self.label_9.setText(_translate("MainWindow", "Entries:", None))
        self.label_7.setText(_translate("MainWindow", "Type:", None))
        self.groupBox_mystats.setTitle(_translate("MainWindow", "My Players", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionAdd_To_Following.setText(_translate("MainWindow", "Add To Following", None))
        self.actionAdd_To_Following.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionEdit_Tourney_Info.setText(_translate("MainWindow", "Edit Tourney Info", None))
        self.actionSet_My_Name.setText(_translate("MainWindow", "Set My Name", None))


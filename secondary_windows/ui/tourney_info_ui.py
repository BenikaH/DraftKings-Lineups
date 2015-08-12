# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tourney_info_window.ui'
#
# Created: Sun Aug  2 08:56:18 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(351, 157)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cb_tourneyid = QtGui.QComboBox(Dialog)
        self.cb_tourneyid.setWhatsThis(_fromUtf8(""))
        self.cb_tourneyid.setObjectName(_fromUtf8("cb_tourneyid"))
        self.gridLayout.addWidget(self.cb_tourneyid, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cb_buyin = QtGui.QComboBox(Dialog)
        self.cb_buyin.setEditable(True)
        self.cb_buyin.setObjectName(_fromUtf8("cb_buyin"))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.cb_buyin.setItemText(0, _fromUtf8(""))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.cb_buyin.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cb_buyin, 3, 0, 1, 1)
        self.cb_date = QtGui.QDateEdit(Dialog)
        self.cb_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(0, 0, 0)))
        self.cb_date.setMinimumDate(QtCore.QDate(2014, 1, 1))
        self.cb_date.setCalendarPopup(True)
        self.cb_date.setCurrentSectionIndex(1)
        self.cb_date.setObjectName(_fromUtf8("cb_date"))
        self.gridLayout.addWidget(self.cb_date, 3, 1, 1, 1)
        self.cb_type = QtGui.QComboBox(Dialog)
        self.cb_type.setObjectName(_fromUtf8("cb_type"))
        self.cb_type.addItem(_fromUtf8(""))
        self.cb_type.addItem(_fromUtf8(""))
        self.cb_type.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cb_type, 3, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.le_name = QtGui.QLineEdit(Dialog)
        self.le_name.setReadOnly(True)
        self.le_name.setObjectName(_fromUtf8("le_name"))
        self.gridLayout.addWidget(self.le_name, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btn_submit = QtGui.QPushButton(Dialog)
        self.btn_submit.setObjectName(_fromUtf8("btn_submit"))
        self.gridLayout.addWidget(self.btn_submit, 4, 1, 1, 1)
        self.btn_close = QtGui.QPushButton(Dialog)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.gridLayout.addWidget(self.btn_close, 4, 2, 1, 1)
        self.btn_refresh = QtGui.QPushButton(Dialog)
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.gridLayout.addWidget(self.btn_refresh, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tourney Info", None))
        self.label_5.setText(_translate("Dialog", "Tournament Type", None))
        self.label_2.setText(_translate("Dialog", "Tournament Name", None))
        self.label.setText(_translate("Dialog", "Tournament ID", None))
        self.cb_buyin.setItemText(1, _translate("Dialog", "$1", None))
        self.cb_buyin.setItemText(2, _translate("Dialog", "$2", None))
        self.cb_buyin.setItemText(3, _translate("Dialog", "$5", None))
        self.cb_buyin.setItemText(4, _translate("Dialog", "$10", None))
        self.cb_buyin.setItemText(5, _translate("Dialog", "$25", None))
        self.cb_date.setDisplayFormat(_translate("Dialog", "M/d", None))
        self.cb_type.setItemText(0, _translate("Dialog", "50/50", None))
        self.cb_type.setItemText(1, _translate("Dialog", "GPP", None))
        self.cb_type.setItemText(2, _translate("Dialog", "League", None))
        self.label_4.setText(_translate("Dialog", "Date", None))
        self.label_3.setText(_translate("Dialog", "Buy In", None))
        self.btn_submit.setText(_translate("Dialog", "Submit", None))
        self.btn_close.setText(_translate("Dialog", "Close", None))
        self.btn_refresh.setText(_translate("Dialog", "Refresh", None))


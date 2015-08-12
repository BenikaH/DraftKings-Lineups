# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'greats_win_raw.ui'
#
# Created: Sun Jul  5 13:33:56 2015
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
        Dialog.resize(501, 417)
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(20, 250))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 2, 3, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_2.setText(_translate("Dialog", "Delete", None))
        self.pushButton.setText(_translate("Dialog", "Add", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'greats_win_raw.ui'
#
# Created: Sun Jul  5 13:58:39 2015
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
        Dialog.resize(501, 417)
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_del = QtGui.QPushButton(Dialog)
        self.btn_del.setObjectName(_fromUtf8("btn_del"))
        self.gridLayout.addWidget(self.btn_del, 3, 2, 1, 1)
        self.le_names = QtGui.QLineEdit(Dialog)
        self.le_names.setObjectName(_fromUtf8("le_names"))
        self.gridLayout.addWidget(self.le_names, 0, 0, 1, 2)
        self.btn_add = QtGui.QPushButton(Dialog)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.gridLayout.addWidget(self.btn_add, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.list_names = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_names.sizePolicy().hasHeightForWidth())
        self.list_names.setSizePolicy(sizePolicy)
        self.list_names.setMinimumSize(QtCore.QSize(20, 250))
        self.list_names.setMaximumSize(QtCore.QSize(200, 16777215))
        self.list_names.setBaseSize(QtCore.QSize(0, 0))
        self.list_names.setObjectName(_fromUtf8("list_names"))
        self.gridLayout.addWidget(self.list_names, 0, 2, 3, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Players To Follow", None))
        self.btn_del.setText(_translate("Dialog", "Delete", None))
        self.btn_add.setText(_translate("Dialog", "Add", None))


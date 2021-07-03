# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from . import images_rc

class Ui_tombola(object):
    def setupUi(self, tombola):
        tombola.setObjectName("tombola")
        tombola.resize(197, 366)
        tombola.setWindowTitle(" ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tombola.setWindowIcon(icon)
        tombola.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.centralwidget = QtWidgets.QWidget(tombola)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_num = QtWidgets.QLabel(self.centralwidget)
        self.lbl_num.setEnabled(True)
        self.lbl_num.setGeometry(QtCore.QRect(40, 30, 121, 191))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.lbl_num.setFont(font)
        self.lbl_num.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lbl_num.setText("")
        self.lbl_num.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_num.setObjectName("lbl_num")
        self.lne_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lne_num.setGeometry(QtCore.QRect(40, 240, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lne_num.setFont(font)
        self.lne_num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lne_num.setObjectName("lne_num")
        self.pb_start = QtWidgets.QPushButton(self.centralwidget)
        self.pb_start.setGeometry(QtCore.QRect(40, 290, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start.setFont(font)
        self.pb_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_start.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.pb_start.setObjectName("pb_start")
        tombola.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tombola)
        self.statusbar.setObjectName("statusbar")
        tombola.setStatusBar(self.statusbar)

        self.retranslateUi(tombola)
        QtCore.QMetaObject.connectSlotsByName(tombola)

    def retranslateUi(self, tombola):
        _translate = QtCore.QCoreApplication.translate
        self.lne_num.setText(_translate("tombola", "2"))
        self.pb_start.setText(_translate("tombola", "Start"))


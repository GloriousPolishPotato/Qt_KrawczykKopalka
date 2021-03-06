# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zmiana_widoku.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#           Modyfikacje:
#           07.11.2020 | Szymon Krawczyk     | Zmiana drugiego okna na klasę Interface służącą jako demo
#                                            |   rysowania dynamicznie generowanych linii
#

from PyQt5 import QtCore, QtGui, QtWidgets
from zmiana_widoku.lines import Interface

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: Wheat")
        self.page.setObjectName("page")
        self.Screen1pushButton = QtWidgets.QPushButton(self.page)
        self.Screen1pushButton.setGeometry(QtCore.QRect(290, 260, 171, 41))
        self.Screen1pushButton.setObjectName("Screen1pushButton")
        self.stackedWidget.addWidget(self.page)

        # self.page_2 = QtWidgets.QWidget()
        self.page_2 = Interface()       # nowa klasa
        self.page_2.setStyleSheet("background-color: SkyBlue")
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(260, 250, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.screen2pushButton = QtWidgets.QPushButton(self.page_2)
        self.screen2pushButton.setGeometry(QtCore.QRect(260, 300, 211, 23))
        self.screen2pushButton.setObjectName("screen2pushButton")
        self.stackedWidget.addWidget(self.page_2)
        self.mainPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainPushButton.setGeometry(QtCore.QRect(150, 560, 461, 23))
        self.mainPushButton.setObjectName("mainPushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Screen1pushButton.setText(_translate("MainWindow", "Nie klikaj mnie!"))
        self.label.setText(_translate("MainWindow", "i co zrobiłeś?"))
        self.screen2pushButton.setText(_translate("MainWindow", "Powrót"))
        self.mainPushButton.setText(_translate("MainWindow", "Ekran główny"))
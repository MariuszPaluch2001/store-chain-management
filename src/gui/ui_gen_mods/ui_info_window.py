# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Info_Window(object):
    def setupUi(self, Info_Window):
        if not Info_Window.objectName():
            Info_Window.setObjectName(u"Info_Window")
        Info_Window.resize(800, 600)
        self.centralwidget = QWidget(Info_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(60, 90, 361, 461))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 290, 121, 41))
        Info_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Info_Window)
        self.statusbar.setObjectName(u"statusbar")
        Info_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Info_Window)

        QMetaObject.connectSlotsByName(Info_Window)
    # setupUi

    def retranslateUi(self, Info_Window):
        Info_Window.setWindowTitle(QCoreApplication.translate("Info_Window", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("Info_Window", u"Refresh", None))
    # retranslateUi


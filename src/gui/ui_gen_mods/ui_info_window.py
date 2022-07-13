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
        self.Refresh_Button = QPushButton(self.centralwidget)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setGeometry(QRect(560, 290, 121, 41))
        self.Query_Table = QTableWidget(self.centralwidget)
        if (self.Query_Table.columnCount() < 5):
            self.Query_Table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.Query_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Query_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Query_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Query_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Query_Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Query_Table.setObjectName(u"Query_Table")
        self.Query_Table.setGeometry(QRect(40, 80, 501, 471))
        Info_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Info_Window)
        self.statusbar.setObjectName(u"statusbar")
        Info_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Info_Window)

        QMetaObject.connectSlotsByName(Info_Window)
    # setupUi

    def retranslateUi(self, Info_Window):
        Info_Window.setWindowTitle(QCoreApplication.translate("Info_Window", u"MainWindow", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Info_Window", u"Refresh", None))
        ___qtablewidgetitem = self.Query_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Info_Window", u"Product Name", None));
        ___qtablewidgetitem1 = self.Query_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Info_Window", u"Amount", None));
        ___qtablewidgetitem2 = self.Query_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Info_Window", u"Delivery Date", None));
        ___qtablewidgetitem3 = self.Query_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Info_Window", u"Exp. Date", None));
        ___qtablewidgetitem4 = self.Query_Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Info_Window", u"Store Name", None));
    # retranslateUi


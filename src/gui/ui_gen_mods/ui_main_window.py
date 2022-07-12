# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 110, 202, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Add_Product_Button = QPushButton(self.verticalLayoutWidget)
        self.Add_Product_Button.setObjectName(u"Add_Product_Button")

        self.verticalLayout.addWidget(self.Add_Product_Button)

        self.Add_Delivery_Button = QPushButton(self.verticalLayoutWidget)
        self.Add_Delivery_Button.setObjectName(u"Add_Delivery_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_Delivery_Button.sizePolicy().hasHeightForWidth())
        self.Add_Delivery_Button.setSizePolicy(sizePolicy)
        self.Add_Delivery_Button.setMinimumSize(QSize(158, 25))

        self.verticalLayout.addWidget(self.Add_Delivery_Button)

        self.Info_Product_Button = QPushButton(self.verticalLayoutWidget)
        self.Info_Product_Button.setObjectName(u"Info_Product_Button")

        self.verticalLayout.addWidget(self.Info_Product_Button)

        self.Exit_Button = QPushButton(self.verticalLayoutWidget)
        self.Exit_Button.setObjectName(u"Exit_Button")

        self.verticalLayout.addWidget(self.Exit_Button)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 130, 211, 201))
        self.label.setPixmap(QPixmap(u"resources/mongo.jpeg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Add_Product_Button.setText(QCoreApplication.translate("MainWindow", u"Add new product", None))
        self.Add_Delivery_Button.setText(QCoreApplication.translate("MainWindow", u"Add new delivery", None))
        self.Info_Product_Button.setText(QCoreApplication.translate("MainWindow", u"Info about products", None))
        self.Exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_delivery.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Add_Delivery_Window(object):
    def setupUi(self, Add_Delivery_Window):
        if not Add_Delivery_Window.objectName():
            Add_Delivery_Window.setObjectName(u"Add_Delivery_Window")
        Add_Delivery_Window.resize(800, 600)
        self.centralwidget = QWidget(Add_Delivery_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 70, 381, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 500, 151, 41))
        Add_Delivery_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Add_Delivery_Window)
        self.statusbar.setObjectName(u"statusbar")
        Add_Delivery_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Delivery_Window)

        QMetaObject.connectSlotsByName(Add_Delivery_Window)
    # setupUi

    def retranslateUi(self, Add_Delivery_Window):
        Add_Delivery_Window.setWindowTitle(QCoreApplication.translate("Add_Delivery_Window", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Add_Delivery_Window", u"   Amount                ", None))
        self.label_2.setText(QCoreApplication.translate("Add_Delivery_Window", u"   Delivery Date     ", None))
        self.label_3.setText(QCoreApplication.translate("Add_Delivery_Window", u"   Expiration Date ", None))
        self.label_4.setText(QCoreApplication.translate("Add_Delivery_Window", u"   Product name    ", None))
        self.label_5.setText(QCoreApplication.translate("Add_Delivery_Window", u"   Store name         ", None))
        self.pushButton.setText(QCoreApplication.translate("Add_Delivery_Window", u"Submit", None))
    # retranslateUi


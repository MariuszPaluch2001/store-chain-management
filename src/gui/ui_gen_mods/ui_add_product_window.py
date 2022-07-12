# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Add_Product(object):
    def setupUi(self, Add_Product):
        if not Add_Product.objectName():
            Add_Product.setObjectName(u"Add_Product")
        Add_Product.resize(800, 600)
        self.centralwidget = QWidget(Add_Product)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 80, 401, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Product_Name_Input = QLineEdit(self.verticalLayoutWidget)
        self.Product_Name_Input.setObjectName(u"Product_Name_Input")

        self.horizontalLayout_5.addWidget(self.Product_Name_Input)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Product_Mass_Input = QLineEdit(self.verticalLayoutWidget)
        self.Product_Mass_Input.setObjectName(u"Product_Mass_Input")

        self.horizontalLayout_2.addWidget(self.Product_Mass_Input)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Product_Mass_Unit_Input = QLineEdit(self.verticalLayoutWidget)
        self.Product_Mass_Unit_Input.setObjectName(u"Product_Mass_Unit_Input")

        self.horizontalLayout_4.addWidget(self.Product_Mass_Unit_Input)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(430, 210, 291, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.Producent_Names_Combo = QComboBox(self.horizontalLayoutWidget_5)
        self.Producent_Names_Combo.setObjectName(u"Producent_Names_Combo")

        self.horizontalLayout_6.addWidget(self.Producent_Names_Combo)

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(430, 260, 291, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.Producent_TIN_Input = QLineEdit(self.horizontalLayoutWidget_6)
        self.Producent_TIN_Input.setObjectName(u"Producent_TIN_Input")

        self.horizontalLayout_7.addWidget(self.Producent_TIN_Input)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 300, 399, 261))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Product_Description_Input = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.Product_Description_Input.setObjectName(u"Product_Description_Input")

        self.horizontalLayout_3.addWidget(self.Product_Description_Input)

        self.label_5 = QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.Insert_Button = QPushButton(self.centralwidget)
        self.Insert_Button.setObjectName(u"Insert_Button")
        self.Insert_Button.setGeometry(QRect(498, 384, 171, 31))
        Add_Product.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Add_Product)
        self.statusbar.setObjectName(u"statusbar")
        Add_Product.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Product)

        QMetaObject.connectSlotsByName(Add_Product)
    # setupUi

    def retranslateUi(self, Add_Product):
        Add_Product.setWindowTitle(QCoreApplication.translate("Add_Product", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Add_Product", u"Product name", None))
        self.label.setText(QCoreApplication.translate("Add_Product", u"Mass                  ", None))
        self.label_4.setText(QCoreApplication.translate("Add_Product", u"Mass unit         ", None))
        self.label_2.setText(QCoreApplication.translate("Add_Product", u"Producent name", None))
        self.label_6.setText(QCoreApplication.translate("Add_Product", u"TIN", None))
        self.label_5.setText(QCoreApplication.translate("Add_Product", u"Description     ", None))
        self.Insert_Button.setText(QCoreApplication.translate("Add_Product", u"Submit", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Students/flashcard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class flashcard(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 427)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(201, 21, 210, 63))
        self.label.setStyleSheet("font: 48pt \"Futura\";\n"
                                 "color: rgb(253, 128, 8);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_2.setGeometry(QtCore.QRect(201, 92, 176, 63))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_2.setStyleSheet("font: 48pt \"Futura\";\n"
                                   "color: rgb(253, 128, 8);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 340, 113, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 340, 113, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 108, 33))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_3.setStyleSheet("font: 25pt \"Futura\";\n"
                                   "color: rgb(253, 128, 8);")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(190, 230, 264, 49))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setStyleSheet("font: 18pt \"Andale Mono\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setStyleSheet("font: 18pt \"Andale Mono\";")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Flashcard"))
        self.label_2.setText(_translate("Dialog", "ひらがな"))
        self.pushButton.setText(_translate("Dialog", "Next"))
        self.pushButton_2.setText(_translate("Dialog", "Exit"))
        self.label_3.setText(_translate("Dialog", "Hiragana"))
        self.radioButton_2.setText(_translate("Dialog", "I don\'t know this word"))
        self.radioButton.setText(_translate("Dialog", "I know this word"))
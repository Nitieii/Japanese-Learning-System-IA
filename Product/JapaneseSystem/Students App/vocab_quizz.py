# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vocab_quiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class vocabQuiz(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 554)
        Dialog.setMinimumSize(QtCore.QSize(600, 300))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 411, 51))
        self.label.setStyleSheet("font: 48pt \"Futura\";\n"
                                 "color: rgb(253, 128, 8);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.label_4.setStyleSheet("font: 20pt \"Futura\";\n"
                                   "color: rgb(252, 0, 240);")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 90, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(320, 90, 51, 31))
        self.label_5.setStyleSheet("font: 20pt \"Futura\";\n"
                                   "color: rgb(252, 0, 240);")
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 90, 261, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 130, 113, 41))
        self.pushButton.setStyleSheet("color: rgb(236, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 470, 113, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 30, 131, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setStyleSheet("font: 15pt \"Futura\";\n"
                                   "color: rgb(253, 128, 8);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 20pt \"Futura\";\n"
                                   "color: rgb(253, 128, 8);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 190, 571, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Words', 'Enter Answer'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Vocabulary Quizz"))
        self.label_4.setText(_translate("Dialog", "Number of Vocab:"))
        self.comboBox.setItemText(0, _translate("Dialog", "5"))
        self.comboBox.setItemText(1, _translate("Dialog", "10"))
        self.comboBox.setItemText(2, _translate("Dialog", "15"))
        self.comboBox.setItemText(3, _translate("Dialog", "20"))
        self.comboBox.setItemText(4, _translate("Dialog", "25"))
        self.comboBox.setItemText(5, _translate("Dialog", "30"))
        self.label_5.setText(_translate("Dialog", "Unit"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Greetings"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Friends"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Shopping"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "TheFirstDate"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Trip"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Family"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "Vacation"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Feelings"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Job"))
        self.comboBox_2.setItemText(9, _translate("Dialog", "ValentineDay"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "LostandFound"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Shopping"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "Education"))
        self.pushButton.setText(_translate("Dialog", "Generate"))
        self.pushButton_2.setText(_translate("Dialog", "Submit"))
        self.label_9.setText(_translate("Dialog", "Timer:"))
        self.label_2.setText(_translate("Dialog", "00:00"))
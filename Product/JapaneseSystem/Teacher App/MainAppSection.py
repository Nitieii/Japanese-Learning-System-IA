import csv
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout, QPushButton

from listfunct import Ui_MainWindow as mainW
from login import logIn
from history import history
from studentsList import student_list


class Home(QMainWindow, mainW):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_out)
        self.pushButton_3.clicked.connect(self.students_list)

        logVar = LogIn(self)
        logVar.show()

    def students_list(self):
        listS = studentList(self)
        listS.show()

    def log_out(self):
        sys.exit()


username = "sensei"
password = "sensei"


class LogIn(logIn):
    def __init__(self, parent=None):
        super(LogIn, self).__init__(parent)
        self.setupUi(self)

        # Set the placeholder text for the input of username and password
        self.lineEdit.setPlaceholderText("Username")
        self.lineEdit_2.setPlaceholderText("Password")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        # If the user click on the exit button, close the app
        self.pushButton_2.clicked.connect(self.exitApp)
        # If the user click on the log in button, check the username and password and enter the App.
        self.pushButton.clicked.connect(self.enterApp)

    def exitApp(self):
        sys.exit(0)  # 0 means without errors

    def enterApp(self):
        if self.lineEdit.text() == username and self.lineEdit_2.text() == password:
            self.close()
        else:
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")


class studentList(student_list):
    def __init__(self, parent=None):
        super(studentList, self).__init__(parent)
        self.setupUi(self)
        self.loadStudentsList()

    def loadStudentsList(self):

        vbox = QVBoxLayout()

        with open("../Students App/StudentAccs/studentsAccs.csv") as studentL:
            accountL = []
            studentName = []
            file = csv.reader(studentL, delimiter=",")  # Split the data by the ","
            for row in file:
                for acc in row:
                    accountL.append(acc)  # Append all the words in the list into the vocab array

            for i in range(0, len(accountL), 3):
                studentName.append(accountL[i])

            for i in studentName:
                btn = QPushButton('{}'.format(i), self)
                vbox.addWidget(btn)
                vbox.addStretch(1)
                self.groupBox.setLayout(vbox)

    def historyS(self):
        historySS = historySt(self)
        historySS.show()


class historySt(history):
    def __init__(self, parent=None):
        super(historySt, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)  # creating the application with arguments from user
mainW = Home()  # setting the main window to the Home UI
mainW.show()
app.exec_()

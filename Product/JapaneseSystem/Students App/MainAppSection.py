import sys, csv, os, random, fnmatch
import unicodedata
from datetime import date

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from Listfunct import Ui_MainWindow as mainW
from finishFlash import finishflash
from finishQuiz import finishquizz
from flashcard import flashcard
from history import history
from kanji import kanji
from log_in import logIn
from vocab_list import vocab_list
from vocab_quizz import vocabQuiz
from SignUp import signUp
from SignUpSuccess import signUpSuc
from historyQuiz import historyquizz

sys.setrecursionlimit(10 ** 6)


class Home(QMainWindow, mainW):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_out)
        self.pushButton_3.clicked.connect(self.list_vocab)
        self.pushButton_4.clicked.connect(self.vocab_quizz)
        self.pushButton_5.clicked.connect(self.check_flash)
        self.pushButton_6.clicked.connect(self.kanji)
        self.pushButton_7.clicked.connect(self.historyS)
        logVar = LogIn(self)
        logVar.show()

        # Check if the vocab list is empty or not

    def list_vocab(self):
        listV = VocabList(self)
        listV.show()

    def vocab_quizz(self):
        quizV = VocabQuiz(self)
        quizV.show()

    def finish_quizz(self):
        quizFinish = finishQuizz(self)
        quizFinish.show()

    def flash_card(self):
        flashC = flashCard(self)
        flashC.show()

    def finish_flash(self):
        flashF = finishFlash(self)
        flashF.show()

    def check_flash(self):
        # Check if the vocab list is empty or not
        if os.path.getsize("VocabList/VocabList.csv") == 0:
            self.finish_flash()
        else:
            self.flash_card()

    def historyS(self):
        historys = History(self)
        historys.show()

    def kanji(self):
        kanjiL = Kanji(self)
        kanjiL.show()

    def log_out(self):
        sys.exit()


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
        self.pushButton_3.clicked.connect(self.signup)

    def exitApp(self):
        sys.exit(0)  # 0 means without errors

    def enterApp(self):
        # Set the input to variables
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # Open the database file
        with open("StudentAccs/studentsAccs.csv", "r") as studentAccF:
            studentAccL = []
            students = []
            file = csv.reader(studentAccF, delimiter=",")  # Split the data by the ","
            for row in file:
                students.append(row)
                for detailed in row:
                    studentAccL.append(detailed)

            # Check if the username is on the students account list
            if username in studentAccL:
                # Take out the index of the username in list
                index = studentAccL.index(username)
                Lindex = int(index / 3)
                # Take out the password that match to username
                studentsPassword = students[Lindex][2]

                # Check the password
                if password == studentsPassword:
                    self.close()
                else:
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit.repaint()
                    self.lineEdit_2.repaint()
            # If not, simply empty the input so that the user can input again
            else:
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit.repaint()
                self.lineEdit_2.repaint()

    def signup(self):
        signU = SignUp(self)
        signU.show()


class SignUp(signUp):
    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.exitApp)
        self.pushButton.clicked.connect(self.sUp)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

    def sUp(self):
        name = self.lineEdit.text()
        userName = self.lineEdit_3.text()
        passWord = self.lineEdit_2.text()
        rePassword = self.lineEdit_4.text()

        with open("StudentAccs/studentsAccs.csv", "r+") as StudentAccF:
            accountL = []
            file = csv.reader(StudentAccF, delimiter=",")  # Split the data by the ","
            for row in file:
                for acc in row:
                    accountL.append(acc)  # Append all the words in the list into the vocab array

            if name in accountL or userName in accountL:
                self.lineEdit.setPlaceholderText("Already exist")
                self.lineEdit_3.setPlaceholderText("Already exist")
                self.emptyLineEdit()

            elif passWord != rePassword:
                self.lineEdit_4.setPlaceholderText("Wrong Confirmed Password")
                self.emptyLineEdit()

            elif passWord != rePassword and (name in accountL or userName in accountL):
                self.lineEdit.setPlaceholderText("Already exist")
                self.lineEdit_3.setPlaceholderText("Already exist")
                self.lineEdit_4.setPlaceholderText("Wrong Confirmed Password")
            else:
                StudentAccF.write(name + ",")
                StudentAccF.write(userName + ",")
                StudentAccF.write(passWord + "\n")

                self.close()
                self.successSignUp()

    def exitApp(self):
        self.close()

    def emptyLineEdit(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit.repaint()
        self.lineEdit_2.repaint()
        self.lineEdit_3.repaint()
        self.lineEdit_4.repaint()

    def successSignUp(self):
        succesSU = SignUpS(self)
        succesSU.show()


class SignUpS(signUpSuc):
    def __init__(self, parent=None):
        super(SignUpS, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.extit)

    def extit(self):
        self.close()


global scoreQ


class VocabList(vocab_list):
    def __init__(self, parent=None):
        super(VocabList, self).__init__(parent)
        self.setupUi(self)
        self.loadTable()
        self.pushButton.clicked.connect(self.manual_vocab_add)  # the users press add button
        self.pushButton_2.clicked.connect(self.deleteVocab)  # the users press add button

    def loadTable(self):

        with open("VocabList/VocabList.csv") as mydatabase:  # Open the file
            file = csv.reader(mydatabase, delimiter=",")  # Split the data by the ","

            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table
        self.tableWidget.repaint()

    def manual_vocab_add(self):
        # Assign variables to the input text
        new_vocab = self.lineEdit.text()
        new_definition = self.lineEdit_2.text()

        # Open the file to store all the new vocab
        with open("VocabList/VocabList.csv", "r+") as vocab_listFile:
            vocabL = []
            file = csv.reader(vocab_listFile, delimiter=",")  # Split the data by the ","
            for row in file:
                for vocab in row:
                    vocabL.append(vocab)  # Append all the words in the list into the vocab array

            # Check if the new word is in the file or not
            if new_vocab not in vocabL:
                vocab_listFile.write(new_vocab + ",")
                vocab_listFile.write(new_definition + "\n")

        # Empty the input space for users to continue inputting new words and definitions
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.loadTable()

    def deleteVocab(self):

        global cell_row
        selected_cell = self.tableWidget.selectedItems()

        # Get the row of the selected cell in the QTable
        for item in selected_cell:
            cell_row = item.row()

        # Open the Vocab list file
        with open("VocabList/VocabList.csv", "r") as out_file:
            file = csv.reader(out_file, delimiter=",")  # Split the data by the ","
            vocabArray = []
            output = []

            for word in file:
                vocabArray.append(word)  # Add all the words in the list into the array

        with open("VocabList/VocabList.csv", "r") as out_file_1:
            for line in out_file_1:
                if not line.startswith(vocabArray[cell_row][0]):  # if the line not startwith the String Input
                    # append it to the output list => The name deleted will no longer in the list
                    output.append(line)
            out_file_1.close()

        f = open("VocabList/VocabList.csv", "w")
        f.writelines(output)  # Write the output list to the Database file
        f.close()

        self.tableWidget.clear()  # Clear all the content all the table and reload
        self.loadTable()


scoreQ = 0
correctAnswersIndex = []
correctAnswers = []
wrongAnswers = []
wrongAnswersIndex = []
randomEnglishWords = []
definitionAnswer = []

today = date.today()
d = ""

# Create the correct answers file with the name of current date
fileHistoryNameCorrect = ""
fileHistoryPathCorrect = ""

# Create the wrong answers file with the name of current date
fileHistoryNameWrong = ""
fileHistoryPathWrong = ""


class VocabQuiz(vocabQuiz):
    def __init__(self, parent=None):
        super(VocabQuiz, self).__init__(parent)
        self.start = True
        self.count = 0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generateQ)
        self.pushButton_2.clicked.connect(self.submitQ)
        index = 0

    def generateQ(self):
        self.pushButton.setEnabled(False)
        self.setTheTimer()
        self.generateTable()
        self.addingQ()

    def setTheTimer(self):

        # Set the different timer for each selection
        if self.comboBox.currentText() == "5":
            self.count = 20 * 10
        elif self.comboBox.currentText() == "10":
            self.count = 40 * 10
        elif self.comboBox.currentText() == "15":
            self.count = 60 * 10
        elif self.comboBox.currentText() == "20":
            self.count = 80 * 10
        elif self.comboBox.currentText() == "25":
            self.count = 100 * 10
        else:
            self.count = 120 * 10

        # Set text for the timer label
        self.label_2.setText(str(10))
        self.label_2.repaint()

        if self.count == 0:
            self.start = False

        self.start_action()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):

        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1

            # timer is completed
            if self.count == 0:
                # making flag false
                self.start = False

                # setting text to the label
                self.submitQ()
                # self.close()

        if self.start:
            # getting text from count
            text = str(self.count / 10) + " s"

            # showing text
            self.label_2.setText(text)

    def start_action(self):
        # making flag true
        self.start = True
        # count = 0
        if self.count == 0:
            self.start = False

    def submitQ(self):
        self.count = -1
        self.close()
        self.checkAnswer()
        self.storeResult()
        self.finishQ()

    def generateTable(self):
        # Take the number of row from the user input
        numberOfRow = int(self.comboBox.currentText())
        # Create the table with number of rows above
        self.tableWidget.setRowCount(numberOfRow)
        self.tableWidget.repaint()

    def addingQ(self):

        global chosenTopic
        global numberOfVocab
        global filePath
        global arrayN, definition, definitionAnswer

        numberOfVocab = int(self.comboBox.currentText())
        chosenTopic = self.comboBox_2.currentText()

        # Open the file that have the name of input topic
        fileName = chosenTopic + ".csv"
        filePath = "VocabQuizz/" + fileName

        with open(filePath, "r") as quizzFile:
            file = csv.reader(quizzFile, delimiter=",")

            # Create list of random numbers without duplicating
            output = random.sample(range(numberOfVocab), numberOfVocab)
            global randomEnglishWords
            arrayN = []
            definition = []
            global definitionAnswer

            # Append all the English word into array
            for i in file:
                arrayN.append(i[1])
                definition.append(i[0])

            # Set the text for cell
            for k in range(0, self.tableWidget.rowCount()):
                self.tableWidget.setItem(k, 0, QTableWidgetItem(arrayN[output[k]]))
                definitionAnswer.append(definition[output[k]])
                randomEnglishWords.append(arrayN[output[k]])
        self.tableWidget.repaint()

    def checkAnswer(self):

        # Create Arrays to store corrects and wrong answers
        global scoreQ
        global correctAnswersIndex
        global correctAnswers
        global wrongAnswers
        global wrongAnswersIndex

        scoreQ = 0
        correctAnswers = []
        correctAnswersIndex = []
        wrongAnswers = []
        wrongAnswersIndex = []

        # Loop through all the row in the table to check the inputted answers
        for indexRow in range(self.tableWidget.rowCount()):
            inputAnswer = QTableWidgetItem(self.tableWidget.item(indexRow, 1)).text()
            if unicodedata.normalize('NFC', inputAnswer) == unicodedata.normalize('NFC', definitionAnswer[indexRow]):
                scoreQ += 1
                correctAnswers.append(inputAnswer)
                correctAnswersIndex.append(indexRow)
            else:
                wrongAnswers.append(inputAnswer)
                wrongAnswersIndex.append(indexRow)
        for correctAns in correctAnswers:
            definitionAnswer.remove(correctAns)

    def storeResult(self):

        # Take the date that the quiz is taken
        global today, d, fileHistoryNameWrong, fileHistoryPathWrong, fileHistoryNameCorrect, fileHistoryPathCorrect
        filesNumber = 0

        today = date.today()
        d = today.strftime("%d-%m-%Y")

        root = "History File/"
        files = fnmatch.filter((f for f in os.listdir(root)), f'{d + "-correctAns"}*.csv')  # Check all the files with
        # the provided names in a directory

        if not files:
            filesNumber = ''
        else:
            filesNumber += len(files)


        # Create the correct answers file with the name of current date
        fileHistoryNameCorrect = d + f"-correctAns{filesNumber}.csv"
        fileHistoryPathCorrect = "History File/" + fileHistoryNameCorrect

        # Create the wrong answers file with the name of current date
        fileHistoryNameWrong = d + f"-wrongAns{filesNumber}.csv"
        fileHistoryPathWrong = "History File/" + fileHistoryNameWrong

        # Write the correct answers to the file
        with open(fileHistoryPathCorrect, "w+") as historyFile:
            for i in range(len(correctAnswers)):
                historyFile.write(randomEnglishWords[correctAnswersIndex[i]] + ",")
                historyFile.write(correctAnswers[i] + "\n")
            historyFile.close()

        # Write the wrong answers to the file
        with open(fileHistoryPathWrong, "w+") as historyFile_1:
            for m in range(0, len(wrongAnswers)):
                historyFile_1.write(randomEnglishWords[wrongAnswersIndex[m]] + ",")
                historyFile_1.write(wrongAnswers[m] + ",")
                historyFile_1.write(definitionAnswer[m] + "\n")
            historyFile_1.close()

    def finishQ(self):
        quizFinish = finishQuizz(self)
        quizFinish.show()


class finishQuizz(finishquizz):
    def __init__(self, parent=None):
        super(finishQuizz, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.quitW)
        self.label_2.setText("Your Score is: " + str(scoreQ) + "/" + str(numberOfVocab))
        self.label_2.repaint()
        self.loadResult()
        self.saveRecord()

    def loadResult(self):
        with open(fileHistoryPathWrong, "r+") as resultWrong:  # Open the file
            file = csv.reader(resultWrong, delimiter=",")  # Split the data by the ","

            numberOfRowWrong = len(wrongAnswers)
            # Create the table with number of rows above
            self.tableWidget.setRowCount(numberOfRowWrong)

            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table

            # Reload the content of the table again
            self.tableWidget.repaint()
            resultWrong.close()

        with open(fileHistoryPathCorrect, "r+") as resultCorrect:  # Open the file
            file_1 = csv.reader(resultCorrect, delimiter=",")  # Split the data by the ","

            numberOfRowCorrect = len(correctAnswers)
            # Create the table with number of rows above
            self.tableWidget_2.setRowCount(numberOfRowCorrect)

            for i, row in enumerate(file_1):
                for j, col in enumerate(row):
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table

            # Reload the table
            self.tableWidget_2.repaint()
            resultCorrect.close()

    def saveRecord(self):
        filePath = "Students Record Quiz/historyFile.csv"

        with open(filePath, "a+") as historyFile:
            historyFile.write(d + ",")
            historyFile.write(chosenTopic + ",")
            historyFile.write(str(numberOfVocab) + ",")
            historyFile.write(str(scoreQ) + ",")
            historyFile.write(fileHistoryPathWrong + ",")
            historyFile.write(fileHistoryPathCorrect + "\n")

    def quitW(self):
        self.close()


randomNums = []


class flashCard(flashcard):
    def __init__(self, parent=None):
        super(flashCard, self).__init__(parent)
        self.setupUi(self)
        self.loadCard()
        self.pushButton.clicked.connect(self.loadCard)

    def loadCard(self):
        if (os.path.getsize("VocabList/VocabList.csv")) != 0:
            with open("VocabList/VocabList.csv", "r") as vocab_list_file:
                file = csv.reader(vocab_list_file, delimiter=",")
                vocabArray = []
                output = []

                notTrue = False

                for word in file:
                    vocabArray.append(word)
                # Take a random index number for choosing a random words in the vocab list

                # Infinity set random words and definition for the vocab on the flash card
                while not notTrue:
                    # Check if the next word is duplicate with the previous word or not
                    indexN = random.randint(0, len(vocabArray) - 1)  # Get a random number
                    global randomNums
                    if len(randomNums) < len(vocabArray):
                        if indexN not in randomNums:
                            randomNums.append(indexN)
                            randomVocab = vocabArray[indexN][0]
                            randomDef = vocabArray[indexN][1]
                            notTrue = True
                            # Set Text for word and definition
                            self.label_2.setText(randomVocab)
                            self.label_2.repaint()
                            self.label_3.setText(randomDef)
                            self.label_3.repaint()
                    else:
                        randomNums = []
                        if indexN not in randomNums:
                            randomNums.append(indexN)
                            randomVocab = vocabArray[indexN][0]
                            randomDef = vocabArray[indexN][1]
                            notTrue = True

                            # Set Text for word and definition
                            self.label_2.setText(randomVocab)
                            self.label_2.repaint()
                            self.label_3.setText(randomDef)
                            self.label_3.repaint()

                # If the user know the word, delete the words from the vocab list
                if self.radioButton.isChecked():
                    with open("VocabList/VocabList.csv", "r") as check_file_1:
                        for line in check_file_1:
                            if not line.startswith(vocabArray[indexN][0]):  # if the line not startwith the String Input
                                # append it to the output list => The name deleted will no longer in the list
                                output.append(line)
                        check_file_1.close()

                    f = open("VocabList/VocabList.csv", "w")
                    f.writelines(output)  # Write the output list to the Database file
                    f.close()

        else:
            # If the user know all the vocab list, open finish flash card windows
            self.close()
            self.finish_flash()

    def finish_flash(self):
        flashF = finishFlash(self)
        flashF.show()


class finishFlash(finishflash):
    def __init__(self, parent=None):
        super(finishFlash, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.finish_fl)

    def finish_fl(self):
        self.close()


rowL = 0


class History(history):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.setupUi(self)
        self.loadTable()

    def loadTable(self):

        historyFile = open("Students Record Quiz/historyFile.csv", "r")

        self.tableWidget.setRowCount(len(list(historyFile)))

        self.tableWidget.repaint()

        historyFile = open("Students Record Quiz/historyFile.csv")

        fileH = csv.reader(historyFile, delimiter=",")  # Split the data by the ","
        arrayN = []

        for i in fileH:
            arrayN.append(i)

        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem(arrayN[i][j]))

        self.tableWidget.repaint()

        self.tableWidget.cellClicked.connect(self.historyQ)

    def historyQ(self, row, column):
        global rowL
        rowL = row
        historyQu = HistoryQ(self)
        historyQu.show()


class HistoryQ(historyquizz):
    def __init__(self, parent=None):
        super(HistoryQ, self).__init__(parent)
        self.setupUi(self)
        self.showHistory()

    def showHistory(self):
        # Step 1: Load the score from the history file
        with open("Students Record Quiz/historyFile.csv") as historyFile:
            historyL = []
            file = csv.reader(historyFile, delimiter=",")
            for line in file:
                historyL.append(line)

            scoreHQ = historyL[rowL][3]
            totalHQ = historyL[rowL][2]
            correctAnswersPath = historyL[rowL][5]
            wrongAnswersPath = historyL[rowL][4]
            self.label_2.setText("Score is: " + str(scoreHQ) + "/" + str(totalHQ))
            historyFile.close()

        numberOfRW = len(list(wrongAnswersPath))
        with open(wrongAnswersPath, "r+") as resultWrongF:  # Open the file
            file_3 = csv.reader(resultWrongF, delimiter=",")  # Split the data by the ","

            # Create the table with number of rows above
            self.tableWidget.setRowCount(numberOfRW)

            for i_1, row_1 in enumerate(file_3):
                for j_1, col_1 in enumerate(row_1):
                    self.tableWidget.setItem(i_1, j_1, QTableWidgetItem(col_1))  # Set the data to the table

            # Reload the content of the table again
            self.tableWidget.repaint()
        numberOfRC = len(list(correctAnswersPath))
        with open(correctAnswersPath, "r+") as resultCorrectF:  # Open the file
            file_4 = csv.reader(resultCorrectF, delimiter=",")  # Split the data by the ","
            # Create the table with number of rows above
            self.tableWidget_2.setRowCount(numberOfRC)

            for i_2, row_2 in enumerate(file_4):
                for j_2, col_2 in enumerate(row_2):
                    self.tableWidget_2.setItem(i_2, j_2, QTableWidgetItem(col_2))  # Set the data to the table

            # Reload the table
            self.tableWidget_2.repaint()


class Kanji(kanji):
    def __init__(self, parent=None):
        super(Kanji, self).__init__(parent)
        self.setupUi(self)
        self.loadKanji()
        self.pushButton.clicked.connect(self.loadKanji)

        self.correctAns = ""
        self.previousAns = ""

    def loadKanji(self):

        with open("VocabList/Kanji.csv") as kanji_file:
            file = csv.reader(kanji_file, delimiter=",")
            kanjiArray = []
            flag = True

            for word in file:
                kanjiArray.append(word)

            while flag:  # The program will run until the user exit.

                l = 0
                randomKanji = random.sample(kanjiArray, 4)

                # Array with random indexes
                randomIndexList = []

                while len(randomIndexList) < 4:
                    index = random.randint(0, 3)

                    if index not in randomIndexList:
                        randomIndexList.append(index)

                # Set the text for the label t
                self.label_2.setText(randomKanji[randomIndexList[index]][0])

                # Assign the correct answers for the variable to check it later
                # using global for the purpose of using it in another function
                self.correctAns = randomKanji[randomIndexList[index]][1]
                self.label_2.repaint()

                self.checkAnswer()

                # Assign random text for each button
                self.checkBox.setText(randomKanji[randomIndexList[l]][1])
                self.checkBox.repaint()
                l += 1
                self.checkBox_2.setText(randomKanji[randomIndexList[l]][1])
                self.checkBox_2.repaint()
                l += 1
                self.checkBox_3.setText(randomKanji[randomIndexList[l]][1])
                self.checkBox_3.repaint()
                l += 1
                self.checkBox_4.setText(randomKanji[randomIndexList[l]][1])
                self.checkBox_4.repaint()

                flag = False

    def checkAnswer(self):
        if self.checkBox.isChecked():
            if self.checkBox.text() == self.correctAns:
                self.label_3.setText("Correct")
            else:
                self.label_3.setText("Wrong")
                self.label_3.repaint()
            self.checkBox.setChecked(False)
        elif self.checkBox_2.isChecked():
            if self.checkBox_2.text() == self.correctAns:
                self.label_3.setText("Correct")
            else:
                self.label_3.setText("Wrong")
                self.label_3.repaint()
            self.checkBox_2.setChecked(False)
        elif self.checkBox_3.isChecked():
            if self.checkBox_3.text() == self.correctAns:
                self.label_3.setText("Correct")
            else:
                self.label_3.setText("Wrong")
                self.label_3.repaint()
            self.checkBox_3.setChecked(False)
        else:
            if self.checkBox_4.text() == self.correctAns:
                self.label_3.setText("Correct")
            else:
                self.label_3.setText("Wrong")
                self.label_3.repaint()
            self.checkBox_4.setChecked(False)


app = QApplication(sys.argv)  # creating the application with arguments from user
mainW = Home()  # setting the main window to the Home UI
mainW.show()
app.exec_()

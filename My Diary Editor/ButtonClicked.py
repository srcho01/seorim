from PyQt5.QtWidgets import QMessageBox, QFontDialog
from PyQt5.QtGui import QFont
from DataBase import *
import os

# Folder Path
folder = "c:/Users/srcho/Desktop/AD Project/AD Project Source Code/DB"

def loginFunction(self, input, pwd):
    p = input.text()
    if p == "":
        QMessageBox.information(self, 'Message', '비밀번호를 입력해주세요')
    elif p == pwd:
        self.display.stack0.parent().stack.setCurrentIndex(2)
        self.password.clear()
    else:
        QMessageBox.information(self, 'Message', '비밀번호가 틀렸습니다')
        self.password.clear()


def signUPCheckFunction(self, pwd):
    if pwd == "":
        self.display.stack0.parent().stack.setCurrentIndex(1)
    else:
        QMessageBox.information(self, 'Message', '이미 비밀번호가 설정되어 있습니다')
        self.signUP.setEnabled(False)


def signUPFunction(self, password1, password2):
    pwd1 = password1.text()
    pwd2 = password2.text()

    def passwordClear():
        self.pwd1.clear()
        self.pwd2.clear()

    if pwd1 == pwd2:
        if len(pwd1) < 8:
            QMessageBox.information(self, 'Message', '비밀번호는 8자 이상이어야 합니다')
            passwordClear()
            return False

        else:
            containAlpha = 0
            containNum = 0
            for i in pwd1:
                if i.isalpha():
                    containAlpha = 1
                elif i.isdigit():
                    containNum = 1
            if containAlpha == 1 and containNum == 1:
                setPWD(pwd1)
                passwordClear()
                return True
            else:
                QMessageBox.information(self, 'Message', '비밀번호에 영어와 숫자가 모두 포함되어야 합니다')
                passwordClear()
                return False

    else:
        QMessageBox.information(self, 'Message', '입력한 비밀번호가 서로 다릅니다')
        passwordClear()
        return False


def saveFunction(dateEdit, weatherEdit, titleEdit, textEdit):
    date = dateEdit.date().toString()
    weather = weatherEdit.currentText()
    title = titleEdit.text()
    text = textEdit.toPlainText()
    if title != "" or text != "":
        saveDiary(date, weather, title, text)

def loadFunction(self, dateEdit):
    self.titleLoad.clear()
    self.textLoad.clear()
    date = dateEdit.date().toString()
    text = loadDiary(date)

    if text == False:
        QMessageBox.information(self, 'Message', '작성된 일기가 없습니다')

    else:
        self.weatherLoad.setText(text[0].strip())
        self.titleLoad.setText(text[1].strip())
        for i in range(2,len(text)):
            self.textLoad.append(text[i].strip())


def settingFunction(titleEdit, titleLoad, textEdit, textLoad):
    font, ok = QFontDialog.getFont()
    if ok:
        style = QFont(font).family()
        titleEdit.setFont(QFont(style, 15))
        titleLoad.setFont(QFont(style, 15))
        textEdit.setFont(font)
        textLoad.setFont(font)
        saveFont(QFont(style, 15), font)

def deleteFunction(self, dateEdit, loadEdit, titleEdit, weatherEdit):
    date = dateEdit.date().toString()
    filePath = f"{folder}/{date}.txt"
    if os.path.exists(filePath):
        reply = QMessageBox.warning(self, 'Message', '정말로 일기를 지우시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            os.remove(filePath)
            loadEdit.clear()
            titleEdit.clear()
            weatherEdit.clear()


def clearFunction(self, titleEdit, textEdit, weatherEdit):
    if titleEdit.text() != "" or textEdit.toPlainText() != "":
        reply = QMessageBox.warning(self, 'Message', '정말로 제목과 내용을 모두 지우시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            titleEdit.clear()
            textEdit.clear()
            weatherEdit.setCurrentText("맑음")
import pickle, os
from PyQt5.QtGui import QFont


# Folder Path & Folder Setting
folder = "c:/Users/srcho/Desktop/AD Project/AD Project Source Code/DB" 
if not os.path.exists(folder):
    os.makedirs(folder)


def getPWD():
    try:
        f = open(f"{folder}/pwd.txt", 'r')
        pwd = f.readline().strip()
        f.close()
        return pwd
    except FileNotFoundError:
        return ""
        
def setPWD(pwd):
    f = open(f"{folder}/pwd.txt", 'w')
    f.write(pwd)
    f.close()


def getFont(titleEdit, titleLoad, textEdit, textLoad):
    try:
        f = open(f"{folder}/font.pickle", 'rb')
        font =  pickle.load(f)
        titleEdit.setFont(QFont(font[0], font[1]))
        titleLoad.setFont(QFont(font[0], font[1]))
        textEdit.setFont(QFont(font[2], font[3]))
        textLoad.setFont(QFont(font[2], font[3]))
        f.close()
    except:
        pass
    
def saveFont(titleFont, textFont):
    f = open(f"{folder}/font.pickle", 'wb')
    font = [QFont(titleFont).family(), QFont(titleFont).pointSize(), QFont(textFont).family(), QFont(textFont).pointSize()]
    pickle.dump(font, f)
    f.close()


def saveDiary(date, weather, title, text):
    f = open(f"{folder}/{date}.txt", 'w')
    f.write(weather + "\n" + title + "\n" + text)
    f.close()

def loadDiary(date):
    try:
        f = open(f"{folder}/{date}.txt", 'r')
        return f.readlines()
    except FileNotFoundError:
        return False
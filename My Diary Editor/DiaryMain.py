from PyQt5.QtWidgets import QApplication, QWidget

from ButtonClicked import *
from UI import *
from DataBase import getPWD, getFont


class Diary(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        ### Window ###
        self.display = mainWindow()
        
        ### Variables ###
        self.flag = True
        self.pwd = getPWD()

        # shortcut
        self.login = self.display.stack0.login
        self.signUP = self.display.stack0.signUP
        self.password = self.display.stack0.password

        self.confirm = self.display.stack1.confirm
        self.cancel = self.display.stack1.cancel
        self.pwd1 = self.display.stack1.password1
        self.pwd2 = self.display.stack1.password2

        self.setting = self.display.stack2.setting
        self.resetPWD = self.display.stack2.resetPWD
        self.logout = self.display.stack2.logout

        self.save = self.display.stack2.tabEdit.save
        self.clear = self.display.stack2.tabEdit.clear
        self.titleEdit = self.display.stack2.tabEdit.titleEdit
        self.dateEdit = self.display.stack2.tabEdit.dateEdit
        self.weatherEdit = self.display.stack2.tabEdit.weatherEdit
        self.textEdit = self.display.stack2.tabEdit.textEdit

        self.load = self.display.stack2.tabLoad.load
        self.delete = self.display.stack2.tabLoad.delete
        self.titleLoad = self.display.stack2.tabLoad.titleLoad
        self.dateLoad = self.display.stack2.tabLoad.dateLoad
        self.weatherLoad = self.display.stack2.tabLoad.weatherLoad
        self.textLoad = self.display.stack2.tabLoad.textLoad

        ### Font Setting ###
        getFont(self.titleEdit, self.titleLoad, self.textEdit, self.textLoad)

        ### Event Handler Connect ###
        keys = [self.login, self.signUP, self.confirm, self.cancel, self.save,
                self.load, self.setting, self.resetPWD, self.logout, self.delete, self.clear]

        for key in keys:
            key.clicked.connect(self.buttonClicked)

    
    def buttonClicked(self):

        button = self.sender()
        pageIndex = self.display.stack.currentIndex()

        # page 0 buttons
        if pageIndex == 0:
            if button == self.login:
                self.pwd = getPWD()
                loginFunction(self, self.password, self.pwd)

            elif button == self.signUP:
                self.pwd = getPWD()
                signUPCheckFunction(self, self.pwd)
        
        # page 1 buttons
        elif pageIndex == 1:
            if button == self.confirm:
                success = signUPFunction(self, self.pwd1, self.pwd2)
                if success:
                    if self.flag:
                        self.display.stack1.parent().stack.setCurrentIndex(0)
                    else:
                        self.display.stack1.parent().stack.setCurrentIndex(2)

            elif button == self.cancel:
                if self.flag:
                    self.display.stack1.parent().stack.setCurrentIndex(0)
                else:
                    self.display.stack1.parent().stack.setCurrentIndex(2)

        # page 2 buttons
        elif pageIndex == 2:
            if button == self.save:
                saveFunction(self.dateEdit, self.weatherEdit, self.titleEdit, self.textEdit)
            elif button == self.load:
                loadFunction(self, self.dateLoad)
            elif button == self.setting:
                settingFunction(self.titleEdit, self.titleLoad, self.textEdit, self.textLoad)
            elif button == self.resetPWD:
                self.display.stack2.parent().stack.setCurrentIndex(1)
                self.flag = False
            elif button == self.logout:
                self.display.stack2.parent().stack.setCurrentIndex(0)
            elif button == self.delete:
                deleteFunction(self, self.dateLoad, self.textLoad, self.titleLoad, self.weatherLoad)
            elif button == self.clear:
                clearFunction(self, self.titleEdit, self.textEdit, self.weatherEdit)
        

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    diary = Diary()
    sys.exit(app.exec_())
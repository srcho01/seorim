from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QTabWidget, QDesktopWidget, QStackedLayout
from PyQt5.QtWidgets import  QLineEdit,  QDateEdit, QTextBrowser, QComboBox, QLabel, QPushButton, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ### Set Window ###
        self.setGeometry(0, 0, 1000, 750)
        self.setWindowTitle('My Diary Editor')

        ### Array Center ###
        frame = self.frameGeometry()
        centerPosition = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centerPosition)
        self.move(frame.topLeft())

        ### Set Stacks ###
        self.stack = QStackedLayout(self)
        self.stack0 = login_UI()
        self.stack.addWidget(self.stack0)
        self.stack1 = signUP_UI()
        self.stack.addWidget(self.stack1)
        self.stack2 = diary_UI()
        self.stack.addWidget(self.stack2)

        ### Display ###
        self.show()


class login_UI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):        
        ### Button, Text###
        # program name
        self.name = QLabel(" My Diary Editor ")

        font1 = self.name.font()
        font1.setPointSize(40)
        font1.setFamily('Courgette')
        font1.setBold(True)
        self.name.setFont(font1)

        self.name.setAlignment(Qt.AlignCenter)
        self.name.setStyleSheet("color: black;"
                      "background-color: #79E5CB;"
                      "border-radius:10px;")

        # signIN text
        self.signIN = QLabel("비밀번호를 입력하세요", self)

        font2 = self.signIN.font()
        font2.setPointSize(15)
        self.signIN.setFont(font2)
        self.signIN.setAlignment(Qt.AlignCenter)

        # password
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        # notice
        self.notice = QLabel("※ 프로그램 최초 실행 시, 가입을 먼저 진행해주세요 ※")
        self.notice.setAlignment(Qt.AlignCenter)

        # login
        self.login = QPushButton("LOGIN", self)

        # signUP
        self.signUP = QPushButton("SIGN UP", self)

        ### BoxLayout ###
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        hbox1.addStretch(1)
        hbox1.addWidget(self.name)
        hbox1.addStretch(1)

        hbox2.addWidget(self.signIN)

        hbox3.addWidget(self.notice)

        hbox4.addStretch(1)
        hbox4.addWidget(self.password)
        hbox4.addStretch(1)        

        hbox5.addStretch(1)
        hbox5.addWidget(self.login)
        hbox5.addWidget(self.signUP)
        hbox5.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(6)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addStretch(6)
        
        self.setLayout(vbox)


class signUP_UI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):        
        ### Button, Text ###
        # "Please set your password" text
        self.text1 = QLabel("비밀번호를 설정하세요\n", self)

        font1 = self.text1.font()
        font1.setPointSize(15)
        font1.setBold(True)
        self.text1.setFont(font1)
        self.text1.setAlignment(Qt.AlignCenter)

        # password condition text
        self.text2 = QLabel("비밀번호는 최소 8자리 이상, 영어와 숫자가 모두 포함되어야 합니다", self)
        self.text2.setAlignment(Qt.AlignCenter)

        # password1
        self.pwd1 = QLabel("비밀번호 입력   ")
        self.password1 = QLineEdit()
        self.password1.setEchoMode(QLineEdit.Password)

        # password2
        self.pwd2 = QLabel("비밀번호 재확인")
        self.password2 = QLineEdit()
        self.password2.setEchoMode(QLineEdit.Password)

        # confirm & cancel
        self.confirm = QPushButton("확인", self)
        self.cancel = QPushButton("취소", self)

        ### BoxLayout ###
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        hbox1.addWidget(self.text1)
        hbox2.addWidget(self.text2)

        hbox3.addStretch(1)
        hbox3.addWidget(self.pwd1)
        hbox3.addWidget(self.password1)
        hbox3.addStretch(1)

        hbox4.addStretch(1)
        hbox4.addWidget(self.pwd2)
        hbox4.addWidget(self.password2)
        hbox4.addStretch(1)

        hbox5.addStretch(1)
        hbox5.addWidget(self.confirm)
        hbox5.addWidget(self.cancel)
        hbox5.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)
        vbox.addStretch(5)
        
        self.setLayout(vbox)


class diary_UI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):
        ### Button ###
        # tab
        self.tabEdit = tabEdit()
        self.tabLoad = tabLoad()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tabEdit,'Edit')
        self.tabs.addTab(self.tabLoad,'Load')

        # setting
        self.setting = QPushButton("Font\nSetting", self)
        self.setting.setFixedHeight(60)

        # reset password
        self.resetPWD = QPushButton("Reset\nPassword", self)
        self.resetPWD.setFixedHeight(60)

        # logout
        self.logout = QPushButton("LOGOUT", self)
        self.logout.setFixedHeight(60)

        ### BoxLayout ###
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        vbox1.addWidget(self.tabs)

        vbox2.addStretch(1)
        vbox2.addWidget(self.setting)
        vbox2.addStretch(8)
        vbox2.addWidget(self.resetPWD)
        vbox2.addWidget(self.logout)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

class tabEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        def Font(text, s):
            font = text.font()
            font.setPointSize(s)
            return font

        ### Text ###
        date = QLabel("Date", self)
        date.setFont(Font(date, 12))

        weather = QLabel("Weather", self)
        weather.setFont(Font(weather, 12))

        title = QLabel("Title", self)
        title.setFont(Font(title, 12))

        ### Button ###
        # title
        self.titleEdit = QLineEdit()
        self.titleEdit.setFont(Font(self.titleEdit, 15))
        self.titleEdit.setFixedSize(700, 40)

        # date
        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setFont(Font(self.dateEdit, 12))
        self.dateEdit.setFixedSize(150, 40)

        # weather
        self.weatherEdit = QComboBox()
        self.weatherEdit.addItems('맑음 흐림 비 눈'.split())
        self.weatherEdit.setFixedSize(70, 40)

        # text
        self.textEdit = QTextEdit()
        self.textEdit.setFont(Font(self.textEdit, 13))
        
        # clear
        self.clear = QPushButton("Clear", self)
        self.clear.setFixedHeight(40)

        # save
        self.save = QPushButton("Save", self)
        self.save.setFixedHeight(40)

        ### Box Layout ###
        # hbox
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox1.addWidget(date)
        hbox1.addWidget(self.dateEdit)
        hbox1.addStretch(1)
        hbox1.addWidget(weather)
        hbox1.addWidget(self.weatherEdit)
        hbox1.addStretch(3)
        hbox1.addWidget(self.clear)
        
        hbox2.addWidget(title)
        hbox2.addWidget(self.titleEdit)
        hbox2.addStretch(1)
        hbox2.addWidget(self.save)

        hbox3.addWidget(self.textEdit)

        # vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)


class tabLoad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        def Font(text, s):
            font = text.font()
            font.setPointSize(s)
            return font

        ### Text ###
        date = QLabel("Date", self)
        date.setFont(Font(date, 12))

        weather = QLabel("Weather  ", self)
        weather.setFont(Font(weather, 12))

        title = QLabel("Title", self)
        title.setFont(Font(title, 12))

        ### Button ###
        # Title
        self.titleLoad = QTextBrowser()
        self.titleLoad.setFont(Font(self.titleLoad, 15))
        self.titleLoad.setFixedSize(700, 40)

        # Date
        self.dateLoad = QDateEdit()
        self.dateLoad.setDate(QDate.currentDate())
        self.dateLoad.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.dateLoad.setAlignment(Qt.AlignCenter)
        self.dateLoad.setFont(Font(self.dateLoad, 12))
        self.dateLoad.setFixedSize(150, 40)

        # Weather
        self.weatherLoad = QLabel("    ")
        self.weatherLoad.setFont(Font(self.weatherLoad, 15))
        self.weatherLoad.setFixedSize(70, 40)

        # Text
        self.textLoad = QTextBrowser()
        self.textLoad.setFont(Font(self.textLoad, 13))

        # delete
        self.delete = QPushButton("Delete", self)
        self.delete.setFixedHeight(40)

        # load
        self.load = QPushButton("Load", self)
        self.load.setFixedHeight(40)

        ### Box Layout ###
        # hbox
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox1.addWidget(date)
        hbox1.addWidget(self.dateLoad)
        hbox1.addStretch(1)
        hbox1.addWidget(weather)
        hbox1.addWidget(self.weatherLoad)
        hbox1.addStretch(3)
        hbox1.addWidget(self.delete)

        hbox2.addWidget(title)
        hbox2.addWidget(self.titleLoad)
        hbox2.addStretch(1)
        hbox2.addWidget(self.load)

        hbox3.addWidget(self.textLoad)

        # vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
# import main as ma
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,500)
        self.Login()
        self.background()
        self.back = QPushButton("<-Back",self)
        self.back.setStyleSheet("color: red;background-color: lightyellow;font-size: 20px")
        self.back.clicked.connect(self.back_click)
    
    def back_click(self):
        from main import main
        self.main = main()
        self.close()
        self.main.show()

    def Login(self):
        self.login = QLabel("Login pages!",self)
        self.login.setStyleSheet("color: black;font-size: 25px")
        self.login.move(260,0)
        self.not_found = QLabel("",self)
        self.not_found.move(200,50)
        self.not_found.setStyleSheet("font-size: 25px")

        self.login_word = QLabel("Login:",self)
        self.login_word.move(90,100)
        self.login_word.setStyleSheet('font-size: 25px')
        self.login_edit = QLineEdit(self)
        self.login_edit.setPlaceholderText("enter your login")
        self.login_edit.move(250,100)
        self.login_edit.setStyleSheet("font-size: 20px;width: 230px;")

        self.password_word = QLabel("Password:",self)
        self.password_word.move(90,200)
        self.password_word.setStyleSheet('font-size: 25px')
        self.password_edit = QLineEdit(self)
        self.password_edit.move(250,200)
        self.password_edit.setPlaceholderText("enter your password")
        self.password_edit.setStyleSheet("font-size: 20px;width: 230px;")
        
        self.submit = QPushButton("Submit",self)
        self.submit.setStyleSheet("font-size: 20px;width:300px;background-color:green")
        self.submit.move(170,280)
        self.submit.clicked.connect(self.submit_clic)
    def background(self):
        self.night = QRadioButton("Night Mode",self)
        self.night.move(90,350)
        self.night.setStyleSheet("color: blue;font-size: 25px")
        self.night.clicked.connect(self.back_cliced)
        self.light = QRadioButton("Light Mode",self)
        self.light.move(390,350)
        self.light.setStyleSheet("color: blue; font-size: 25px")
        self.light.clicked.connect(self.back_cliced)
    
    def back_cliced(self):
        if self.night.isChecked():
            self.setStyleSheet("background-color: black;")
            self.night.setStyleSheet("color: white;font-size: 25px")
            self.light.setStyleSheet("color: white;font-size: 25px")
            self.login.setStyleSheet("color: white;font-size:25px")
            self.login_word.setStyleSheet("color: white;font-size: 25px")
            self.password_word.setStyleSheet("color: white;font-size:25px")
        elif self.light.isChecked():
            self.setStyleSheet("background-color: white;")
            self.night.setStyleSheet("color: black;font-size: 25px")
            self.light.setStyleSheet("color: black;font-size: 25px")
            self.login.setStyleSheet("color: black;font-size:25px")
            self.login_word.setStyleSheet("color: black;font-size: 25px")
            self.password_word.setStyleSheet("color: black;font-size:25px")

    def submit_clic(self):
        control_count = 0
        with open("x_va_nol/loginlar.txt") as f:
            for i in f.read().split("\n"):
                if i.split(":")[0] == self.login_edit.text():
                    if i.split(":")[1] == self.password_edit.text():
                        pass
                else:
                    control_count += 0
            if control_count == 0:
                self.not_found.setText("Login or password wrong!")
                self.not_found.setStyleSheet("color: red;font-size: 25px")
                self.login_edit.clear()
                self.password_edit.clear()
                self.not_found.adjustSize()
            
# app = QApplication([])
# win = Login()
# win.show()
# app.exec_()
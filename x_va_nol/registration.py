from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
class Registration(QWidget):
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
        self.about = QPushButton("About",self)
        self.about.setStyleSheet("font-size: 15px;width: 10px")
        self.about.move(608,00)
        self.about.clicked.connect(self.remember)

        self.login = QLabel("Registration pages!",self)
        self.login.setStyleSheet("color: black;font-size: 25px")
        self.login.move(240,0)
        self.not_found = QLabel("",self)
        self.not_found.move(180,50)
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
            self.back.setStyleSheet("background-color: black;color: red;font-size: 25px")
            self.about.setStyleSheet("background-color: silver;color:yellow")
            self.login_edit.setStyleSheet("color: white")
        elif self.light.isChecked():
            self.setStyleSheet("background-color: white;")
            self.night.setStyleSheet("color: black;font-size: 25px")
            self.light.setStyleSheet("color: black;font-size: 25px")
            self.login.setStyleSheet("color: black;font-size:25px")
            self.login_word.setStyleSheet("color: black;font-size: 25px")
            self.password_word.setStyleSheet("color: black;font-size:25px")
            self.back.setStyleSheet("background-color: lightyellow;font-size: 25px;color: red")
            self.about.setStyleSheet("background-color: white;color: black")

    def remember(self):
        rem = QMessageBox()
        rem.setWindowTitle("Registration about!")
        rem.setStandardButtons(QMessageBox.Ok)
        rem.setIcon(QMessageBox.Warning)
        rem.setText("Passwords in there are 8 elements and one number, big letter, small letter and symbol must contain!")
        rem.setFixedSize(0,0)
        rem.exec_()
    def submit_clic(self):
        symbol = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','?',"\\",'|','`','~',';',',']
        truesymbol = ['@','$','^','&','_']
        number = str('1234567890')
        number_count = 0;symbol_count = 0; big_letter = 0; small_letter = 0;count = 0;name_count =0
        while True:
            for i in self.password_edit.text():
                if i in truesymbol:
                    symbol_count += 1
                elif i in symbol:
                    count += 1
                    break
                elif i.islower():
                    small_letter += 1
                elif i.isupper():
                    big_letter += 1
                elif i in number:
                    number_count += 1
            if count == 0:
                if len(self.password_edit.text()) >= 8 and number_count > 0 and symbol_count > 0 and small_letter > 0 and big_letter > 0:
                    with open("x_va_nol/loginlar.txt") as f:
                        f.seek(0)
                        for i in f.read().split("\n"):
                            if i.split(":")[0] == self.login_edit.text():
                                name_count += 1
                                count = 0
                                break
                else:
                    count += 1
            if name_count > 0:
                self.not_found.setText("Entered login is aviable!")
                self.not_found.setStyleSheet("color: red;font-size: 25px")
                self.login_edit.clear()
                self.password_edit.clear()
                self.not_found.adjustSize()
            
            if count > 0:
                self.not_found.setText("Entered password or login is invalid!")
                self.not_found.setStyleSheet("color: red;font-size: 25px")
                self.login_edit.clear()
                self.password_edit.clear()
                self.not_found.adjustSize()
                break
                
            
            # if control_count == 0:
            #     self.not_found.setText("Login or password is available!")
            #     self.not_found.setStyleSheet("color: red;font-size: 25px")
            #     self.login_edit.clear()
            #     self.password_edit.clear()
            #     self.not_found.adjustSize()
            
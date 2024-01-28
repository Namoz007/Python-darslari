from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
# from login import Login
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,500)
        self.choise()
        self.background()
        
    def choise(self):
        welcome = QLabel("Welcome to X and Zero game!",self)
        welcome.setStyleSheet("color: red;font-size: 22px")
        welcome.move(190,30)

        self.choise_Login = QPushButton("Login",self)
        self.choise_Login.setStyleSheet("background-color: green;font-size: 25px;width: 200px;color: blue")
        self.choise_Login.move(60,100)
        self.choise_Login.clicked.connect(self.login_clicked)

        self.choise_Registration = QPushButton("Registration",self)
        self.choise_Registration.setStyleSheet("background-color: green;color: red;font-size: 25px;width: 200px")
        self.choise_Registration.move(390,100)
        self.choise_Registration.clicked.connect(self.registration_clicked)
    
    def login_clicked(self):
            from login import Login
            self.login = Login()
            self.close()
            self.login.show()
    
    def registration_clicked(self):
        from registration import Registration
        self.registration = Registration()
        self.close()
        self.registration.show()

    def background(self):
        self.night = QRadioButton("Night Mode",self)
        self.night.move(60,250)
        self.night.setStyleSheet("color: blue;font-size: 25px")
        self.night.clicked.connect(self.back_cliced)
        self.light = QRadioButton("Light Mode",self)
        self.light.move(390,250)
        self.light.setStyleSheet("color: blue; font-size: 25px")
        self.light.clicked.connect(self.back_cliced)
    
    def back_cliced(self):
        if self.night.isChecked():
            self.setStyleSheet("background-color: black;")
            self.night.setStyleSheet("color: white;font-size: 25px")
            self.light.setStyleSheet("color: white;font-size: 25px")
        elif self.light.isChecked():
            self.setStyleSheet("background-color: white;")
            self.night.setStyleSheet("color: black;font-size: 25px")
            self.light.setStyleSheet("color: black;font-size: 25px")

app = QApplication([])
main_window = main()
main_window.setWindowTitle('X and Zero')
main_window.show()
app.exec_()
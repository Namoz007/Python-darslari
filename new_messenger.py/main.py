from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout,QLineEdit
from PyQt5.QtGui import QIcon
class enter_main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,600)
        self.Registration()
        self.setStyleSheet("background-color: white")

    def Registration(self):
        self.first_name_word = QLabel("First name",self)
        self.first_name_word.setStyleSheet("font-size: 20px")
        self.first_name_word.move(140,70)

        self.first_name = QLineEdit(self)
        self.first_name.setPlaceholderText("Firstname")
        self.first_name.setStyleSheet("font-size: 20px;height: 25px;width: 230px")
        self.first_name.move(50,100)

        self.first_name_danger = QLabel("",self)
        self.first_name_danger.setStyleSheet("font-size: 20px;color: red")
        self.first_name_danger.move(50,130)


        self.last_name_word = QLabel("Last name",self)
        self.last_name_word.setStyleSheet('font-size: 20px')
        self.last_name_word.move(470,70)

        self.last_name = QLineEdit(self)
        self.last_name.setPlaceholderText("Last name")
        self.last_name.setStyleSheet("font-size: 20px;height: 25px;width: 230px;")
        self.last_name.move(400,100)

        self.last_name_danger = QLabel("",self)
        self.last_name_danger.setStyleSheet("font-size: 20px;color: red")
        self.last_name_danger.move(400,130)


        self.day_word = QLabel('Day',self)
        self.day_word.setStyleSheet("font-size: 20px")
        self.day_word.move(110,200)

        self.day = QLineEdit(self)
        self.day.setPlaceholderText("Day")
        self.day.setStyleSheet("font-size: 20px;width: 80px;height: 25px")
        self.day.move(80,230)

        self.day_danger = QLabel("",self)
        self.day_danger.setStyleSheet("font-size: 20px;color: red")
        self.day_danger.move(80,260)


        self.month_word = QLabel("Month",self)
        self.month_word.setStyleSheet("font-size: 20px")
        self.month_word.move(320,200)

        self.month = QLineEdit(self)
        self.month.setPlaceholderText("Month")
        self.month.setStyleSheet("font-size: 20px;width: 80px;height: 25px")
        self.month.move(300,230)
        
        self.month_danger = QLabel("",self)
        self.month_danger.setStyleSheet("font-size: 20px;color: red")
        self.month_danger.move(300,260)


        self.year_word = QLabel("Year",self)
        self.year_word.setStyleSheet("font-size: 20px")
        self.year_word.move(550,200)

        self.year = QLineEdit(self)
        self.year.setPlaceholderText("Year")
        self.setStyleSheet("font-size: 20px;width: 80px;height: 25px")
        self.year.move(520,230)

        self.year_danger = QLabel("",self)
        self.year_danger.setStyleSheet("font-size: 20px;color: red")
        self.year_danger.move(520,260)


        self.nickname_word = QLabel("Nick name",self)
        self.nickname_word.setStyleSheet("font-size: 20px;")
        self.nickname_word.move(130,330)

        self.nickname = QLineEdit(self)
        self.nickname.setPlaceholderText("Nickname")
        self.nickname.setStyleSheet("font-size: 20px;width: 230px;height: 25px")
        self.nickname.move(50,360)

        self.nickname_danger = QLabel("",self)
        self.nickname_danger.setStyleSheet("font-size: 20px;color: red")
        self.nickname_danger.move(50,390)


        self.number_word = QLabel("Number",self)
        self.number_word.setStyleSheet("font-size: 20px;")
        self.number_word.move(480,330)

        self.number = QLineEdit(self)
        self.number.setPlaceholderText("telephone number")
        self.number.setStyleSheet("font-size: 20px;width: 230px;height: 25px")
        self.number.move(400,360)

        self.number_danger = QLabel("",self)
        self.number_danger.setStyleSheet("font-size: 20px;color: red")
        self.number_danger.move(400,390)


        self.submit = QPushButton("Submit",self)
        self.submit.setStyleSheet('font-size: 25px;width: 250px;background-color: lightblue')
        self.submit.clicked.connect(self.submit_click)
        self.submit.move(210,440)

    def submit_click(self):
        self.number = str('1234567890')
        self.sign = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','?',"\\",'|','`','~',';',',']
        self.t_sign = ['@','$','^','&','_']

        word_count = 0
        for i in self.first_name.text():
            if i in self.number:
                word_count += 1
            elif i in self.sign:
                word_count += 1
        if word_count > 0:
            self.first_name.clear()
            self.first_name_danger.setText("Name is unqualified!")
            self.first_name_danger.adjustSize()
        else:
            self.first_name_danger.setText(" ")
            self.first_name_danger.adjustSize()


        last_count = 0
        for i in self.last_name.text():
            if i in self.number:
                last_count += 1
            elif i in self.sign:
                last_count += 1
        if last_count > 0:
            self.last_name_danger.setText("Last name is unqualified!")
            self.last_name_danger.adjustSize()
            self.last_name.clear()
        else:
            self.last_name_danger.setText(" ")
            self.last_name_danger.adjustSize()
        

        day_count = 0
        if self.day.text() > "31":
            day_count += 1
        if day_count > 0:
            self.day_danger.setText("Day is not correct!")
            self.day_danger.adjustSize()
            self.day.clear()
        else:
            self.day_danger.setText(' ')
            self.day_danger.adjustSize()


        month_count = 0
        if self.month.text() > "12" or self.month.text() < '0':
            month_count += 1
        elif self.month.text() == ' ':
            month_count += 1
        if month_count > 0:
            self.month_danger.setText("Month is not correct!")
            self.month_danger.adjustSize()
            self.month.clear()
        else:
            self.month_danger.setText(' ')
            self.month_danger.adjustSize()


        year_count = 0
        if self.year.text() > "2016" or self.year.text() < "1960":
            year_count += 1
        if year_count > 0:
            self.year_danger.setText("Year is not correct!")
            self.year_danger.adjustSize()
            self.year.clear()
        else:
            self.year_danger.setText(' ')
            self.year_danger.adjustSize()




app = QApplication([])
main_window = enter_main()
main_window.setWindowTitle("NEW MESSENGER")
main_window.setWindowIcon(QIcon("C:\\Users\\user\\desktop\\telegram.png"))
main_window.show()
app.exec_()
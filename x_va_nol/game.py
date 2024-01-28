from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
import random as rand
class game(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,500)
        self.background()
        self.c1 = 0;self.c2 = 0;self.c3 = 0;self.c4 = 0;self.c5 = 0;self.c6 = 0;self.c7 = 0;self.c8 = 0;self.c9 = 0;
        self.welcome = QLabel("X and Zero",self)
        self.welcome.setStyleSheet('font-size: 25px;color: green')
        self.welcome.move(270,0)
        self.game_main()
        
        self.danger = QLabel('',self)
        self.danger.setStyleSheet("font-size: 22px;color: red")
        self.danger.move(250,50)

    def game_main(self):
        self.game_layout = QHBoxLayout()

        self.one = QPushButton("",self)
        self.one.setStyleSheet("background-color: silver")
        self.one.setFixedSize(90,70)
        self.one.move(150,90)

        self.two = QPushButton("",self)
        self.two.setStyleSheet("background-color: silver")
        self.two.setFixedSize(90,70)
        self.two.move(290,90)

        self.three = QPushButton("",self)
        self.three.setStyleSheet("background-color: silver")
        self.three.setFixedSize(90,70)
        self.three.move(430,90)

        self.four = QPushButton("",self)
        self.four.setStyleSheet("background-color: silver")
        self.four.setFixedSize(90,70)
        self.four.move(150,210)

        self.five = QPushButton("",self)
        self.five.setStyleSheet("background-color: silver")
        self.five.setFixedSize(90,70)
        self.five.move(290,210)

        self.six = QPushButton("",self)
        self.six.setStyleSheet("background-color: silver")
        self.six.setFixedSize(90,70)
        self.six.move(430,210)

        self.seven = QPushButton("",self)
        self.seven.setStyleSheet("background-color: silver")
        self.seven.setFixedSize(90,70)
        self.seven.move(150,330)

        self.eight = QPushButton("",self)
        self.eight.setStyleSheet("background-color: silver")
        self.eight.setFixedSize(90,70)
        self.eight.move(290,330)

        self.nine = QPushButton("",self)
        self.nine.setStyleSheet("background-color: silver")
        self.nine.setFixedSize(90,70)
        self.nine.move(430,330)
    
    def agent(self):
        self.lst = ['one','two','three','four','five','six','seven','eight','nine']
        self.agent_choise = rand.choices(self.lst) 

    def btn_one(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!")   

    def btn_two(self):
        if self.c2 == 0:
            self.two.setText("O")
            self.lst.remove('two')
            self.c2 += 1
        else:
            self.danger.setText("You can not paste!") 

    
    def btn_three(self):
        if self.c3 == 0:
            self.three.setText("o")
            self.lst.remove('three')
            self.c3 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_four(self):
        if self.c4 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_five(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_six(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_seven(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_eight(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def btn_nine(self):
        if self.c1 == 0:
            self.one.setText("o")
            self.lst.remove('one')
            self.c1 += 1
        else:
            self.danger.setText("You can not paste!") 

    def background(self):
        self.night = QRadioButton("Night mode",self)
        self.night.setStyleSheet("font-size: 25px;color: blue")
        self.night.move(10,420)
        self.night.clicked.connect(self.back_click)

        self.light = QRadioButton("Light mode",self)
        self.light.setStyleSheet("font-size: 25px;color: blue")
        self.light.move(10,460)
    
    def back_click(self):
        if self.night.isChecked():
            pass
        elif self.light.isChecked():
            pass


app = QApplication([])
win = game()
win.setWindowTitle("X and Zero")
win.show()
app.exec_()
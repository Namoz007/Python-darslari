import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
# class Time:
#     def __init__(self,hours,minut,secund) -> None:
#         self.hours = hours
#         self.minut = minut
#         self.secund = secund
    
#     def get24hourse(self):
#         hours24 = 24 * 60
#         hours = (self.hours * 60) + self.minut
#         count = hours24 - hours
#         if self.secund == 60:
#             self.secund = 0
#             count -= 1
#         print(f"Soat 24:00 gacha {count // 60} soat {count % 60} minut {self.secund} sekund qoldi.")
    
#     def getHundredHours(self):
#         self.minut += 100
#         if self.minut > 120:
#             self.hours += 2
#             self.minut -= 120
#         elif self.minut > 60:
#             self.hours += 1
#             self.minut -= 60

# lst = []
# x = int(input("Nechta obeykt kiritmoqchisiz: "))
# for i in range(x):
#     lst.append( Time(int(input("Enter hour: ")),int(input("Enter minut: ")),int(input("Enter secund: "))))

# while True:
#     print("""
# 1.Qancha vaqt qolganini bilish     2.100 daqiqa qo'shish
# """)
#     a = int(input(">>>> "))

#     if a == 1:
#         for i in range(x):
#             lst[i].get24hourse()
#             print(" ")
#     elif a == 2:
#         for i in range(x):
#             lst[i].getHundredHours()
#             print("100 daqiqa qo'shildi")
#     else:
#         print("rahmat")



# class worker:
#     def __init__(self,surname,position,salary) -> None:
#         self.surname = surname
#         self.position = position
#         self.salary = salary
    
#     def __str__(self) -> str:
#         print(f"""
# Surname: {self.surname}
# Position: {self.position}
# Salary: {self.salary}
# """)

# lst = []
# x = int(input("Nechta obeykt kiritmoqchisiz: "))
# for i in range(x):
#     lst.append(worker(input("Enter surname: "),input("Enter your position: "),int(input("Enter your salary: "))))

# while True:
#     print("""1.Oylikni 15 foiz oshirish.     2.Ismni tekshirish.""")
#     a = int(input(">>>> "))
#     if a == 1:
#         for i in lst:
#             i.salary += i.salary * 0.15 
#             print(i.salary)
#     elif a == 2:
#         for i in lst:
#             if i.surname == 'Abdulla':
#                 i.position += 'injiner'
#                 print(f"Sizning lavozimingiz {i.position}")
#     else:
#         print("The end")




# class word(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(200,150)
#         self.edit = QLineEdit(self)
#         self.edit.move(30,20)
#         self.btn = QPushButton("Parse",self)
#         self.btn.move(30,50)
#         self.btn.setStyleSheet("font-size: 15px;width: 130px")
#         self.btn.clicked.connect(self.clicked)
#         self.word = QLabel("",self)
#         self.word.move(30,90)
    
#     def clicked(self):
#         x = self.edit.text()
#         self.word.setText(f"{x[::-1]}")
#         self.word.adjustSize()
        

# app = QApplication([])
# win = word()
# win.show()
# app.exec_()




# class word(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(200,150)
#         self.edit = QLineEdit(self)
#         self.edit.move(30,20)
#         self.word_count = QLineEdit(self)
#         self.word_count.move(30,50)
#         self.btn = QPushButton("Parse",self)
#         self.btn.move(30,80)
#         self.btn.setStyleSheet("font-size: 15px;width: 130px")
#         self.btn.clicked.connect(self.clicked)
#         self.word = QLabel("",self)
#         self.word.move(30,120)
    
#     def clicked(self):
#         x = self.edit.text().count(self.word_count.text())
#         self.word.setText(f"{self.word_count.text()} - {x}")
#         self.word.adjustSize()
        

# app = QApplication([])
# win = word()
# win.show()
# app.exec_()


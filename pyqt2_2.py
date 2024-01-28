from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox

class display(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,500)
        self.setStyleSheet("background-color:lightgreen")
        self.
    
    def choise(self):
        enter = QLabel("Bootcamp Result",self)

app = QApplication([])
disp = display()

disp.show()
app.exec_()
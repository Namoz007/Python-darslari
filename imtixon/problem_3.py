from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QCheckBox, QRadioButton
class math(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,250)

        self.input_word = QLabel("Input: ",self)
        self.input_word.setStyleSheet("font-size: 20px")
        self.input_word.move(50,30)
        
        self.input_edit = QLineEdit(self)
        self.input_edit.setStyleSheet('font-size: 15px')
        self.input_edit.move(120,30)

        self.btn = QPushButton("Submit",self)
        self.btn.setStyleSheet("background-color: lightgreen")
        self.btn.setFixedSize(175,30)
        self.btn.move(118,60)
        self.btn.clicked.connect(self.click)

        self.output_word = QLabel("",self)
        self.output_word.setStyleSheet("font-size: 20px")
        self.output_word.move(50,120)

    def click(self):
        plus = 0
        minus = 0
        kopaytiruv = 0
        boluv = 0
        foiz = 0
        qous1 = 0
        qous2 = 0
        for i in self.input_edit.text():
            if i == '+':
                plus += 1
            elif i == '-':
                minus += 1
            elif i == '*':
                kopaytiruv += 1
            elif i == '/':
                boluv += 1
            elif i == '%':
                foiz += 1
            elif i == '(':
                qous1 += 1
            elif i == ')':
                qous2 += 1
        
        self.output_word.setText(f"Output: + amali {plus} ta, - amali {minus} ta,\n * amali {kopaytiruv} ta, / amali {boluv} ta,\n % amali {foiz} ta, () amali {qous1} ta")
        self.output_word.adjustSize()

app = QApplication([])
win = math()
win.setWindowTitle("Amallarni hisoblagich")
win.show()
app.exec_()
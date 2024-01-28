from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QMainWindow
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import sys
class start_main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,600)
        self.setStyleSheet("background-color: white")
        self.start()
        # self.photo = QPixmap("C:\\Users\\user\\desktop\\telegram.png")

    def start(self):
        self.telegram_photo = QLabel(self)
        self.telegram_img = QPixmap("C:\\Users\\user\\desktop\\telegramm.png")
        self.telegram_photo.setPixmap(self.telegram_img)
        self.telegram_photo.move(210,100)

        self.start_messaging = QPushButton("START MESSAGING",self)
        self.start_messaging.clicked.connect(self.start_click)
        self.start_messaging.setStyleSheet("font-size: 25px;background-color: lightblue;")
        self.start_messaging.move(230,350)

    def start_click(self):
        from main import enter_main
        self.new_win = enter_main()
        self.close()
        self.new_win.show()

app = QApplication([])
window = start_main()
window.setWindowTitle("NEW MESSENGER")
window.setWindowIcon(QIcon("C:\\Users\\user\\desktop\\telegram.png"))
window.show()
app.exec_()
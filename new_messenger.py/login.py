from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QMainWindow
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.acceptDrops()

		# set window title
		self.setWindowTitle("Load Image on Window")

		# set window size
		self.setGeometry(0, 0, 500, 500)

		# Create an instance of label
		self.label = QLabel(self)
		
		# Load image
		self.pixmap = QPixmap('C:\\Users\\user\\desktop\\telegramm.png')

		# Set image to label
		self.label.setPixmap(self.pixmap)
		# self.label.setFixedHeight(550)
		# self.label.setFixedWidth(550)

        # Resize the label according to image size
		self.label.resize(self.pixmap.width(),
						self.pixmap.height())

		# show the widgets
		self.show()

# Instantiate pyqt5 application
App = QApplication([])

# create window instance
window = Window()

# start the app
App.exit(App.exec())

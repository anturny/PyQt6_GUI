import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon # For Icon

class Window(QWidget):
    def __init__(self): 

        super().__init__() 

        self.setWindowTitle("PyQt6 Course")

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png")) # Change window icon

        self.setGeometry(200, 200, 500, 400) # Set window dimensions

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMenu, QPushButton # Import
from PyQt6.QtGui import QIcon, QFont # For Icon and font 
from PyQt6.QtCore import QSize

class Window(QWidget):
    def __init__(self): 

        super().__init__() 

        self.setWindowTitle("QPushButton")

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png")) # Change window icon

        self.setGeometry(200, 200, 500, 400) # Set window dimensions

        btn = QPushButton("Click", self) # Give text of push button, must use self for it to appear
        btn.setGeometry(100, 100, 130, 130) # Change geometry
        btn.setFont(QFont("Times", 14)) # Change font and font size
        btn.setIcon(QIcon("/media/windowsMedia/qt.png")) # Set icon
        btn.setIconSize(QSize(36,36)) # Adjust Icon Size

        # Popup Menu
        menu = QMenu() # Define menu
        menu.setFont(QFont("Times", 14)) # Set Menu Font
        menu.setStyleSheet('background-color:yellow') # Change menu color
        menu.addAction("Copy")
        menu.addAction("Cut") 
        menu.addAction("Paste") # Add elements of menu

        btn.setMenu(menu) # Align popup menu with button

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
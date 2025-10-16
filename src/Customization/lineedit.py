import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont # For Icon

class Window(QWidget):
    def __init__(self): 

        super().__init__() 

        self.setWindowTitle("PyQt6 Course")

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png")) # Change window icon

        self.setGeometry(200, 200, 500, 400) # Set window dimensions

        line_edit = QLineEdit(self) # We can write something in line edit inside
        line_edit.setFont(QFont("Sanserif", 15)) # Change font and size
        #line_edit.setText("Default Text") # Fill in text space
        line_edit.setPlaceholderText("Please enter your username: ") # Set placeholder text
        #line_edit.setEnabled(False) # This will disable the text from being written in
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
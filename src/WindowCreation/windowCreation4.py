import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon # For Icon

class Window(QWidget):
    def __init__(self): 
        '''_init__ is a reserved method in Python classes called a 
        constructor in object-orientated programming. This method is called when
        an object is created from a class and it allows the the class to initialize
        the tributes of that class.'''

        super().__init__() 
        '''super() is used to give access to methods and properties of the parent
        class. It also makes class inheritance more manageable.'''

        self.setWindowTitle("PyQt6 Course")
        '''(self) is used to represent the instance of the class and access the tributes
        of that class by calling to self.'''

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png")) # Change window icon

        self.setGeometry(200, 200, 500, 400) # Set window dimensions

        self.setStyleSheet('background-color:red') # Change background window color

        self.setWindowOpacity(0.7) # Sets the window's opacity

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
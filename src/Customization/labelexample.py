import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie # For Icon

class Window(QWidget):
    def __init__(self): 

        super().__init__() 

        self.setWindowTitle("Label Example")

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png")) # Change window icon

        self.setGeometry(200, 200, 500, 400) # Set window dimensions

        '''
        label = QLabel("Welcome to PyQt6 Course", self) # First text in window 
        #label.setText("The text in here") # This will override previous text
        label.move(100, 100) # Moves label position (x,y)
        label.setFont(QFont("Times", 15)) # Change font
        label.setStyleSheet('color:red') # Change color
        '''

        '''
        # Adding image to the label
        label = QLabel(self) # Define label
        pixmap = QPixmap("media/windowsMedia/qt.png") # Find image
        label.setPixmap(pixmap) # Display image on pixmap
        '''

        #Adding gif image to the label
        label = QLabel(self)
        movie = QMovie("media/windowsMedia/cat.gif") # import gif
        movie.setSpeed(500) # This is in percent speed
        label.setMovie(movie) # port movie to label
        movie.start() # Start movie 

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
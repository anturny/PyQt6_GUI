import sys

from PyQt6.QtWidgets import QApplication, QWidget 


app = QApplication(sys.argv) #Create object of QApplication, add (sys.argv) if using Command Line Utility

window = QWidget()

window.show() #Shows window

sys.exit(app.exec()) #Place to enter main loop of application
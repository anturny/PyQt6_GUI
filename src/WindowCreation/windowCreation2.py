import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow() #Create main window, we can use more tools with QMainWindow
window.statusBar().showMessage("Welcome to PyQt6 Course") #Show status bar in window, will NOT work with QWidget
window.menuBar().addMenu("File") #Creates file dropdown in menu

window.show()

sys.exit(app.exec()) #Showcase window
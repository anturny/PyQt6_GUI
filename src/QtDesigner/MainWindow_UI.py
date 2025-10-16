from PyQt6.QtWidgets import QApplication, QWidget
from QtDesigner.Window_UI import Ui_Form # This is from the Window_UI.py file, we take classes from that file into THIS document.
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__() # Initializing

        self.ui = Ui_Form() # Define
        self.ui.setupUi(self) # Sets up file

        self.setWindowTitle("New one") # Change window title to New one

app = QApplication(sys.argv) # Create application
window = Window() # Create window
window.show() # Shows window
sys.exit(app.exec()) # Creates loop
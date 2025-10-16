from PyQt6.QtWidgets import QApplication, QWidget
import sys
import os
from PyQt6 import uic # Import uic module

class UI(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "Window.ui") # Find file
        uic.loadUi(ui_path, self) # Transforms .ui files into .py files

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
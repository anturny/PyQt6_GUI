import sys

from PyQt6.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)

window = QDialog() # Creates dialog window

window.show()

sys.exit(app.exec())
# Credit
Note that this entire tutorial is thanks to Parwiz Forogh's YouTube Tutorial at [PyQt6 - The Ultimate GUI Toolkit for Python Developers in 2023](https://youtu.be/_16NK5LZPes?si=4e_72eY-PwwBHf30).

# Step-by-step Rundown
The first step to building this Python-based GUI is to install the toolkit inside the terminal after activating the virtual environment.
```
pip install PyQt6
```

When we import PyQt6, everything is inside modules and modules are divided into different classes. QtWidgets is a class that provide UI elements to help create classic desktop style user interfaces. There are about 138 different related classes. The QApplication class manage the GUI application control flow and main settings. It helps specialize the GUI with some functionality needed for QWidget based applications. The QWidget helps us create the window.
```
from PyQt6.QtWidgets import QApplication, QWidget 
```

This is where we enter the main loop of the application and the event handling begins from this point. The main loop receives events from the window system and dispatches them to the application. The main loop ends if we call exit method and the main widget is destroyed.
```
sys.exit(app.exec())
```

This is the end of how to create a window.
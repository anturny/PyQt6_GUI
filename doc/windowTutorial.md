# Windows Guide
The first step to building this Python-based GUI is to install the toolkit inside the terminal after activating the virtual environment.
```
pip install PyQt6
```
This is the beginning of how to create a window in the [windowCreation.py](/src/windowCreation.py) file.

When we import PyQt6, everything is inside modules and modules are divided into different classes. QtWidgets is a class that provide UI elements to help create classic desktop style user interfaces. There are about 138 different related classes. The QApplication class manage the GUI application control flow and main settings. It helps specialize the GUI with some functionality needed for QWidget based applications. The QWidget helps us create the window.
```
from PyQt6.QtWidgets import QApplication, QWidget 
```

This is where we enter the main loop of the application and the event handling begins from this point. The main loop receives events from the window system and dispatches them to the application. The main loop ends if we call exit method and the main widget is destroyed.
```
sys.exit(app.exec())
```

This is the end of the file.

## Window Class Types
- QMainWindow: This window class provides a main application window. A main window provides a framework for building an application's user interface. PyQt has QMainWindow and its related classes for main window management. It also has its own layout to which you can add QToolBars, QDockWidgets, QMenuBar, and QStatusBar.

- QDialog: The QDialog class is the base class of dialog window. A dialog window is a top-level window mostly used for short-term tasks and brief communications with the user. QDialogs may be modal or modeless.

- QWidget: The QWidget class is the base class of all user interface objects. The widget is the important point of the user interface as it receives mouse, keyboard, and other events from the window system and paints a representation of itself on the screen. 

This is the beginning of how to create a window in the [windowCreation2.py](/src/windowCreation2.py) file.

This file primarily demonstrates the difference between QMainWindow and QWidget with the following two classes.
```
indow.statusBar().showMessage("Welcome to PyQt6 Course")
window.menuBar().addMenu("File")
```

This is the end of the file.


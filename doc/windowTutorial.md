# Windows Guide
The first step to building this Python-based GUI is to install the toolkit inside the terminal after activating the virtual environment.
```
pip install PyQt6
```
## First Window with QWidget
This is the beginning of how to create a window in the [windowCreation.py](/src/windowCreation.py) file.

When we import PyQt6, everything is inside modules and modules are divided into different classes. QtWidgets is a class that provide UI elements to help create classic desktop style user interfaces. There are about 138 different related classes. The QApplication class manage the GUI application control flow and main settings. It helps specialize the GUI with some functionality needed for QWidget based applications. The QWidget helps us create the window.
```
from PyQt6.QtWidgets import QApplication, QWidget 
```

This is where we enter the main loop of the application and the event handling begins from this point. The main loop receives events from the window system and dispatches them to the application. The main loop ends if we call exit method and the main widget is destroyed.
```
sys.exit(app.exec())
```

## Window Class Types
- QMainWindow: This window class provides a main application window. A main window provides a framework for building an application's user interface. PyQt has QMainWindow and its related classes for main window management. It also has its own layout to which you can add QToolBars, QDockWidgets, QMenuBar, and QStatusBar.

- QDialog: The QDialog class is the base class of dialog window. A dialog window is a top-level window mostly used for short-term tasks and brief communications with the user. QDialogs may be modal or modeless.

- QWidget: The QWidget class is the base class of all user interface objects. The widget is the important point of the user interface as it receives mouse, keyboard, and other events from the window system and paints a representation of itself on the screen. 

## QMainWindow vs QWidget
This is the beginning of how to create a window in the [windowCreation2.py](/src/windowCreation2.py) file.

This file primarily demonstrates the difference between QMainWindow and QWidget with the following two classes.
```
window.statusBar().showMessage("Welcome to PyQt6 Course")
window.menuBar().addMenu("File")
```

## QDialog
This is the beginning of how to create a window in the [windowCreation3.py](/src/windowCreation3.py) file.

This tutorial only creates a dialog window which are primarily used for short-term tasks and brief communications with the user.
```
window = QDialog()
```

## Classes and Calling to Self
This is the beginning of how to create a window in the [windowCreation4.py](/src/windowCreation4.py) file.

Class extends from QWidget. When inheriting from a class, we are able to access all attributes of that class. Now the Window class can access all attributes of the QWidget class.

We utilize _init__ is a reserved method in Python classes called a constructor in object-orientated programming. This method is called when an object is created from a class and it allows the the class to initialize the tributes of that class.

super() is used to give access to methods and properties of the parent class, and it also makes class inheritance more manageable.

It is also important to note that the picture used to demonstrate the icon can be found in the media/windowsMedia/qt.png pathway.

![alt text](qt.png)

In this file, we play with many customization options as shown in the code below.
```
class Window(QWidget):
    def __init__(self): 
        super().__init__()

        self.setWindowTitle("PyQt6 Course")

        self.setWindowIcon(QIcon("media/windowsMedia/qt.png"))

        self.setGeometry(200, 200, 500, 400)

        self.setStyleSheet('background-color:red')

        self.setWindowOpacity(0.7)
```
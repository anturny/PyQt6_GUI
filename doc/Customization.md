For this section, we will copy a template we can use across the board. In order to do this, we will always need a file for widgets in the [wind.py](/src/Customization/wind.py) file.

We will copy the contents of the [windowCreation4.py](/src/WindowCreation/windowCreation4.py) into the wind.py file and delete the stylesheet and window opacity lines.

# QPushButton

We will copy the contents of wind.py into the [btnexample.py](/src/Customization/btnexample.py) file.

In this file, we learn about importing QMenu and QPushButton from QtWidget, QSize from QtCore, and QFont from QtGui.

- QMenu: Class used to create menu widgets
- QPushButton: Clickable widget to trigger actions in UI
- QSize: Class that changes size of window
- QFont: Class that changes font type and size

We customize the push button and drop down menu by manipulating its size, color, and font.

```
btn = QPushButton("Click", self) # Give text of push button, must use self for it to appear
btn.setGeometry(100, 100, 130, 130) # Change geometry
btn.setFont(QFont("Times", 14)) # Change font and font size
btn.setIcon(QIcon("/media/windowsMedia/qt.png")) # Set icon
btn.setIconSize(QSize(36,36)) # Adjust Icon Size

# Popup Menu
menu = QMenu() # Define menu
menu.setFont(QFont("Times", 14)) # Set Menu Font
menu.setStyleSheet('background-color:yellow') # Change menu color
menu.addAction("Copy")
menu.addAction("Cut") 
menu.addAction("Paste") # Add elements of menu

btn.setMenu(menu) # Align popup menu with button
```

# QLabel

QLabel widget provides text, gifs, or widget display. The user interaction functionality is provided. This is showcased in the [labelexample.py](/src/Customization/labelexample.py) file.

We will need QLabel from QtWidgets, QPixmap and QMovie from QtGui. 

- QLabel: Class for text and image display
```
label = QLabel("Welcome to PyQt6 Course", self) # First text in window 
label.setText("The text in here") # This will override previous text
label.move(100, 100) # Moves label position (x,y)
label.setFont(QFont("Times", 15)) # Change font
label.setStyleSheet('color:red') # Change color
```

- QPixmap: Class of off-screen image representation that can be used as a paint device
```
label = QLabel(self) # Define label
pixmap = QPixmap("media/windowsMedia/qt.png") # Find image
label.setPixmap(pixmap) # Display image on pixmap
```

- QMovie: Convenience class for playing movies with QImageReader
```
label = QLabel(self)
movie = QMovie("media/windowsMedia/cat.gif") # import gif
movie.setSpeed(500) # This is in percent speed
label.setMovie(movie) # port movie to label
movie.start() # Start movie 
```

The file showcases how we can use QLabel to setup labels inside a window and modify the text, position, font, and color.

When we add an image to the label, we can call to the file in the directory and use a Pixmap in order to display.

When we want to play a video or gif, we will use QMovie by defining the label first, porting the movie, setting the speed at the percent we want it playing at, then begin the movie.

In this instance, we utilize a cat gif:

![alt text](/media/windowsMedia/cat.gif)

# QLineEdit

QLineEdit is a class in QtWidgets that helps as a one line text editor. A line edit allows the user to enter and edit a single line of plain text with a useful collection of editing functions including: undo, redo, cut, paste, drag and drop.

We first define line_edit and then import QFont to adjust the font and size. We can fill in the typable text space with .setText, but it would be better to use .setPlaceholdertext as this will disappear when the user begins typing. The .setEnabled(False) will prevent the user from typing inside, most likely useful when we need to fill out forms. If we need to set passwords, we may use .setEchoMode(QLineEdit.EchoMode.Password) in order to do so.

```
line_edit = QLineEdit(self)
line_edit.setFont(QFont("Sanserif", 15))
line_edit.setText("Default Text")
line_edit.setPlaceholderText("Please enter your username: ")
line_edit.setEnabled(False)
line_edit.setEchoMode(QLineEdit.EchoMode.Password)
```

# QHBoxLayout

QHBoxLayout is related to the QtWidgets 
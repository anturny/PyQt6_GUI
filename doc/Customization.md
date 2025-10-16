# QPushButton

We will always need a file for widgets in the [wind.py](/src/Customization/wind.py) file.

We will copy the contents of the [windowCreation4.py](/src/WindowCreation/windowCreation4.py) into the wind.py file and delete the stylesheet and window opacity lines. We will then copy the contents into the [btnexample.py](/src/Customization/btnexample.py) file.

In this file, we learn about importing QMenu and QPushButton from QtWidget, QSize from QtCore, and QFont from QtGui.

QMenu: Class used to create menu widgets
QPushButton: Clickable widget to trigger actions in UI
QSize: Class that changes size of window
QFont: Class that changes font type and size

We customize the push button and drop down menu by manipulating its size, color, and font.

# QLabel

QLabel widget provides text, gifs, or widget display. The user interaction functionality is provided. This is showcased in the [labelexample.py](/src/Customization/labelexample.py) file.

We will need QLabel from QtWidgets, QPixmap and QMovie from QtGui. 

QLabel: Class for text and image display
QPixmap: Class of off-screen image representation that can be used as a paint device
QMovie: Convenience class for playing movies with QImageReader

The file showcases how we can use QLabel to setup labels inside a window and modify the text, position, font, and color.

When we add an image to the label, we can call to the file in the directory and use a Pixmap in order to display.

When we want to play a video or gif, we will use QMovie by defining the label first, porting the movie, setting the speed at the percent we want it playing at, then begin the movie.

In this instance, we utilize a cat gif:

![alt text](/media/windowsMedia/cat.gif)


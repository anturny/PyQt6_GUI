# QTDesigner

It should be noted before ANYTHING else that QTDesigner is the tool for designing and building graphical user interfaces or GUIs with QT Widgets. You can customize your windows or dialogues in a "what you see is what you get" manner. We can test them with different styles and resolutions. 

In the terminal, we will need to install PyQt6 tools in order to access QT Designer as the base pip does not come with it. However, the main problem is that the terminal command only accepts Python 3.9.0, not 3.12.0 that we were previously working with. Please install Python 3.9.0 and restart your virtual environment if you haven't already done so.

Upon setting up your new Python 3.9.0 environment, your pip installations should be wiped. The requirements.txt file should now be reflecting the new pip updates with the tools so please reinstall PyQt6 with either of the options below in the terminal.

```
pip install -r requirements.txt
```
or
```
pip install pyqt6-tools
```

It should also additionally be noted that you should NOT attempt to execute the following command as it will make the tools and PyQt6 incompatible.
```
pip install PyQt6 --upgrade
```

If you accidentally ran that command, please use the following command in the terminal, type in "Y", hit enter, and then execute either of the installations as told above.
```
pip uninstall PyQt6
```

If you're the lucky soul who made it this far with all your code working, navigate to the pathway PyQt6_GUI/.venv/Lib \site-packages/qt6_appplications/Qt/bin/designer.exe, right click and open it insider File Explorer.

At this point, please follow the tutorial in the [YouTube demonstration](https://youtu.be/_16NK5LZPes?si=asA0FvDcwoGcX1ce&t=1565) as it is difficult to demonstrate a completely different application within the scope of VSCode. I created a Window.UI file within the src folder in order to follow the tutorial.

The next step is to use the terminal again in the following format.
```
pyuic6 -x "path folder/.ui file name" -o "path folder/new .py file name"
```

I input as the following.
```
pyuic6 -x src/Window.ui -o src/Window_UI.py
```

This is in order to translate our main design into our coding logic, which is actually ineffective. It should run your design when you press "Run". 

In order to port it easier, you can also do the following.
```
pyuic6 "UI file name" > "new PY file name"
```
For example:
```
pyuic6 Window.ui > Window_UI.py
```
When you run this, there is no QApplication and the loop. It will not run. We can load it into another file in order to separate the main code from the logic code. 
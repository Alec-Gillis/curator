from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QValidator
from PyQt5.QtGui import QTextFrame
import typing
from pynput import keyboard
import sys
import os
import json
import webbrowser
from json.decoder import JSONDecodeError

class SongActions:

    def __init__(self):
        pass

    #play/queue/skip?
    def do_action(self):
        pass

    def get_song(self):
        pass

    def play_song(self):
        pass

    def queue_song(self):
        pass

    def skip_song(self):
        pass


# Validate the string being passed into the spotify player
class Validator(QValidator):
    def __init__(self):
        super(Validator, self).__init__()

    def validate(self, a0: str, a1: int) -> typing.Tuple['QValidator.State', str, int]:
        pass


# Define the display window for the application
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 300, 400, 300)
        self.setWindowTitle("spotify-util")
        self.initUI()

    def initUI(self) -> None:
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

        self.text = QtWidgets.QLineEdit(self)
        self.text.move(10, 10)
        self.text.setFixedWidth(300)
        self.text.setMaxLength(25)
        self.text
    #       self.enterEvent()

    def clicked(self) -> None:
        self.label.setText("You pressed the bbbbbbbbb")
        self.update()

    def update(self) -> None:
        self.label.adjustSize()


#Create the application
def window() -> None:
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec_())


window()

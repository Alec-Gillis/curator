from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle("spotify-util")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the bbbbbbbbb")
        self.update()

    def update(self) -> None:
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Window()


    win.show()
    sys.exit(app.exec_())

window()

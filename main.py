import sys
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
from UI import Ui_Form
# from mainUi import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.qp = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окружности весьма жёлтые!')

        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def drawC(self):
        pen = QPen()
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        pen.setColor(QtGui.QColor().fromRgb(r, g, b))
        pen.setWidth(10)
        self.qp.setPen(pen)

        d = random.randint(1, 100)
        x = random.randint(1, 400)
        y = random.randint(1, 400)
        print(d, x, y)

        self.qp.drawEllipse(x, y, d, d)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.flag:
            self.qp = QPainter(self)
            for _ in range(5):
                self.drawC()
            self.qp.end()

        # self.painter.setPen(QPen(Qt.yellow))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

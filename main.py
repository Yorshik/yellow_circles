from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
import sys
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from random import randint


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.flag = False
        self.setup()

    def setup(self):
        uic.loadUi('Ui.ui', self)
        self.create_yellow_circle.clicked.connect(self.draw_yellow_circle)

    def draw_yellow_circle(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.setPen(QColor(255, 255, 0))
            r = randint(1, 100)
            self.qp.drawEllipse(QPoint(200, 260), r, r)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())

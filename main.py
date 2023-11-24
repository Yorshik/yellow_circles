import sys
from random import randint

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from ui import Ui_Form


class YellowCircles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.flag = False
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.create_circle.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            color = randint(0, 255), randint(0, 255), randint(0, 255)
            self.qp.setBrush(QColor(*color))
            self.qp.setPen(QColor(*color))
            r = randint(1, 100)
            self.qp.drawEllipse(QPoint(200, 260), r, r)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())

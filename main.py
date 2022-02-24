import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.paint = False
        self.circles = []

    def run(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = randint(0, 500), randint(0, 500)
        diameter = randint(0, 100)
        self.circles.append(((x, y), diameter))
        for pos, diameter in self.circles:
            qp.drawEllipse(*pos, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

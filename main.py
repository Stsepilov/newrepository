import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btnspawn.clicked.connect(self.on_click)
        self.btnspawn = False

    def on_click(self):
        self.btnspawn = True
        self.repaint()

    def draw_ellips(self, qp):
        a = randint(30, 100)
        x = randint(100, 700)
        y = randint(100, 477)
        qp.setBrush(QColor(255, 241, 0))
        qp.setPen(QColor(255, 241, 0))
        qp.drawEllipse(x, y, a, a)

    def paintEvent(self, event):
        if self.btnspawn:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellips(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

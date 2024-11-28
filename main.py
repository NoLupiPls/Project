import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(10, 300)
        y = random.randint(50, 250)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        painter.setPen(QColor(0, 0, 0))
        for x, y, diameter in self.circles:
            painter.drawEllipse(QRect(x, y, diameter, diameter))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

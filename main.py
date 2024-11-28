import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 400, 300)
        self.circles = []

        # Кнопка
        self.button = QPushButton("Добавить круг", self)
        self.button.setGeometry(150, 20, 100, 30)
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(10, 300)
        y = random.randint(50, 250)
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(QColor(0, 0, 0))
            painter.drawEllipse(QRect(x, y, diameter, diameter))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

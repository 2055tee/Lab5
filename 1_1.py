import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import *


class simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        head_color = QColor(255, 204, 153)  # Light brown
        painter.setBrush(QBrush(head_color))
        painter.drawEllipse(180, 50, 80, 80)

        eye_color = QColor(0, 0, 0)  # Black
        painter.setBrush(QBrush(eye_color))
        painter.drawEllipse(200, 70, 15, 15)
        painter.drawEllipse(235, 70, 15, 15)

        mouth_color = QColor(0, 0, 0)  # Black
        painter.setPen(QPen(mouth_color, 2))
        painter.drawArc(212, 100, 20, 20, 0, -180 * 16)

def main():
    app = QApplication(sys.argv)

    w = simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
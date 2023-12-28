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
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(
            [QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150)]
        )

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)])

        p.end()
    
# draw a triangle
class Simple_drawing_window3(simple_drawing_window):
    def __init__(self):
        simple_drawing_window.__init__(self)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a triangle
        triangle_color = QColor(0, 0, 0)
        painter.setBrush(QBrush(triangle_color))

        # Define the points of the triangle
        points = [QPoint(400, 200), QPoint(600, 200), QPoint(300, 50)]
        painter.drawPolygon(points)


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
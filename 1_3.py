import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import *


class simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")

class Simple_drawing_window3(simple_drawing_window):
    def __init__(self):
        simple_drawing_window.__init__(self)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        #Draw star
        star_color = QColor(255, 255, 0)
        painter.setBrush(QBrush(star_color))
        painter.drawPolygon(
            [QPoint(300, 220), QPoint(320, 200), QPoint(340, 220), QPoint(330, 185), QPoint(360, 185), QPoint(330, 175),QPoint(320,150), QPoint(310, 175), QPoint(280, 185), QPoint(310, 185)]
        )


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
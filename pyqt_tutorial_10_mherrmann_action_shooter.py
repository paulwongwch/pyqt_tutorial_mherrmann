import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSound

abs_path = os.path.dirname(os.path.abspath(__file__))

class PlainTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self._holes = []
        self._bullet = QPixmap(os.path.join(abs_path, "./resource/bullet.png"))
        size = self._bullet.size()
        self._offset = QPoint(size.width() // 2, size.height() // 2)

    def mousePressEvent(self, e):
        self._holes.append(e.pos())
        super().mousePressEvent(e)
        self.viewport().update()
        QSound.play(os.path.join(abs_path, "./resource/shot.wav"))

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self.viewport())
        for hole in self._holes:
            painter.drawPixmap(hole - self._offset, self._bullet)


app = QApplication([])
text = PlainTextEdit()
text.setPlainText("Click with the mouse below to shoot ;-)")

app.setApplicationName("Text Editor")
window = QMainWindow()
window.setCentralWidget(text)

window.show()
app.exec_()
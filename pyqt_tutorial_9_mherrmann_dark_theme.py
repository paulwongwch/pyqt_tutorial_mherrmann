import os

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

abs_path = os.path.dirname(os.path.abspath(__file__))

app = QApplication([])
app.setStyle("Fusion")

text =  "<center>"  \
        "<h1>Text Editor</h1>"  \
        "&#8291;"   \
        "<img src='" + os.path.join(abs_path, "resource/icon.svg") + "'>"    \
        "</center>" \
        "<p>Version 0.0.1<br/>"  \
        "Copyright &copy; Company Inc.</p>"

label = QLabel(text)
label.show()

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)

app.setPalette(palette)
app.exec_()
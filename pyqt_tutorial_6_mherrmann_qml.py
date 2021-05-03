from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

app = QApplication([])
engine = QQmlApplicationEngine()
engine.load(r"C:\Users\paulw\PycharmProjects\pyqt_tutorial_mherrmann\pyqt_tutorial_6_mherrmann_main.qml")
app.exec_()
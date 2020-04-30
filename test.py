from PyQt5 import QtWidgets, QtCore
from PyQt5 import Qt
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            print("KIRRAAA KUIN")

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            print("BAITSU DE DASUTO")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
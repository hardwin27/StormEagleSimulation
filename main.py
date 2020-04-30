from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from UIOnly import Ui_MainWindow
import SpriteObject
import sys

class Control(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        # self.mainWindow = QtWidgets.QMainWindow()
        # self.mainUi = Ui_MainWindow()
        # self.mainUi.setupUi(self.mainWindow)
        self.setupUi(self)
        self.StormEagle = SpriteObject.StormEagle
        self.StormEagleSprites = SpriteObject.StormEagleIntro

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            print("KIRRAAA KUIN")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Control()
    controller.show()
    sys.exit(app.exec_())
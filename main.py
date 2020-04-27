from PyQt5 import QtCore, QtWidgets, QtGui
from UIOnly import Ui_MainWindow
import sys

class Control:
    def __init__(self):
        super().__init__()
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.mainWindow)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Control()
    controller.mainWindow.show()
    sys.exit(app.exec_())
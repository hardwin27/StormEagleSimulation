from PyQt5 import QtGui

class Platform():
    def __init__(self, x, y):
        self.platformPic = QtGui.QImage("Resource/Stages.png")
        self.xPos = x
        self.yPos = y
        self.top = 1 - 1
        self.bottom = 96 -1
        self.left = 0
        self.right = 357
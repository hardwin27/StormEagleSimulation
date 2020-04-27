from PyQt5 import QtGui
from Point import Point

class Platform():
    def __init__(self, x, y):
        self.platformPic = QtGui.QImage("Resource/Stages.png")
        self.xPos = x
        self.yPos = y
        self.topCollision = Point(180, 0)
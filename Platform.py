from PyQt5 import QtGui
from CollisionPoint import CollisionPoint

class Platform():
    def __init__(self, x, y):
        self.platformPic = QtGui.QImage("Resource/Stages.png")
        self.xPos = x
        self.yPos = y
        self.topCollision = CollisionPoint(180, 0)
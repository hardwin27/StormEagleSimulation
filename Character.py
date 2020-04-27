from PyQt5 import QtGui
from Point import Point
from Point import Point

class SpriteFrame():
    def __init__(self, centerPoint, top, bottom, left, right, index, maxFrameTime, next):
        self.centerPoint = centerPoint
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.index = index
        self.maxFrameTime = maxFrameTime
        self.next = next

class FrameList():
    pass

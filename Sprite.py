from PyQt5 import QtGui
from Point import Point

class State():
    def __init__(self, name, alpha, omega):
        self.stateName = name
        self.stateFirstIndex = alpha
        self.stateLastIndex = omega

class Character():
    def __init__(self, spriteUrl, width, height, amount, collisionP):
        self.spritesheet = QtGui.QImage(spriteUrl)
        self.spriteWidth = width
        self.spriteHeight = height
        
        self.spriteAmount = amount
        self.xPos = 0
        self.yPos = 0
        self.bottomCollision = collisionP

        self.sprite = []
        for x in range(self.spriteAmount):
            temp = self.spritesheet.copy(x * self.spriteWidth, 0, self.spriteWidth, self.spriteHeight)
            self.sprite.append(temp)
            
        self.mask = []
        for x in range(self.spriteAmount):
            temp2 = self.spritesheet.copy(x * self.spriteWidth, 0, self.spriteWidth, self.spriteHeight)
            self.mask.append(temp2)
        for index in range(len(self.mask)):
            for x in range(self.spriteWidth):
                for y in range(self.spriteHeight):
                    if self.mask[index].pixelColor(x, y) == QtGui.QColor(0, 0, 0, 255):
                        self.mask[index].setPixelColor(x, y, QtGui.QColor(255, 255, 255, 255))
                    else:
                        self.mask[index].setPixelColor(x, y, QtGui.QColor(0, 0, 0, 255))
        
        self.state = []
        self.centerPoint = []

StormEagle = Character("Resource/EagleSprite.png", 76, 99, 18, Point(35, 78))
StormEagle.state = [State("stand", 0, 0), State("gust", 1, 2), State("intro", 3, 6), State("fly", 7, 10), State("stormCannon", 11, 12), State("dive", 13, 14), State("eggBomb", 15, 17)]
StormEagle.centerPoint.append(Point(31, 53))
StormEagle.centerPoint.append(Point(29, 50))
StormEagle.centerPoint.append(Point(32, 58))
StormEagle.centerPoint.append(Point(29, 64))
StormEagle.centerPoint.append(Point(26, 63))
StormEagle.centerPoint.append(Point(32, 64))
StormEagle.centerPoint.append(Point(29, 65))
StormEagle.centerPoint.append(Point(30, 50))
StormEagle.centerPoint.append(Point(30, 55))
StormEagle.centerPoint.append(Point(28, 63))
StormEagle.centerPoint.append(Point(31, 66))
StormEagle.centerPoint.append(Point(37, 52))
StormEagle.centerPoint.append(Point(37, 55))
StormEagle.centerPoint.append(Point(26, 55))
StormEagle.centerPoint.append(Point(32, 57))
StormEagle.centerPoint.append(Point(27, 60))
StormEagle.centerPoint.append(Point(26, 58))
StormEagle.centerPoint.append(Point(28, 48))

Megaman = Character("Resource/MegamanSprite.png", 36, 47, 7, Point(18, 41))
Megaman.centerPoint.append(Point(18, 26))
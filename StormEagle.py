from PyQt5 import QtGui

class StormEagle():
    def __init__(self):
        self.spritesheet = QtGui.QImage('Resource/EagleSprite.png')
        self.spriteWidth = 76
        self.spriteHeight = 99
        self.spriteAmount = 18
        self.xPos = 0
        self.yPos = 0
        
        self.sprite = []
        for x in range(self.spriteAmount):
            temp = self.spritesheet.copy(x * self.spriteWidth, 0, self.spriteWidth, self.spriteHeight)
            self.sprite.append(temp)
            
        # self.maskSheet = self.spritesheet.copy()
        # for x in range(self.spriteWidth):
        #     for y in range(self.spriteHeight):
        #         if self.maskSheet.pixelColor(x, y) == QtGui.QColor(0, 0, 0, 255):
        #             self.maskSheet.setPixelColor(x, y, QtGui.QColor(255, 255, 255, 255))
        #         else:
        #             self.maskSheet.setPixelColor(x, y, QtGui.QColor(0, 0, 0, 255))
        
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
        
from PyQt5 import QtGui

class SpriteSlice():
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

class StormEagle():
    def __init__(self):
        self.spritesheet = QtGui.QPixmap('Resource/EagleSprite.png')
        self.spriteWidth = 76
        self.spriteHeight = 99
        
        self.sprite = []
        for x in range(18):
            temp = SpriteSlice(76 * x, 0)
            self.sprite.append(temp)
        
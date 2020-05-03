from enum import Enum, auto
from PyQt5 import QtGui

class State(Enum):
    offscrean = auto()
    intro = auto()
    stand = auto()
    fly = auto()
    reappear = auto()
    dive = auto()
    hover = auto()
    throwEggBomb =  auto()
    shootStormTornado = auto()
    stagger = auto()
    gust = auto()
    decendingIntro = auto()

class FaceDir(Enum):
    left = auto()
    right = auto()

class Frame:
    def __init__(self, centerX, centerY, top, bottom, left, right, maxCounterVal, next, sprite, mask):
        self.centerX = centerX 
        self.centerY = centerY
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.maxCounterVal = maxCounterVal
        self.next = next
        self.sprite = sprite
        self.mask = mask
        self.frameWidth = self.right - self.left
        self.frameHeight = self.bottom - self.top

class FrameList:
    def __init__(self, character, amount):
        self.array = []
        self.spriteSheet = character.spriteSheet
        self.amount = amount

    def insert(self, centerX, centerY, top, bottom, left, right, maxCounterVal, next):
        tempSprite = self.spriteSheet.copy(left, top, right - left, bottom - top)
        
        tempMask = self.spriteSheet.copy(left, top, right - left, bottom - top)
        for x in range(right - left):
            for y in range(bottom - top):
                if tempMask.pixelColor(x, y) == QtGui.QColor(0, 0, 0, 255):
                    tempMask.setPixelColor(x, y, QtGui.QColor(255, 255, 255, 255))
                else:
                    tempMask.setPixelColor(x, y, QtGui.QColor(0, 0, 0, 255))
        self.array.append(Frame(centerX - left, centerY - top, top - top, bottom - top, left - left, right - left, maxCounterVal, next, tempSprite, tempMask))

class Character:
    def __init__(self, name, spriteUrl, faceDir):
        self.name = name
        self.spriteSheet = QtGui.QImage(spriteUrl)
        self.posX = 0
        self.posY = 0
        self.vX = 0
        self.vY = 0
        self.currentState = State.offscrean
        self.frameIndex = 0
        self.frameTimeCounter = 0
        self.faceDir = faceDir
        self.initFaceDir = faceDir

StormEagle = Character("Storm Eagle", "Resource/EagleSprite.png", FaceDir.left)

StormEagleFly = FrameList(StormEagle, 4)
StormEagleIntro = FrameList(StormEagle, 4)
StormEagleStand = FrameList(StormEagle, 1)
StormEagleGust = FrameList(StormEagle, 2)
StormEagleShootStormCannon = FrameList(StormEagle, 2)
StormEagleThrowEggBomb = FrameList(StormEagle, 3)
StormEagleDive = FrameList(StormEagle, 2)
# StormEagleStagger = FrameList(StormEagle)

StormEagleFly.insert(562, 50, 25, 81, 541, 596, 1, 1)
StormEagleFly.insert(638, 55, 25, 86, 607, 677, 1, 2)
StormEagleFly.insert(712, 63, 4, 94, 687, 749, 1, 3)
StormEagleFly.insert(638, 55, 25, 86, 607, 677, 1, 0)

StormEagleIntro.insert(257, 64, 5, 90, 234, 296, 1, 1)
StormEagleIntro.insert(330, 63, 4, 89, 306, 370, 1, 2)
StormEagleIntro.insert(412, 64, 5, 89, 387, 449, 1, 3)
StormEagleIntro.insert(485, 65, 6, 90, 459, 523, 1, 0)

StormEagleStand.insert(31, 53, 22, 79, 12, 58, 1, 0)

StormEagleGust.insert(105, 50, 25, 76, 86, 141, 1, 1)
StormEagleGust.insert(184, 58, 28, 83, 153, 222, 1, 0)

StormEagleShootStormCannon.insert(873, 52, 21, 78, 843, 900, 1, 1)
StormEagleShootStormCannon.insert(948, 53, 21, 78, 917, 975, 9, 0)

StormEagleThrowEggBomb.insert(1167, 60, 2, 93, 1146, 1208, 1, 1)
StormEagleThrowEggBomb.insert(1242, 59, 0, 92, 1218, 1282, 1, 2)
StormEagleThrowEggBomb.insert(1320, 48, 18, 81, 1291, 1361, 1, 0)


Megaman = Character("Megaman", "Resource/MegamanSprite", FaceDir.right)

MegamanStand = FrameList(Megaman, 3)
MegamanStagger = FrameList(Megaman, 4)

MegamanStand.insert(18, 26, 3, 43, 0, 34, 10, 1)
MegamanStand.insert(54, 25, 2, 42, 36, 70, 10, 2)
MegamanStand.insert(90, 25, 2, 42, 72, 106, 5, 0)

MegamanStagger.insert(126, 26, 3, 43, 108, 143, 1, 1)
MegamanStagger.insert(165, 23, 2, 43, 146, 181, 1, 2)
MegamanStagger.insert(202, 22, 0, 44, 184, 216, 1, 3)
MegamanStagger.insert(237, 22, 1, 44, 218, 257, 1, 0)

StormEagleDive.insert(1024, 51, 15, 84, 997, 1053, 1, 1)
StormEagleDive.insert(1094, 49, 8, 85, 1067, 1131, 1, 0)
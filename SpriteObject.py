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

class FaceDir(Enum):
    left = auto()
    right = auto()

class Frame:
    def __init__(self, centerX, centerY, top, bottom, left, right, maxCounterVal, next, sprite, mask):
        self.centerX = centerX - left
        self.centerY = centerY - top
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
        self.array.append(Frame(centerX, centerY, top, bottom, left, right, maxCounterVal, next, tempSprite, tempMask))

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

StormEagleFly = FrameList(StormEagle, 5)
StormEagleStand = FrameList(StormEagle, 1)
# StormEagleGust = FrameList(StormEagle)
# StormEagleShootStormCannon = FrameList(StormEagle)
# StormEagleFly = FrameList(StormEagle)
# StormEagleHover = FrameList(StormEagle)
# StormEagleThrowEggBomb = FrameList(StormEagle)
# StormEagleStagger = FrameList(StormEagle)

StormEagleFly.insert(562, 50, 25, 81, 541, 596, 1, 1)
StormEagleFly.insert(638, 55, 25, 86, 607, 677, 1, 2)
StormEagleFly.insert(712, 63, 4, 94, 687, 749, 1, 3)
StormEagleFly.insert(638, 55, 25, 86, 607, 677, 1, 0)
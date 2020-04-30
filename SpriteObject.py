from enum import Enum, auto
from PyQt5 import QtGui

class State(Enum):
    none = auto()
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
    def __init__(self, character):
        self.array = []
        self.spriteSheet = character.spriteSheet

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
    def __init__(self, spriteUrl):
        self.spriteSheet = QtGui.QImage(spriteUrl)
        self.posX = 0
        self.posY = 0
        self.vX = 0
        self.vY = 0
        self.currentState = State.none
        self.frameIndex = 0
        self.frameTimeCounter = 0

StormEagle = Character("Resource/EagleSprite.png")

StormEagleIntro = FrameList(StormEagle.spriteSheet)
StormEagleStand = FrameList(StormEagle.spriteSheet)
StormEagleGust = FrameList(StormEagle.spriteSheet)
StormEagleShootStormCannon = FrameList(StormEagle.spriteSheet)
StormEagleFly = FrameList(StormEagle.spriteSheet)
StormEagleHover = FrameList(StormEagle.spriteSheet)
StormEagleThrowEggBomb = FrameList(StormEagle.spriteSheet)
StormEagleStagger = FrameList(StormEagle.spriteSheet)

StormEagleIntro.insert(562, 50, 25, 81, 541, 596, 1, 1)
StormEagleIntro.insert(638, 55, 25, 86, 607, 677, 1, 2)
StormEagleIntro.insert(712, 63, 4, 94, 687, 749, 1, 3)
StormEagleIntro.insert(791, 66, 815, 97, 765, 829, 1, 4)
StormEagleIntro.insert(638, 55, 25, 86, 607, 677, 1, 0)


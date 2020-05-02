from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from UIOnly import Ui_MainWindow
import SpriteObject
from SpriteObject import State, FaceDir
from Platform import Platform
import sys

class Control(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.StormEagle = SpriteObject.StormEagle
        self.StormEagleSprites = SpriteObject.StormEagleFly
        self.StormEagle.currentState = State.reappear
        self.StormEagle.posX = 450
        self.StormEagle.posY = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateScreen)
        self.timer.start(100)

        backgroundPixmap = QtGui.QPixmap("Resource/BG4.jpeg")
        self.platformImage = Platform(168, 321)
        backgroundCanvas = QtGui.QPixmap(self.screenWidth, self.screenHeight)
        painter = QtGui.QPainter(backgroundCanvas)
        painter.drawPixmap(0, 0, self.screenWidth, self.screenHeight, backgroundPixmap)
        painter.drawImage(self.platformImage.xPos, self.platformImage.yPos, self.platformImage.platformPic)
        painter.end()
        self.backgroundImage = backgroundCanvas.toImage()

    def updateStormEagle(self):
        self.StormEagle.frameTimeCounter += 1
        if self.StormEagle.frameTimeCounter > self.StormEagleSprites.array[self.StormEagle.frameIndex].maxCounterVal:
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = self.StormEagleSprites.array[self.StormEagle.frameIndex].next

        if self.StormEagle.currentState == State.reappear:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 5
            self.StormEagle.posX += self.StormEagle.vX
            self.StormEagle.posY += self.StormEagle.vY

        if self.StormEagle.posY + self.StormEagleSprites.array[self.StormEagle.frameIndex].bottom - self.StormEagleSprites.array[self.StormEagle.frameIndex].centerY > self.platformImage.top + self.platformImage.yPos:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 0
            self.StormEagle.currentState = State.intro
            self.StormEagleSprites = SpriteObject.StormEagleIntro
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
        
        if self.StormEagle.currentState == State.intro and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1:
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
            
    def andOperation(self, backgroundColor, maskColor):
        red = bin(backgroundColor.red() & maskColor.red())
        green = bin(backgroundColor.green() & maskColor.green())
        blue = bin(backgroundColor.blue() & maskColor.blue())

        red = int(red, 2)
        green = int(green, 2)
        blue = int(blue, 2)

        # print(str(red) + " " + str(green) + " " + str(blue))

        color = QtGui.QColor(red, green, blue)

        return color

    def orOperation(self, backgroundColor, spriteColor):
        red = bin(backgroundColor.red() | spriteColor.red())
        green = bin(backgroundColor.green() | spriteColor.green())
        blue = bin(backgroundColor.blue() | spriteColor.blue())

        red = int(red, 2)
        green = int(green, 2)
        blue = int(blue, 2)

        # print(str(red) + " " + str(green) + " " + str(blue))

        color = QtGui.QColor(red, green, blue)

        return color

    def masking(self, character, frameList, background):
        if character.faceDir == character.initFaceDir:
            x = 1
            while x < frameList.array[character.frameIndex].frameWidth:
                xForBackground = x + character.posX - 1 - frameList.array[character.frameIndex].centerX
                y = 1
                while y < frameList.array[character.frameIndex].frameHeight:
                    yForBackground = y + character.posY - 1 - frameList.array[character.frameIndex].centerY
                    if xForBackground >= 0 and xForBackground <= self.screenWidth - 1 and yForBackground >= 0 and yForBackground <= self.screenHeight - 1:
                        color1 = self.andOperation(background.pixelColor(xForBackground, yForBackground), frameList.array[character.frameIndex].mask.pixelColor(x, y))
                        background.setPixelColor(xForBackground, yForBackground, color1)
                        color2 = self.orOperation(background.pixelColor(xForBackground, yForBackground), frameList.array[character.frameIndex].sprite.pixelColor(x, y))
                        background.setPixelColor(xForBackground, yForBackground, color2)
                    y += 1
                x += 1
        else:
            x = 1
            while x < frameList.array[character.frameIndex].frameWidth:
                i = frameList.array[character.frameIndex].frameWidth - x
                xForBackground = x + character.posX - 1 - frameList.array[character.frameIndex].centerX
                y = 1
                while y < frameList.array[character.frameIndex].frameHeight:
                    j  = y
                    yForBackground = y + character.posY - 1 - frameList.array[character.frameIndex].centerY
                    if xForBackground >= 0 and xForBackground <= self.screenWidth - 1 and yForBackground >= 0 and yForBackground <= self.screenHeight - 1:
                        color1 = self.andOperation(background.pixelColor(xForBackground, yForBackground), frameList.array[character.frameIndex].mask.pixelColor(i, j))
                        background.setPixelColor(xForBackground, yForBackground, color1)
                        color2 = self.orOperation(background.pixelColor(xForBackground, yForBackground), frameList.array[character.frameIndex].sprite.pixelColor(i, j))
                        background.setPixelColor(xForBackground, yForBackground, color2)
                    y += 1
                x += 1
        return background

    def updateScreen(self):
        self.updateStormEagle()
        backgroundDrawn = self.backgroundImage.copy()
        backgroundDrawn = self.masking(self.StormEagle, self.StormEagleSprites, backgroundDrawn)
        canvas = QtGui.QPixmap(self.screenWidth, self.screenHeight)
        painter = QtGui.QPainter(canvas)
        painter.drawImage(0, 0, backgroundDrawn)
        painter.end()

        self.lbl_MainScreen.setPixmap(canvas)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            self.StormEagle.faceDir = FaceDir.left

        if event.key() == QtCore.Qt.Key_Right:
            self.StormEagle.faceDir = FaceDir.right

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Control()
    controller.show()
    sys.exit(app.exec_())
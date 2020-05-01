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
        self.StormEagle.currentState = State.intro
        self.StormEagle.posX = 300
        self.StormEagle.posY = 300

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateScreen)
        self.timer.start(1000)

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
        
        # if self.StormEagle.currentState == State.intro:
        #     self.StormEagle.vX = 0
        #     self.StormEagle.vY = 5
        #     self.StormEagle.posX += self.StormEagle.vX
        #     self.StormEagle.posY += self.StormEagle.vY



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
        for x in range(frameList.array[character.frameIndex].frameWidth - 1):
            for y in range(frameList.array[character.frameIndex].frameHeight - 1):
                # if character.initFaceDir == character.faceDir:
                #     xForBackground = x + character.posX - frame.array[character.frameIndex].centerX
                #     yForBackground = y + character.posY - frame.array[character.frameIndex].centerY
                # else:
                #     xForBackground = frame.array[character.frameIndex].frameWidth - x + character.posX - frame.array[character.frameIndex].centerX
                #     yForBackground = y + character.posY - frame.array[character.frameIndex].centerY

                
                
                
                if character.initFaceDir == character.faceDir:
                    i = frameList.array[character.frameIndex].left + x + 1
                    xForBackground = character.posX + x
                    print(xForBackground)
                else:
                    i = frameList.array[character.frameIndex].right - x - 1
                    diff = i - frameList.array[character.frameIndex].centerX
                    # if diff > 0:
                    # if frameList.array[character.frameIndex].centerX < round(frameList.array[character.frameIndex].frameWidth / 2):
                    xForBackground = character.posX + x
                    print(xForBackground)

                    # elif diff > 0:
                    #     xForBackground = character.posX + x - frameList.array[character.frameIndex].left - 1 - frameList.array[character.frameIndex].centerX
                    #     print(xForBackground)

                    # else:
                    #     i = frameList.array[character.frameIndex].left + x + 1
                    #     xForBackground = character.posX + x - frameList.array[character.frameIndex].centerX
                    #     print(xForBackground)

                j = frameList.array[character.frameIndex].top + y + 1
                yForBackground = character.posY + y - frameList.array[character.frameIndex].centerY
                
                if xForBackground >= 0 and xForBackground <= self.screenWidth and yForBackground >= 0 and yForBackground <= self.screenHeight:
                    color1 = self.andOperation(background.pixelColor(xForBackground, yForBackground), character.maskSheet.pixelColor(i, j))
                    background.setPixelColor(xForBackground, yForBackground, color1)
                    color2 = self.orOperation(background.pixelColor(xForBackground, yForBackground), character.spriteSheet.pixelColor(i , j))
                    background.setPixelColor(xForBackground, yForBackground, color2)
            
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
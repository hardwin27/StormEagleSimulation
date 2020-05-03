from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from UIOnly import Ui_MainWindow
import SpriteObject
from SpriteObject import State, FaceDir
from Platform import Platform
import sys
import copy

class Control(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        backgroundPixmap = QtGui.QPixmap("Resource/BG4.jpeg")
        self.platformImage = Platform(168, 321)
        backgroundCanvas = QtGui.QPixmap(self.screenWidth, self.screenHeight)
        painter = QtGui.QPainter(backgroundCanvas)
        painter.drawPixmap(0, 0, self.screenWidth, self.screenHeight, backgroundPixmap)
        painter.drawImage(self.platformImage.xPos, self.platformImage.yPos, self.platformImage.platformPic)
        painter.end()
        self.backgroundImage = backgroundCanvas.toImage()

        self.StormEagle = SpriteObject.StormEagle
        self.StormEagleSprites = SpriteObject.StormEagleFly
        self.StormEagle.currentState = State.decendingIntro
        self.StormEagle.posX = 450
        self.StormEagle.posY = 0

        self.Megaman = SpriteObject.Megaman
        self.Megaman.currentState = State.stand
        self.MegamanSprite = SpriteObject.MegamanStand
        self.Megaman.posX = round(self.screenWidth/2)
        self.Megaman.posY = self.platformImage.yPos - self.MegamanSprite.array[self.Megaman.frameIndex].bottom + self.MegamanSprite.array[self.Megaman.frameIndex].centerY 

        # self.StormProjectile = SpriteObject.StormCannon
        # self.StormProjectile.currentState = State.inscreen
        # self.StormProjectileSprite = SpriteObject.StormCannonProjectile
        self.StormProjectile = []
        self.StormProjectileSprite = SpriteObject.StormCannonProjectile

        self.GustProjectile = []
        self.GustProjectileSprite = SpriteObject.GustProjectile
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateScreen)
        self.timer.start(100)

    def updateStormEagle(self):
        self.StormEagle.frameTimeCounter += 1

        if self.StormEagle.currentState == State.decendingIntro:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 5
            self.StormEagle.posX += self.StormEagle.vX
            self.StormEagle.posY += self.StormEagle.vY

        if self.StormEagle.currentState == State.decendingIntro and self.StormEagle.posY + self.StormEagleSprites.array[self.StormEagle.frameIndex].bottom - self.StormEagleSprites.array[self.StormEagle.frameIndex].centerY > self.platformImage.top + self.platformImage.yPos:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 0
            self.StormEagle.currentState = State.intro
            self.StormEagleSprites = SpriteObject.StormEagleIntro
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
            # print(str(self.StormEagle.posX) + " " + str(self.StormEagle.posY))
        
        if self.StormEagle.currentState == State.intro and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1:
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0

        if self.StormEagle.currentState == State.throwEggBomb and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1:
            self.StormEagle.currentState = State.fly
            self.StormEagleSprites = SpriteObject.StormEagleFly
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0

        if self.StormEagle.currentState == State.gust and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1:
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
            self.addGustProjectile(self.StormEagle.posX, self.StormEagle.posY, self.StormEagle.faceDir)

        if self.StormEagle.currentState == State.shootStormTornado and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1 and self.StormEagle.frameTimeCounter >= self.StormEagleSprites.array[self.StormEagle.frameIndex].maxCounterVal:
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
            self.addStormCannonProjectile(self.StormEagle.posX, self.StormEagle.posY, self.StormEagle.faceDir)

        if self.StormEagle.currentState == State.dive:
            self.StormEagle.posX += self.StormEagle.vX
            self.StormEagle.posY += self.StormEagle.vY 

        if self.isOffscreen(self.StormEagle, self.StormEagleSprites) != "nope" and self.StormEagle.currentState != State.fly:
            self.StormEagle.currentState = State.reappear
            self.StormEagleSprites = SpriteObject.StormEagleFly
            self.StormEagle.posX = 450
            self.StormEagle.posY = 0

        if self.StormEagle.currentState == State.reappear:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 5
            self.StormEagle.posX += self.StormEagle.vX
            self.StormEagle.posY += self.StormEagle.vY

        if self.StormEagle.currentState == State.reappear and self.StormEagle.posY + self.StormEagleSprites.array[self.StormEagle.frameIndex].bottom - self.StormEagleSprites.array[self.StormEagle.frameIndex].centerY > self.platformImage.top + self.platformImage.yPos:
            self.StormEagle.vX = 0
            self.StormEagle.vY = 0
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0

        # self.StormEagle.frameTimeCounter += 1
        if self.StormEagle.frameTimeCounter > self.StormEagleSprites.array[self.StormEagle.frameIndex].maxCounterVal:
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = self.StormEagleSprites.array[self.StormEagle.frameIndex].next
            
    def updateMegaman(self):
        self.Megaman.frameTimeCounter += 1


        
        if self.Megaman.frameTimeCounter > self.MegamanSprite.array[self.Megaman.frameIndex].maxCounterVal:
            self.Megaman.frameTimeCounter = 0
            self.Megaman.frameIndex = self.MegamanSprite.array[self.Megaman.frameIndex].next
    
    def updateStormProjectile(self, background):
        if self.StormProjectile != []:
            for x in range(len(self.StormProjectile)):
                self.StormProjectile[x].frameTimeCounter += 1

                self.StormProjectile[x].posX += self.StormProjectile[x].vX

                if self.StormProjectile[x].posX < 0:
                    self.StormProjectile[x].currentState = State.offscrean

                # self.StormProjectile[x].frameTimeCounter += 1
                if self.StormProjectile[x].frameTimeCounter > self.StormProjectileSprite.array[self.StormProjectile[x].frameIndex].maxCounterVal:
                    self.StormProjectile[x].frameTimeCounter = 0
                    self.StormProjectile[x].frameIndex = self.StormProjectileSprite.array[self.StormProjectile[x].frameIndex].next

            for x in range(len(self.StormProjectile)):
                # backgroundDrawn = self.masking(self.StormEagle, self.StormEagleSprites, backgroundDrawn)
                background = self.masking(self.StormProjectile[x], self.StormProjectileSprite, background)

            self.StormProjectile = [x for x in self.StormProjectile if x.currentState != State.offscrean]

        return background

    def addStormCannonProjectile(self, posX, posY, faceDir):
        tempStormProjectile = copy.copy(SpriteObject.StormCannon)
        tempStormProjectile.currentState = State.inscreen
        if faceDir == FaceDir.left:
            tempStormProjectile.posX = posX - 50
            tempStormProjectile.vX = -20
        else:
            tempStormProjectile.posX = posX + 50
            tempStormProjectile.vX = 20
        tempStormProjectile.posY = posY
        tempStormProjectile.faceDir = faceDir
        # tempStormProjectileSprite = copy.copy(SpriteObject.StormCannonProjectile)

        self.StormProjectile.append(tempStormProjectile)
        # self.StormProjectileSprite.append(tempStormProjectileSprite)

    def updateGustProjectile(self, background):
        if self.GustProjectile != []:
            for x in range(len(self.GustProjectile)):
                self.GustProjectile[x].frameTimeCounter += 1

                self.GustProjectile[x].posX += self.GustProjectile[x].vX

                if self.GustProjectile[x].posX < 0:
                    self.GustProjectile[x].currentState = State.offscrean

                # self.GustProjectile[x].frameTimeCounter += 1
                if self.GustProjectile[x].frameTimeCounter > self.GustProjectileSprite.array[self.GustProjectile[x].frameIndex].maxCounterVal:
                    self.GustProjectile[x].frameTimeCounter = 0
                    self.GustProjectile[x].frameIndex = self.GustProjectileSprite.array[self.GustProjectile[x].frameIndex].next

            for x in range(len(self.GustProjectile)):
                background = self.masking(self.GustProjectile[x], self.GustProjectileSprite, background)

            self.GustProjectile = [x for x in self.GustProjectile if x.currentState != State.offscrean]

        # if self.StormProjectile != []:
        #     for x in range(len(self.StormProjectile)):
        #         self.StormProjectile[x].frameTimeCounter += 1

        #         self.StormProjectile[x].posX += self.StormProjectile[x].vX

        #         if self.StormProjectile[x].posX < 0:
        #             self.StormProjectile[x].currentState = State.offscrean

                # self.StormProjectile[x].frameTimeCounter += 1
            #     if self.StormProjectile[x].frameTimeCounter > self.StormProjectileSprite.array[self.StormProjectile[x].frameIndex].maxCounterVal:
            #         self.StormProjectile[x].frameTimeCounter = 0
            #         self.StormProjectile[x].frameIndex = self.StormProjectileSprite.array[self.StormProjectile[x].frameIndex].next

            # for x in range(len(self.StormProjectile)):
                # backgroundDrawn = self.masking(self.StormEagle, self.StormEagleSprites, backgroundDrawn)
            #     background = self.masking(self.StormProjectile[x], self.StormProjectileSprite, background)

            # self.StormProjectile = [x for x in self.StormProjectile if x.currentState != State.offscrean]

        return background


    def addGustProjectile(self, posX, posY, faceDir):
        tempGustProjectile = copy.copy(SpriteObject.Gust)
        tempGustProjectile.currentState = State.inscreen
        if faceDir == FaceDir.left:
            tempGustProjectile.posX = posX - 50
            tempGustProjectile.vX = -20
        else:
            tempGustProjectile.posX = posX + 50
            tempGustProjectile.vX = 20
        tempGustProjectile.posY = posY
        tempGustProjectile.faceDir = faceDir

        self.GustProjectile.append(tempGustProjectile)

        # tempStormProjectile = copy.copy(SpriteObject.StormCannon)
        # tempStormProjectile.currentState = State.inscreen
        # if faceDir == FaceDir.left:
        #     tempStormProjectile.posX = posX - 50
        #     tempStormProjectile.vX = -20
        # else:
        #     tempStormProjectile.posX = posX + 50
        #     tempStormProjectile.vX = 20
        # tempStormProjectile.posY = posY
        # tempStormProjectile.faceDir = faceDir
        # tempStormProjectileSprite = copy.copy(SpriteObject.StormCannonProjectile)

        # self.StormProjectile.append(tempStormProjectile)
        # self.StormProjectileSprite.append(tempStormProjectileSprite)
    
    def isOffscreen(self, character, frameList):
        # if character.posY < 0 or character.posY >= self.screenHeight or character.posX < 0 or character.posX >= self.screenWidth:
        if character.posY + frameList.array[character.frameIndex].bottom - frameList.array[character.frameIndex].centerY < 0 or character.posY - frameList.array[character.frameIndex].centerX >= self.screenHeight or character.posX + frameList.array[character.frameIndex].right - frameList.array[character.frameIndex].centerX < 0 or character.posX -frameList.array[character.frameIndex].centerX >= self.screenWidth:
            if character.posX > round(self.screenWidth/2):
                return "right"
            else:
                return "left"
        return "nope"
    
    def andOperation(self, backgroundColor, maskColor):
        red = bin(backgroundColor.red() & maskColor.red())
        green = bin(backgroundColor.green() & maskColor.green())
        blue = bin(backgroundColor.blue() & maskColor.blue())

        red = int(red, 2)
        green = int(green, 2)
        blue = int(blue, 2)

        color = QtGui.QColor(red, green, blue)

        return color

    def orOperation(self, backgroundColor, spriteColor):
        red = bin(backgroundColor.red() | spriteColor.red())
        green = bin(backgroundColor.green() | spriteColor.green())
        blue = bin(backgroundColor.blue() | spriteColor.blue())

        red = int(red, 2)
        green = int(green, 2)
        blue = int(blue, 2)

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
            x = frameList.array[character.frameIndex].frameWidth - 1
            while x >= 1:
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
                x -= 1
        return background

    def updateScreen(self):
        self.updateStormEagle()
        self.updateMegaman()
        backgroundDrawn = self.backgroundImage.copy()
        backgroundDrawn = self.masking(self.StormEagle, self.StormEagleSprites, backgroundDrawn)
        backgroundDrawn = self.updateStormProjectile(backgroundDrawn)
        backgroundDrawn = self.updateGustProjectile(backgroundDrawn)
        backgroundDrawn = self.masking(self.Megaman, self.MegamanSprite, backgroundDrawn)
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

        if event.key() == QtCore.Qt.Key_Z:
            if self.StormEagle.currentState == State.stand:
                self.StormEagle.currentState = State.gust
                self.StormEagleSprites = SpriteObject.StormEagleGust
                self.StormEagle.frameIndex = 0
                self.StormEagle.frameTimeCounter = 0

        if event.key() == QtCore.Qt.Key_X:
            if self.StormEagle.currentState == State.stand:
                self.StormEagle.currentState = State.shootStormTornado
                self.StormEagleSprites = SpriteObject.StormEagleShootStormCannon
                self.StormEagle.frameIndex = 0
                self.StormEagle.frameTimeCounter = 0

        if event.key() == QtCore.Qt.Key_Up:
            if self.StormEagle.currentState == State.fly or self.StormEagle.currentState == State.stand:
                self.StormEagle.currentState = State.fly
                self.StormEagleSprites = SpriteObject.StormEagleFly
                self.StormEagle.vX = 0
                self.StormEagle.vY = -5
                self.StormEagle.posX += self.StormEagle.vX
                self.StormEagle.posY += self.StormEagle.vY
                
        if event.key() == QtCore.Qt.Key_Down:
            if self.StormEagle.currentState == State.fly:
                self.StormEagle.currentState = State.fly
                self.StormEagleSprites = SpriteObject.StormEagleFly
                self.StormEagle.vX = 0
                self.StormEagle.vY = 5
                self.StormEagle.posX += self.StormEagle.vX
                self.StormEagle.posY += self.StormEagle.vY
                if self.StormEagle.posY + self.StormEagleSprites.array[self.StormEagle.frameIndex].bottom - self.StormEagleSprites.array[self.StormEagle.frameIndex].centerY > self.platformImage.top + self.platformImage.yPos:
                    self.StormEagle.vX = 0
                    self.StormEagle.vY = 0
                    self.StormEagle.currentState = State.stand
                    self.StormEagleSprites = SpriteObject.StormEagleStand
                    self.StormEagle.frameTimeCounter = 0
                    self.StormEagle.frameIndex = 0

        if event.key() == QtCore.Qt.Key_Left:
            if self.StormEagle.currentState == State.fly:
                self.StormEagle.vX = -5
                self.StormEagle.vY = 0
                self.StormEagle.posX += self.StormEagle.vX
                self.StormEagle.posY += self.StormEagle.vY

        if event.key() == QtCore.Qt.Key_Right:
            if self.StormEagle.currentState == State.fly:
                self.StormEagle.vX = 5
                self.StormEagle.vY = 0
                self.StormEagle.posX += self.StormEagle.vX
                self.StormEagle.posY += self.StormEagle.vY

        if event.key() == QtCore.Qt.Key_C:
            if self.StormEagle.currentState == State.fly:
                self.StormEagle.currentState = State.throwEggBomb
                self.StormEagleSprites = SpriteObject.StormEagleThrowEggBomb
                self.StormEagle.frameTimeCounter = 0
                self.StormEagle.frameIndex = 0

        if event.key() == QtCore.Qt.Key_Space:
            sides = self.isOffscreen(self.StormEagle, self.StormEagleSprites)
            if sides == "right":
                self.StormEagle.currentState = State.dive
                self.StormEagleSprites = SpriteObject.StormEagleDive
                self.StormEagle.frameTimeCounter = 0
                self.StormEagle.frameIndex = 0
                if self.StormEagle.posX > self.screenWidth - 1:
                    self.StormEagle.posX = self.screenWidth - 1
                self.StormEagle.posY = 0
                self.StormEagle.vX = -50
                self.StormEagle.vY = 50
                self.StormEagle.faceDir = FaceDir.left
            elif sides == "left":
                self.StormEagle.currentState = State.dive
                self.StormEagleSprites = SpriteObject.StormEagleDive
                self.StormEagle.frameTimeCounter = 0
                self.StormEagle.frameIndex = 0
                if self.StormEagle.posX < 0:
                    self.StormEagle.posX = 0
                self.StormEagle.vX = 50
                self.StormEagle.vY = 50
                self.StormEagle.faceDir = FaceDir.right

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Control()
    controller.show()
    sys.exit(app.exec_())
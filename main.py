from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from UIOnly import Ui_MainWindow
import SpriteObject
from SpriteObject import State, FaceDir
from Platform import Platform
import sys
import copy
import random

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
        self.megamanCollisionIsOn = True

        self.StormProjectile = []
        self.StormProjectileSprite = SpriteObject.StormCannonProjectile

        self.GustProjectile = []
        self.GustProjectileSprite = SpriteObject.GustProjectile

        self.EggBombProjectile = []
        self.EggBombProjectileSprite = []

        self.gravitation = 50

        self.counterForRespawn = 0
        
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
            self.addEggBombProjectile(self.StormEagle.posX, self.StormEagle.posY, self.StormEagle.faceDir)

        if self.StormEagle.currentState == State.gust and self.StormEagle.frameIndex == self.StormEagleSprites.amount - 1:
            self.StormEagle.currentState = State.stand
            self.StormEagleSprites = SpriteObject.StormEagleStand
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = 0
            self.addGustProjectile(self.StormEagle.posX, self.StormEagle.posY + self.StormEagleSprites.array[self.StormEagle.frameIndex].bottom - self.StormEagleSprites.array[self.StormEagle.frameIndex].centerY - 5, self.StormEagle.faceDir)

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


        if self.checkCollisionDetection(self.StormEagleSprites.array[self.StormEagle.frameIndex], self.MegamanSprite.array[self.Megaman.frameIndex], self.StormEagle, self.Megaman):
            self.Megaman.currentState = State.stagger
            self.MegamanSprite = SpriteObject.MegamanStagger
            self.Megaman.frameIndex = 0
            self.Megaman.frameTimeCounter = 0
            if self.StormEagle.faceDir == FaceDir.left:
                self.Megaman.vX = - 5
                self.Megaman.faceDir = FaceDir.right
            else:
                self.Megaman.vX = 5
                self.Megaman.faceDir = FaceDir.left

        # self.StormEagle.frameTimeCounter += 1
        if self.StormEagle.frameTimeCounter > self.StormEagleSprites.array[self.StormEagle.frameIndex].maxCounterVal:
            self.StormEagle.frameTimeCounter = 0
            self.StormEagle.frameIndex = self.StormEagleSprites.array[self.StormEagle.frameIndex].next
            
    def updateMegaman(self):
        self.Megaman.frameTimeCounter += 1
        if self.Megaman.posX > self.platformImage.xPos  and self.Megaman.posX <= self.platformImage.xPos + self.platformImage.right:          
            if self.Megaman.currentState == State.stagger and self.Megaman.frameIndex == self.MegamanSprite.amount - 1:
                self.Megaman.currentState = State.stand
                self.MegamanSprite = SpriteObject.MegamanStand
                self.Megaman.frameIndex = 0
                self.Megaman.frameTimeCounter = 0
                self.Megaman.vX = 0
           
        else:
            if self.Megaman.currentState != State.offscrean:
                self.Megaman.currentState = State.falling
                self.MegamanSprite = SpriteObject.MegamanStagger
                self.Megaman.frameIndex = 0
                self.Megaman.frameTimeCounter = 0
                self.Megaman.vX = 0
                self.Megaman.vY = 10

        if self.Megaman.posY - 20 > self.screenHeight:
            if self.Megaman.currentState == State.falling:
                self.counterForRespawn = 0
                self.Megaman.currentState = State.offscrean
            self.Megaman.vY = 0
            self.counterForRespawn += 1
            if self.counterForRespawn >= 30:
                self.Megaman.currentState = State.stand
                self.MegamanSprite = SpriteObject.MegamanStand
                self.Megaman.frameIndex = 0
                self.Megaman.frameTimeCounter = 0
                randomLocation = random.randint(self.platformImage.xPos + self.platformImage.left + 5, self.platformImage.xPos + self.platformImage.right - 5)
                while randomLocation > self.StormEagle.posX - 20 and randomLocation < self.StormEagle.posX + 20:
                    randomLocation = random.randint(self.platformImage.xPos + self.platformImage.left + 5, self.platformImage.xPos + self.platformImage.right - 5)
                self.Megaman.posX = randomLocation
                self.Megaman.posY = self.platformImage.yPos - self.MegamanSprite.array[self.Megaman.frameIndex].bottom + self.MegamanSprite.array[self.Megaman.frameIndex].centerY 

        self.Megaman.posX += self.Megaman.vX
        self.Megaman.posY += self.Megaman.vY

        if self.Megaman.frameTimeCounter > self.MegamanSprite.array[self.Megaman.frameIndex].maxCounterVal:
            self.Megaman.frameTimeCounter = 0
            self.Megaman.frameIndex = self.MegamanSprite.array[self.Megaman.frameIndex].next
    
    def updateStormProjectile(self, background):
        if self.StormProjectile != []:
            for x in range(len(self.StormProjectile)):
                self.StormProjectile[x].frameTimeCounter += 1

                self.StormProjectile[x].posX += self.StormProjectile[x].vX
                
                if self.checkCollisionDetection(self.StormProjectileSprite.array[self.StormProjectile[x].frameIndex], self.MegamanSprite.array[self.Megaman.frameIndex], self.StormProjectile[x], self.Megaman) and self.Megaman.currentState == State.stand:
                    self.Megaman.currentState = State.stagger
                    self.MegamanSprite = SpriteObject.MegamanStagger
                    self.Megaman.frameIndex = 0
                    self.Megaman.frameTimeCounter = 0
                    if self.StormProjectile[x].faceDir == FaceDir.left:
                        self.Megaman.vX = -5
                        self.Megaman.faceDir = FaceDir.right
                    else:
                        self.Megaman.vX = 5
                        self.Megaman.faceDir = FaceDir.left

                if self.StormProjectile[x].posX < 0 or self.StormProjectile[x].posX >= self.screenWidth:
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

                if self.checkCollisionDetection(self.GustProjectileSprite.array[self.GustProjectile[x].frameIndex], self.MegamanSprite.array[self.Megaman.frameIndex], self.GustProjectile[x], self.Megaman):
                    if self.GustProjectile[x].faceDir == FaceDir.left:
                        self.Megaman.faceDir = FaceDir.right
                        self.Megaman.vX = -5
                    else:
                        self.Megaman.faceDir = FaceDir.left
                        self.Megaman.vX = 5
                else:
                    self.Megaman.vX = 0

                if self.GustProjectile[x].posX < 0:
                    self.GustProjectile[x].currentState = State.offscrean

                # self.GustProjectile[x].frameTimeCounter += 1
                if self.GustProjectile[x].frameTimeCounter > self.GustProjectileSprite.array[self.GustProjectile[x].frameIndex].maxCounterVal:
                    self.GustProjectile[x].frameTimeCounter = 0
                    self.GustProjectile[x].frameIndex = self.GustProjectileSprite.array[self.GustProjectile[x].frameIndex].next

            for x in range(len(self.GustProjectile)):
                background = self.masking(self.GustProjectile[x], self.GustProjectileSprite, background)

            self.GustProjectile = [x for x in self.GustProjectile if x.currentState != State.offscrean]

        return background

    def addGustProjectile(self, posX, posY, faceDir):
        tempGustProjectile = copy.copy(SpriteObject.Gust)
        tempGustProjectile.currentState = State.inscreen
        if faceDir == FaceDir.left:
            tempGustProjectile.posX = posX - 50
            tempGustProjectile.vX = -30
        else:
            tempGustProjectile.posX = posX + 50
            tempGustProjectile.vX = 30
        tempGustProjectile.posY = posY
        tempGustProjectile.faceDir = faceDir

        self.GustProjectile.append(tempGustProjectile)

    def updateEggBombProjectile(self, background):
        if self.EggBombProjectile != []:
            for x in range(len(self.EggBombProjectile)):
                self.EggBombProjectile[x].frameTimeCounter += 1

                self.EggBombProjectile[x].posX += self.EggBombProjectile[x].vX
                self.EggBombProjectile[x].posY += self.EggBombProjectile[x].vY

                if self.EggBombProjectile[x].vY < 10 and self.EggBombProjectile[x].currentState == State.egg:
                    self.EggBombProjectile[x].vY += self.gravitation

                if self.EggBombProjectile[x].posX < 0 or self.EggBombProjectile[x].posX >= self.screenWidth or self.EggBombProjectile[x].posY < 0 or self.EggBombProjectile[x].posY >= self.screenHeight:
                    self.EggBombProjectile[x].currentState = State.offscrean

                if self.checkCollisionDetection(self.EggBombProjectileSprite[x].array[self.EggBombProjectile[x].frameIndex], self.MegamanSprite.array[self.Megaman.frameIndex], self.EggBombProjectile[x], self.Megaman):
                    self.Megaman.currentState = State.stagger
                    self.MegamanSprite = SpriteObject.MegamanStagger
                    self.Megaman.frameIndex = 0
                    self.Megaman.frameTimeCounter = 0
                    if self.EggBombProjectile[x].faceDir == FaceDir.left:
                        self.Megaman.vX = - 1
                        self.Megaman.faceDir = FaceDir.right
                    else:
                        self.Megaman.vX = 1
                        self.Megaman.faceDir = FaceDir.left
                    if self.EggBombProjectile[x].currentState == State.egg:
                        self.EggBombProjectile[x].currentState = State.offscrean
                
                if self.EggBombProjectile[x].currentState == State.egg and self.EggBombProjectile[x].posY + self.EggBombProjectileSprite[x].array[self.EggBombProjectile[x].frameIndex].bottom - self.EggBombProjectileSprite[x].array[self.EggBombProjectile[x].frameIndex].centerY > self.platformImage.top + self.platformImage.yPos:
                    self.EggBombProjectile[x].currentState = State.littleBird                                                                                   
                    self.EggBombProjectileSprite[x] = SpriteObject.EggBombLittleBird
                    self.EggBombProjectile[x].frameTimeCounter = 0
                    self.EggBombProjectile[x].frameIndex = 0
                    if self.EggBombProjectile[x].posX > self.Megaman.posX:
                        self.EggBombProjectile[x].vX = -20
                        self.EggBombProjectile[x].faceDir = FaceDir.left
                    else:
                        self.EggBombProjectile[x].vX = 20
                        self.EggBombProjectile[x].faceDir = FaceDir.right
                    self.EggBombProjectile[x].vY = 0
                    self.EggBombProjectile[x].posY = self.platformImage.top + self.platformImage.yPos - 10

                # self.EggBombProjectile[x].frameTimeCounter += 1
                if self.EggBombProjectile[x].frameTimeCounter > self.EggBombProjectileSprite[x].array[self.EggBombProjectile[x].frameIndex].maxCounterVal:
                    self.EggBombProjectile[x].frameTimeCounter = 0
                    self.EggBombProjectile[x].frameIndex = self.EggBombProjectileSprite[x].array[self.EggBombProjectile[x].frameIndex].next

            for x in range(len(self.EggBombProjectile)):
                background = self.masking(self.EggBombProjectile[x], self.EggBombProjectileSprite[x], background)

            for x in range(len((self.EggBombProjectile))):
                if self.EggBombProjectile[x].currentState == State.offscrean:
                    temp = self.EggBombProjectileSprite.pop(x)
                    del(temp)

            self.EggBombProjectile = [x for x in self.EggBombProjectile if x.currentState != State.offscrean]

        return background

    def addEggBombProjectile(self, posX, posY, faceDir):
        tempEggBombProjectile = copy.copy(SpriteObject.EggBomb)
        tempEggBombProjectile.currentState = State.egg
        tempEggBombProjectileSprite = copy.copy(SpriteObject.EggBombEgg)

        tempEggBombProjectile.posX = posX
        tempEggBombProjectile.posY = posY
        if faceDir == FaceDir.left:
            tempEggBombProjectile.posX = posX - 5
            tempEggBombProjectile.vX = -5
            tempEggBombProjectile.vY = -20
        else:
            tempEggBombProjectile.posX = posX + 5
            tempEggBombProjectile.vX = 5
            tempEggBombProjectile.vY = -20
        tempEggBombProjectile.faceDir = faceDir

        self.EggBombProjectile.append(tempEggBombProjectile)
        self.EggBombProjectileSprite.append(tempEggBombProjectileSprite)
        
    def isOffscreen(self, character, frameList):
        if character.posY + frameList.array[character.frameIndex].bottom - frameList.array[character.frameIndex].centerY < 0 or character.posY - frameList.array[character.frameIndex].centerX >= self.screenHeight or character.posX + frameList.array[character.frameIndex].right - frameList.array[character.frameIndex].centerX < 0 or character.posX -frameList.array[character.frameIndex].centerX >= self.screenWidth:
            if character.posX > round(self.screenWidth/2):
                return "right"
            else:
                return "left"
        return "nope"

    def checkCollisionDetection(self, frame2, frame1, object2, object1):
        L1 = frame1.left + object1.posX - 1 - frame1.centerX
        R1 = frame1.right + object1.posX - 1 - frame1.centerX
        T1 = frame1.top + object1.posY - 1 - frame1.centerY
        B1 = frame1.bottom + object1.posY - 1 - frame1.centerY

        L2 = frame2.left + object2.posX - 1 - frame2.centerX
        R2 = frame2.right + object2.posX - 1 - frame2.centerX
        T2 = frame2.top + object2.posY - 1 - frame2.centerY
        B2 = frame2.bottom + object2.posY - 1 - frame2.centerY

        if L2 < R1 and L1 < R2 and T1 < B2 and T2 < B1 :
            return True
        else:
            return False
    
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
        backgroundDrawn = self.updateEggBombProjectile(backgroundDrawn)
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
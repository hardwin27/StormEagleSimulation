# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIOnly.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import Qt
# from Sprite import StormEagle, Megaman
# from Platform import Platform


class Ui_MainWindow(object):

    # def __init__(self):
    #     QtWidgets.QMainWindow.__init__(self)

    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key_Up:
    #         self.timerStormEagle.stop()
    # signalTest = QtCore.pyqtSignal()

    # def testingPrint(self):
    #     print("HELLO")

    def setupUi(self, MainWindow):
        self.screenWidth = 670
        self.screenHeight = 420

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 477)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0845771, y1:0.659, x2:1, y2:0.506, stop:0 rgba(0, 0, 133, 255), stop:1 rgba(186, 0, 255, 255));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lbl_Movement = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Movement.setGeometry(QtCore.QRect(720, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Movement.setFont(font)
        self.lbl_Movement.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Movement.setObjectName("lbl_Movement")
        
        self.lbl_Ctrl = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Ctrl.setGeometry(QtCore.QRect(790, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Ctrl.setFont(font)
        self.lbl_Ctrl.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Ctrl.setObjectName("lbl_Ctrl")
        
        self.lbl_Gust = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Gust.setGeometry(QtCore.QRect(720, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Gust.setFont(font)
        self.lbl_Gust.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Gust.setObjectName("lbl_Gust")
        
        self.lbl_Egg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Egg.setGeometry(QtCore.QRect(720, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Egg.setFont(font)
        self.lbl_Egg.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Egg.setObjectName("lbl_Egg")
        
        self.lbl_Reappear = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Reappear.setGeometry(QtCore.QRect(720, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Reappear.setFont(font)
        self.lbl_Reappear.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Reappear.setObjectName("lbl_Reappear")
        
        self.lbl_Dive = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Dive.setGeometry(QtCore.QRect(720, 240, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Dive.setFont(font)
        self.lbl_Dive.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Dive.setObjectName("lbl_Dive")
        
        self.lbl_Storm = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Storm.setGeometry(QtCore.QRect(720, 270, 91, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Storm.setFont(font)
        self.lbl_Storm.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Storm.setObjectName("lbl_Storm")
        
        self.lbl_MainScreen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_MainScreen.setGeometry(QtCore.QRect(30, 20, self.screenWidth, self.screenHeight))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_MainScreen.sizePolicy().hasHeightForWidth())
        self.lbl_MainScreen.setSizePolicy(sizePolicy)
        self.lbl_MainScreen.setText("")
        self.lbl_MainScreen.setScaledContents(True)
        self.lbl_MainScreen.setObjectName("lbl_MainScreen")

        # backgroundPixmap = QtGui.QPixmap("Resource/BG4.jpeg")
        # self.platformImage = Platform(168, 321)
        # backgroundCanvas = QtGui.QPixmap(self.screenWidth, self.screenHeight)
        # painter = QtGui.QPainter(backgroundCanvas)
        # painter.drawPixmap(0, 0, self.screenWidth, self.screenHeight, backgroundPixmap)
        # painter.drawImage(self.platformImage.xPos, self.platformImage.yPos, self.platformImage.platformPic)
        # painter.end()
        # self.backgroundImage = backgroundCanvas.toImage()

        # self.stormEagle = StormEagle
        # self.stormEagleState = 3
        # self.stormEagleIndex = self.stormEagle.state[self.stormEagleState].stateFirstIndex
        # self.stormEagle.xPos = 450
        # self.stormEagle.yPos = 0

        # self.timerStormEagle = QtCore.QTimer()
        # self.timerStormEagle.timeout.connect(self.animate)
        # self.timerStormEagle.start(200)

        # self.megaMan = Megaman
        # self.megaManIndex = 0
        # self.megaMan.xPos = 200
        # self.megaMan.yPos = 200

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def andOperation(self, backgroundColor, maskColor):
    #     red = bin(backgroundColor.red() & maskColor.red())
    #     green = bin(backgroundColor.green() & maskColor.green())
    #     blue = bin(backgroundColor.blue() & maskColor.blue())

    #     red = int(red, 2)
    #     green = int(green, 2)
    #     blue = int(blue, 2)

    #     # print(str(red) + " " + str(green) + " " + str(blue))

    #     color = QtGui.QColor(red, green, blue)

    #     return color

    # def orOperation(self, backgroundColor, spriteColor):
    #     red = bin(backgroundColor.red() | spriteColor.red())
    #     green = bin(backgroundColor.green() | spriteColor.green())
    #     blue = bin(backgroundColor.blue() | spriteColor.blue())

    #     red = int(red, 2)
    #     green = int(green, 2)
    #     blue = int(blue, 2)

    #     # print(str(red) + " " + str(green) + " " + str(blue))

    #     color = QtGui.QColor(red, green, blue)

    #     return color

    # def maskingStormEagle(self):
    #     for x in range(self.stormEagle.spriteWidth):
    #         for y in range(self.stormEagle.spriteHeight):
    #             backgroundX = x + self.stormEagle.xPos - self.stormEagle.centerPoint[self.stormEagleIndex].xPos
    #             backgroundY = y + self.stormEagle.yPos - self.stormEagle.centerPoint[self.stormEagleIndex].yPos
    #             if backgroundX >= 0 and backgroundX <= self.screenWidth and backgroundY >= 0 and backgroundY <= self.screenHeight:
    #                 # print(str(backgroundX) + " " + str(backgroundY))
    #                 color1 = self.andOperation(self.backgroundUse.pixelColor(backgroundX, backgroundY), self.stormEagleMaskUse.pixelColor(x, y))
    #                 self.backgroundUse.setPixelColor(backgroundX, backgroundY, color1)
    #                 color2 = self.orOperation(self.backgroundUse.pixelColor(backgroundX, backgroundY), self.stormEagleSpriteUse.pixelColor(x, y))
    #                 self.backgroundUse.setPixelColor(backgroundX, backgroundY, color2)

    # def maskingMegaMan(self):
    #     for x in range(self.megaMan.spriteWidth):
    #         for y in range(self.megaMan.spriteHeight):
    #             backgroundX = x + self.megaMan.xPos - self.megaMan.centerPoint[self.megaManIndex].xPos
    #             backgroundY = y + self.megaMan.yPos - self.megaMan.centerPoint[self.megaManIndex].yPos
    #             if backgroundX >= 0 and backgroundX <= self.screenWidth and backgroundY >= 0 and backgroundY <= self.screenHeight:
    #                 # print(str(backgroundX) + " " + str(backgroundY))
    #                 color1 = self.andOperation(self.backgroundUse.pixelColor(backgroundX, backgroundY), self.megaManMaskUse.pixelColor(x, y))
    #                 self.backgroundUse.setPixelColor(backgroundX, backgroundY, color1)
    #                 color2 = self.orOperation(self.backgroundUse.pixelColor(backgroundX, backgroundY), self.megaManSpriteUse.pixelColor(x, y))
    #                 self.backgroundUse.setPixelColor(backgroundX, backgroundY, color2)

    # def animate(self):
    #     if self.stormEagleState == 3 and self.stormEagle.bottomCollision.yPos + self.stormEagle.yPos - self.stormEagle.centerPoint[self.stormEagleIndex].yPos >= self.platformImage.topCollision.yPos + self.platformImage.yPos:
    #         self.stormEagleState = 2
    #         self.stormEagleIndex = self.stormEagle.state[self.stormEagleState].stateFirstIndex

    #     if self.stormEagleState == 2 and self.stormEagleIndex >= self.stormEagle.state[self.stormEagleState].stateLastIndex:
    #         self.stormEagleState = 0
    #         self.stormEagleIndex = self.stormEagle.state[self.stormEagleState].stateFirstIndex

    #     if self.stormEagleState == 3 and self.stormEagleIndex > self.stormEagle.state[3].stateLastIndex:
    #         self.stormEagleIndex = self.stormEagle.state[3].stateFirstIndex

    #     self.backgroundUse = self.backgroundImage.copy()
    #     self.stormEagleSpriteUse = self.stormEagle.sprite[self.stormEagleIndex].copy()
    #     self.stormEagleMaskUse = self.stormEagle.mask[self.stormEagleIndex].copy()
    #     self.maskingStormEagle()

    #     self.megaManSpriteUse = self.megaMan.sprite[self.megaManIndex].copy()
    #     self.megaManMaskUse = self.megaMan.mask[self.megaManIndex].copy()
    #     self.maskingMegaMan()

    #     canvas = QtGui.QPixmap(self.screenWidth, self.screenHeight)
    #     painter = QtGui.QPainter(canvas)
    #     painter.drawImage(0, 0, self.backgroundUse)
    #     painter.end()

    #     if self.stormEagleState != 0: 
    #         self.stormEagleIndex += 1

    #     if self.stormEagleState == 3:
    #         self.stormEagle.yPos += 5

    #     self.lbl_MainScreen.setPixmap(canvas)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_Movement.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Movement:</span></p></body></html>"))
        self.lbl_Ctrl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Controls</span></p></body></html>"))
        self.lbl_Gust.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gust    :</span></p></body></html>"))
        self.lbl_Egg.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Egg Bomb:</span></p></body></html>"))
        self.lbl_Reappear.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Reappear:</span></p></body></html>"))
        self.lbl_Dive.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Dive    :</span></p></body></html>"))
        self.lbl_Storm.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Storm   :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

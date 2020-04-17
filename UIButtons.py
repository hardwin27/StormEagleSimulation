# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIButtons.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 856)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.766, y1:0.136455, x2:1, y2:0, stop:0 rgba(4, 0, 113, 255), stop:1 rgba(241, 214, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_up.setGeometry(QtCore.QRect(140, 480, 31, 81))
        self.btn_up.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_up.setObjectName("btn_up")
        self.btn_Down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Down.setGeometry(QtCore.QRect(140, 630, 31, 81))
        self.btn_Down.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Down.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Down.setObjectName("btn_Down")
        self.btn_Right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Right.setGeometry(QtCore.QRect(190, 580, 81, 31))
        self.btn_Right.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Right.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Right.setObjectName("btn_Right")
        self.btn_Left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Left.setGeometry(QtCore.QRect(40, 580, 81, 31))
        self.btn_Left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Left.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Left.setObjectName("btn_Left")
        self.btn_Gust = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Gust.setGeometry(QtCore.QRect(450, 490, 51, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Gust.setFont(font)
        self.btn_Gust.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Gust.setObjectName("btn_Gust")
        self.btn_Dive = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Dive.setGeometry(QtCore.QRect(590, 490, 51, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Dive.setFont(font)
        self.btn_Dive.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Dive.setObjectName("btn_Dive")
        self.btn_Reappear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Reappear.setGeometry(QtCore.QRect(450, 640, 51, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Reappear.setFont(font)
        self.btn_Reappear.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Reappear.setObjectName("btn_Reappear")
        self.btn_Storm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Storm.setGeometry(QtCore.QRect(590, 640, 51, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Storm.setFont(font)
        self.btn_Storm.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_Storm.setObjectName("btn_Storm")
        self.btn_EGGGGGGGG = QtWidgets.QPushButton(self.centralwidget)
        self.btn_EGGGGGGGG.setGeometry(QtCore.QRect(520, 560, 61, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_EGGGGGGGG.setFont(font)
        self.btn_EGGGGGGGG.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.btn_EGGGGGGGG.setObjectName("btn_EGGGGGGGG")
        self.btn_Start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Start.setGeometry(QtCore.QRect(270, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Start.setFont(font)
        self.btn_Start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Start.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }")
        self.btn_Start.setIconSize(QtCore.QSize(10, 10))
        self.btn_Start.setFlat(True)
        self.btn_Start.setObjectName("btn_Start")
        self.btn_Select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Select.setGeometry(QtCore.QRect(370, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_Select.setFont(font)
        self.btn_Select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Select.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"    ")
        self.btn_Select.setFlat(True)
        self.btn_Select.setObjectName("btn_Select")
        self.lbl_Egg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Egg.setGeometry(QtCore.QRect(510, 620, 81, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Egg.setFont(font)
        self.lbl_Egg.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Egg.setObjectName("lbl_Egg")
        self.lbl_Gust = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Gust.setGeometry(QtCore.QRect(460, 540, 41, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Gust.setFont(font)
        self.lbl_Gust.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Gust.setObjectName("lbl_Gust")
        self.lbl_Dive = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Dive.setGeometry(QtCore.QRect(600, 540, 41, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Dive.setFont(font)
        self.lbl_Dive.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Dive.setObjectName("lbl_Dive")
        self.lbl_Storm = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Storm.setGeometry(QtCore.QRect(590, 690, 51, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Storm.setFont(font)
        self.lbl_Storm.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Storm.setObjectName("lbl_Storm")
        self.lbl_Reappear = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Reappear.setGeometry(QtCore.QRect(440, 690, 81, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.lbl_Reappear.setFont(font)
        self.lbl_Reappear.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.lbl_Reappear.setObjectName("lbl_Reappear")
        self.lbl_MainScreen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_MainScreen.setGeometry(QtCore.QRect(30, 20, 661, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_MainScreen.sizePolicy().hasHeightForWidth())
        self.lbl_MainScreen.setSizePolicy(sizePolicy)
        self.lbl_MainScreen.setText("")
        self.lbl_MainScreen.setScaledContents(True)
        self.lbl_MainScreen.setObjectName("lbl_MainScreen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_up.setText(_translate("MainWindow", "↑"))
        self.btn_Down.setText(_translate("MainWindow", "↓"))
        self.btn_Right.setText(_translate("MainWindow", "→"))
        self.btn_Left.setText(_translate("MainWindow", "←"))
        self.btn_Gust.setText(_translate("MainWindow", "B"))
        self.btn_Dive.setText(_translate("MainWindow", "C"))
        self.btn_Reappear.setText(_translate("MainWindow", "X"))
        self.btn_Storm.setText(_translate("MainWindow", "Y"))
        self.btn_EGGGGGGGG.setText(_translate("MainWindow", "A"))
        self.btn_Start.setText(_translate("MainWindow", "Start"))
        self.btn_Select.setText(_translate("MainWindow", "Select"))
        self.lbl_Egg.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Egg Bomb</span></p></body></html>"))
        self.lbl_Gust.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gust</span></p></body></html>"))
        self.lbl_Dive.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Dive</span></p></body></html>"))
        self.lbl_Storm.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Storm</span></p></body></html>"))
        self.lbl_Reappear.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Reappear</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_game.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.resize(540, 600)
        self.RandomPicture = QLabel(GameWindow)
        self.RandomPicture.setObjectName(u"RandomPicture")
        self.RandomPicture.setGeometry(QRect(40, 20, 451, 311))
        self.RandomPicture.setAutoFillBackground(False)
        self.RandomPicture.setStyleSheet(u"border: 2px solid rgb(102,205,170);")
        self.RandomPicture.setScaledContents(True)
        self.RandomPicture.setWordWrap(True)
        self.RandomWord = QLabel(GameWindow)
        self.RandomWord.setObjectName(u"RandomWord")
        self.RandomWord.setGeometry(QRect(40, 350, 451, 71))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(40)
        self.RandomWord.setFont(font)
        self.RandomWord.setAutoFillBackground(False)
        self.RandomWord.setStyleSheet(u"\n"
"\n"
"\n"
"QLabel {  color : rgb(255, 255, 255)};\n"
"border: 4px solid #20B2AA;\n"
"border-radius: 35px; background: rgb(85, 170, 255)rgba(102, 205, 170, 190); ")
        self.RandomWord.setAlignment(Qt.AlignCenter)
        self.Back = QPushButton(GameWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(40, 510, 220, 60))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(20)
        self.Back.setFont(font1)
        self.Back.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid white;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: rgb(102,205,170);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(3, 205, 150);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(70, 255, 150);\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.NextWord = QPushButton(GameWindow)
        self.NextWord.setObjectName(u"NextWord")
        self.NextWord.setGeometry(QRect(271, 510, 220, 60))
        self.NextWord.setFont(font1)
        self.NextWord.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid white;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: rgb(102,205,170);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(3, 205, 150);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(70, 255, 150);\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.StartTimer = QPushButton(GameWindow)
        self.StartTimer.setObjectName(u"StartTimer")
        self.StartTimer.setGeometry(QRect(271, 440, 85, 60))
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(18)
        self.StartTimer.setFont(font2)
        self.StartTimer.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid white;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: rgb(102,205,170);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(3, 205, 150);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(70, 255, 150);\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.Time = QLabel(GameWindow)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(40, 440, 220, 61))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(20)
        self.Time.setFont(font3)
        self.Time.setStyleSheet(u"\n"
"\n"
"\n"
"QLabel {  color : rgb(255, 255, 255)};\n"
"border: 2px solid #baedff;\n"
"border-radius: 30px; background: rgb(102, 205, 170); \n"
"\n"
"")
        self.Time.setAlignment(Qt.AlignCenter)
        self.SetTime = QPushButton(GameWindow)
        self.SetTime.setObjectName(u"SetTime")
        self.SetTime.setGeometry(QRect(360, 440, 131, 60))
        self.SetTime.setFont(font2)
        self.SetTime.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid white;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: rgb(102,205,170);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(3, 205, 150);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(70, 255, 150);\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"Crocodile!", None))
        self.RandomPicture.setText("")
        self.RandomWord.setText(QCoreApplication.translate("GameWindow", u"Sunflower", None))
        self.Back.setText(QCoreApplication.translate("GameWindow", u"Back", None))
        self.NextWord.setText(QCoreApplication.translate("GameWindow", u"Next word", None))
        self.StartTimer.setText(QCoreApplication.translate("GameWindow", u"Start", None))
        self.Time.setText(QCoreApplication.translate("GameWindow", u"Your time", None))
        self.SetTime.setText(QCoreApplication.translate("GameWindow", u"Set time", None))
    # retranslateUi


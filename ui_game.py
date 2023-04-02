# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_game.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.resize(600, 633)
        self.RandomPicture = QLabel(GameWindow)
        self.RandomPicture.setObjectName(u"RandomPicture")
        self.RandomPicture.setGeometry(QRect(30, 80, 530, 334))
        self.RandomPicture.setAutoFillBackground(False)
        self.RandomPicture.setStyleSheet(u"border: 5px solid #66CDAA;")
        self.RandomPicture.setScaledContents(True)
        self.RandomPicture.setWordWrap(True)
        self.RandomWord = QLabel(GameWindow)
        self.RandomWord.setObjectName(u"RandomWord")
        self.RandomWord.setGeometry(QRect(30, 420, 530, 66))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        font.setItalic(False)
        self.RandomWord.setFont(font)
        self.RandomWord.setAutoFillBackground(False)
        self.RandomWord.setStyleSheet(u"background: #20B2AA;\n"
"border: 3px solid #66CDAA;\n"
"border-radius: 10px;\n"
"\n"
"font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 36px;\n"
"line-height: 44px;\n"
"/* identical to box height */\n"
"\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.RandomWord.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Back = QPushButton(GameWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(30, 560, 170, 50))
        self.Back.setFont(font)
        self.Back.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.NextWord = QPushButton(GameWindow)
        self.NextWord.setObjectName(u"NextWord")
        self.NextWord.setGeometry(QRect(210, 560, 170, 50))
        self.NextWord.setFont(font)
        self.NextWord.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.StartTimer = QPushButton(GameWindow)
        self.StartTimer.setObjectName(u"StartTimer")
        self.StartTimer.setGeometry(QRect(30, 500, 170, 50))
        self.StartTimer.setFont(font)
        self.StartTimer.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.Time = QLabel(GameWindow)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(320, 20, 240, 56))
        self.Time.setFont(font)
        self.Time.setStyleSheet(u"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 25px;\n"
"\n"
"font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 30px;\n"
"line-height: 150%;\n"
"text-align: center;\n"
"letter-spacing: -0.022em;\n"
"color: #FFFFFF;")
        self.Time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.SetTime = QPushButton(GameWindow)
        self.SetTime.setObjectName(u"SetTime")
        self.SetTime.setGeometry(QRect(210, 500, 170, 50))
        self.SetTime.setFont(font)
        self.SetTime.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.label = QLabel(GameWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 240, 56))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 25px;\n"
"\n"
"font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 40px;\n"
"line-height: 150%;\n"
"text-align: center;\n"
"letter-spacing: -0.022em;\n"
"color: #FFFFFF;")
        self.StopTimer = QPushButton(GameWindow)
        self.StopTimer.setObjectName(u"StopTimer")
        self.StopTimer.setGeometry(QRect(390, 560, 170, 50))
        self.StopTimer.setFont(font)
        self.StopTimer.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.ResetTimer = QPushButton(GameWindow)
        self.ResetTimer.setObjectName(u"ResetTimer")
        self.ResetTimer.setGeometry(QRect(390, 500, 170, 50))
        self.ResetTimer.setFont(font)
        self.ResetTimer.setStyleSheet(u"QPushButton {\n"
"background: #2CB67D;\n"
"border: 4px solid #66CDAA;\n"
"border-radius: 21px;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #66CDAB;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background: #2CB67D;\n"
"    }\n"
"\n"
"QPushButton\n"
"{\n"
" font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 26px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.frame = QFrame(GameWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 601, 634))
        self.frame.setStyleSheet(u"border: 9px solid #66CDAA;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.RandomPicture.raise_()
        self.RandomWord.raise_()
        self.Back.raise_()
        self.NextWord.raise_()
        self.StartTimer.raise_()
        self.Time.raise_()
        self.SetTime.raise_()
        self.label.raise_()
        self.StopTimer.raise_()
        self.ResetTimer.raise_()

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"Crocodile!", None))
        self.RandomPicture.setText("")
        self.RandomWord.setText(QCoreApplication.translate("GameWindow", u"Your word:", None))
        self.Back.setText(QCoreApplication.translate("GameWindow", u"Back", None))
        self.NextWord.setText(QCoreApplication.translate("GameWindow", u"Next word", None))
        self.StartTimer.setText(QCoreApplication.translate("GameWindow", u"Start", None))
        self.Time.setText(QCoreApplication.translate("GameWindow", u"Time:", None))
        self.SetTime.setText(QCoreApplication.translate("GameWindow", u"Set time", None))
        self.label.setText(QCoreApplication.translate("GameWindow", u"Score: ", None))
        self.StopTimer.setText(QCoreApplication.translate("GameWindow", u"Guessed", None))
        self.ResetTimer.setText(QCoreApplication.translate("GameWindow", u"Reset", None))
    # retranslateUi


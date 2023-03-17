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
        GameWindow.resize(414, 383)
        self.RandomPicture = QLabel(GameWindow)
        self.RandomPicture.setObjectName(u"RandomPicture")
        self.RandomPicture.setGeometry(QRect(78, 29, 251, 101))
        self.RandomWord = QLabel(GameWindow)
        self.RandomWord.setObjectName(u"RandomWord")
        self.RandomWord.setGeometry(QRect(78, 249, 271, 41))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(20)
        self.RandomWord.setFont(font)
        self.Back = QPushButton(GameWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(62, 310, 142, 41))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(14)
        self.Back.setFont(font1)
        self.NextWord = QPushButton(GameWindow)
        self.NextWord.setObjectName(u"NextWord")
        self.NextWord.setGeometry(QRect(210, 310, 141, 41))
        self.NextWord.setFont(font1)

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"Crocodile!", None))
        self.RandomPicture.setText("")
        self.RandomWord.setText("")
        self.Back.setText(QCoreApplication.translate("GameWindow", u"Back", None))
        self.NextWord.setText(QCoreApplication.translate("GameWindow", u"Next word", None))
    # retranslateUi


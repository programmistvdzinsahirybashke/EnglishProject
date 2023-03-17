# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(411, 382)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 281, 51))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.SettingsButton = QPushButton(self.centralwidget)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(80, 290, 241, 45))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(20)
        self.SettingsButton.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 90, 241, 131))
        self.label_2.setPixmap(QPixmap("top_logo.png"))
        self.label_2.setScaledContents(True)
        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(80, 230, 241, 45))
        self.StartButton.setFont(font1)
        self.StartButton.setAutoDefault(False)
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"Crocodile!", None))
        self.label.setText(QCoreApplication.translate("StartWindow", u"Crocodile!", None))
        self.SettingsButton.setText(QCoreApplication.translate("StartWindow", u"Settings", None))
        self.label_2.setText("")
        self.StartButton.setText(QCoreApplication.translate("StartWindow", u"Start!", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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
    QRadioButton, QSizePolicy, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(411, 382)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        SettingsWindow.setFont(font)
        self.S = QLabel(SettingsWindow)
        self.S.setObjectName(u"S")
        self.S.setGeometry(QRect(130, 10, 201, 61))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.S.setFont(font1)
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 131, 41))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(20)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setMidLineWidth(1)
        self.Back = QPushButton(SettingsWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(130, 270, 142, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(14)
        self.Back.setFont(font3)
        self.radioButtonSetWhite = QRadioButton(SettingsWindow)
        self.radioButtonSetWhite.setObjectName(u"radioButtonSetWhite")

        self.radioButtonSetWhite.setGeometry(QRect(150, 100, 71, 20))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(12)
        self.radioButtonSetWhite.setFont(font4)
        self.radioButtonSetGreen = QRadioButton(SettingsWindow)
        self.radioButtonSetGreen.setObjectName(u"radioButtonSetGreen")
        self.radioButtonSetGreen.setGeometry(QRect(240, 100, 71, 20))
        self.radioButtonSetGreen.setFont(font4)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.S.setText(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Theme :", None))
        self.Back.setText(QCoreApplication.translate("SettingsWindow", u"Back", None))
        self.radioButtonSetWhite.setText(QCoreApplication.translate("SettingsWindow", u"White", None))
        self.radioButtonSetGreen.setText(QCoreApplication.translate("SettingsWindow", u"Green", None))
    # retranslateUi


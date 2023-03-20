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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(540, 600)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        SettingsWindow.setFont(font)
        self.S = QLabel(SettingsWindow)
        self.S.setObjectName(u"S")
        self.S.setGeometry(QRect(140, 90, 271, 81))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(44)
        font1.setBold(True)
        font1.setItalic(False)
        self.S.setFont(font1)
        self.S.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 240, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.label.setMidLineWidth(1)
        self.Back = QPushButton(SettingsWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(60, 440, 210, 60))
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(16)
        self.Back.setFont(font3)
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
        self.radioButtonSetGreen = QRadioButton(SettingsWindow)
        self.radioButtonSetGreen.setObjectName(u"radioButtonSetGreen")
        self.radioButtonSetGreen.setGeometry(QRect(250, 240, 121, 41))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(24)
        self.radioButtonSetGreen.setFont(font4)
        self.radioButtonSetGreen.setStyleSheet(u"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.radioButtonSetDark = QRadioButton(SettingsWindow)
        self.radioButtonSetDark.setObjectName(u"radioButtonSetDark")
        self.radioButtonSetDark.setGeometry(QRect(370, 240, 101, 41))
        self.radioButtonSetDark.setFont(font4)
        self.radioButtonSetDark.setStyleSheet(u"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.label_2 = QLabel(SettingsWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 330, 171, 41))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(28)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.label_2.setMidLineWidth(1)
        self.radioButtonSetTimeMInuteThirty = QRadioButton(SettingsWindow)
        self.radioButtonSetTimeMInuteThirty.setObjectName(u"radioButtonSetTimeMInuteThirty")
        self.radioButtonSetTimeMInuteThirty.setGeometry(QRect(290, 330, 81, 41))
        self.radioButtonSetTimeMInuteThirty.setFont(font4)
        self.radioButtonSetTimeMInuteThirty.setStyleSheet(u"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.radioButtonSetTimeMInute = QRadioButton(SettingsWindow)
        self.radioButtonSetTimeMInute.setObjectName(u"radioButtonSetTimeMInute")
        self.radioButtonSetTimeMInute.setGeometry(QRect(200, 330, 81, 41))
        self.radioButtonSetTimeMInute.setFont(font4)
        self.radioButtonSetTimeMInute.setStyleSheet(u"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.frame_5 = QFrame(SettingsWindow)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(60, 320, 420, 61))
        self.frame_5.setStyleSheet(u"    border: 2px solid  rgb(102,205,170);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(SettingsWindow)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(60, 230, 420, 61))
        self.frame_7.setStyleSheet(u"    border: 2px solid  rgb(102,205,170);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.radioButtonSetTimeTwoMinutes = QRadioButton(SettingsWindow)
        self.radioButtonSetTimeTwoMinutes.setObjectName(u"radioButtonSetTimeTwoMinutes")
        self.radioButtonSetTimeTwoMinutes.setGeometry(QRect(380, 330, 91, 41))
        self.radioButtonSetTimeTwoMinutes.setFont(font4)
        self.radioButtonSetTimeTwoMinutes.setStyleSheet(u"QRadioButton::indicator::unchecked{ \n"
"border: 1px solid; \n"
"border-color: rgb(132,132,132);\n"
"border-radius: 5px;\n"
"background-color: white; \n"
"width: 11px; \n"
"height: 11px; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: white;\n"
"border-radius: 6px;\n"
"background-color: rgb(0,116,188); \n"
"width: 7px; \n"
"height: 7px; \n"
"}")
        self.RestoreSettings = QPushButton(SettingsWindow)
        self.RestoreSettings.setObjectName(u"RestoreSettings")
        self.RestoreSettings.setGeometry(QRect(280, 440, 210, 60))
        self.RestoreSettings.setFont(font3)
        self.RestoreSettings.setStyleSheet(u"QPushButton {\n"
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
        self.frame_7.raise_()
        self.frame_5.raise_()
        self.S.raise_()
        self.label.raise_()
        self.Back.raise_()
        self.radioButtonSetGreen.raise_()
        self.radioButtonSetDark.raise_()
        self.label_2.raise_()
        self.radioButtonSetTimeMInuteThirty.raise_()
        self.radioButtonSetTimeMInute.raise_()
        self.radioButtonSetTimeTwoMinutes.raise_()
        self.RestoreSettings.raise_()

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.S.setText(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Theme :", None))
        self.Back.setText(QCoreApplication.translate("SettingsWindow", u"Back", None))
        self.radioButtonSetGreen.setText(QCoreApplication.translate("SettingsWindow", u"Green", None))
        self.radioButtonSetDark.setText(QCoreApplication.translate("SettingsWindow", u"Gray", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Time :", None))
        self.radioButtonSetTimeMInuteThirty.setText(QCoreApplication.translate("SettingsWindow", u"1:30", None))
        self.radioButtonSetTimeMInute.setText(QCoreApplication.translate("SettingsWindow", u"1:00", None))
        self.radioButtonSetTimeTwoMinutes.setText(QCoreApplication.translate("SettingsWindow", u"2:00", None))
        self.RestoreSettings.setText(QCoreApplication.translate("SettingsWindow", u"Restore settings", None))
    # retranslateUi


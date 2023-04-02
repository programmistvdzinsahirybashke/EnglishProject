# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(540, 516)
        SettingsWindow.setMinimumSize(QSize(540, 516))
        SettingsWindow.setMaximumSize(QSize(540, 516))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        SettingsWindow.setFont(font)
        self.S = QLabel(SettingsWindow)
        self.S.setObjectName(u"S")
        self.S.setGeometry(QRect(50, 10, 451, 121))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setBold(True)
        font1.setItalic(False)
        self.S.setFont(font1)
        self.S.setStyleSheet(u"QLabel {  font-family: 'Montserrat';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 90px;\n"
"line-height: 150%;\n"
"/* or 135px */\n"
"\n"
"text-align: center;\n"
"letter-spacing: -0.022em;\n"
"\n"
"color: #2CB67D; }")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 160, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.label.setMidLineWidth(1)
        self.radioButtonSetGreen = QRadioButton(SettingsWindow)
        self.radioButtonSetGreen.setObjectName(u"radioButtonSetGreen")
        self.radioButtonSetGreen.setGeometry(QRect(245, 160, 121, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(24)
        self.radioButtonSetGreen.setFont(font3)
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
        self.radioButtonSetDark.setGeometry(QRect(375, 160, 101, 41))
        self.radioButtonSetDark.setFont(font3)
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
        self.label_2.setGeometry(QRect(60, 250, 171, 41))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.label_2.setMidLineWidth(1)
        self.radioButtonSetTimeMInuteThirty = QRadioButton(SettingsWindow)
        self.radioButtonSetTimeMInuteThirty.setObjectName(u"radioButtonSetTimeMInuteThirty")
        self.radioButtonSetTimeMInuteThirty.setGeometry(QRect(295, 250, 81, 41))
        self.radioButtonSetTimeMInuteThirty.setFont(font3)
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
        self.radioButtonSetTimeMInute.setGeometry(QRect(205, 250, 81, 41))
        self.radioButtonSetTimeMInute.setFont(font3)
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
        self.frame_5.setGeometry(QRect(50, 240, 440, 61))
        self.frame_5.setStyleSheet(u"border: 3px solid #66CDAA;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(SettingsWindow)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(50, 150, 440, 61))
        self.frame_7.setStyleSheet(u"border: 3px solid #66CDAA;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.radioButtonSetTimeTwoMinutes = QRadioButton(SettingsWindow)
        self.radioButtonSetTimeTwoMinutes.setObjectName(u"radioButtonSetTimeTwoMinutes")
        self.radioButtonSetTimeTwoMinutes.setGeometry(QRect(380, 250, 91, 41))
        self.radioButtonSetTimeTwoMinutes.setFont(font3)
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
        self.Back = QPushButton(SettingsWindow)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(50, 410, 229, 50))
        self.Back.setFont(font1)
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
"font-size: 22px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.RestoreSettings = QPushButton(SettingsWindow)
        self.RestoreSettings.setObjectName(u"RestoreSettings")
        self.RestoreSettings.setGeometry(QRect(290, 410, 201, 50))
        self.RestoreSettings.setFont(font1)
        self.RestoreSettings.setStyleSheet(u"QPushButton {\n"
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
"font-size: 22px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.frame = QFrame(SettingsWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 541, 517))
        self.frame.setStyleSheet(u"border: 9px solid #66CDAA;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.frame_7.raise_()
        self.frame_5.raise_()
        self.S.raise_()
        self.label.raise_()
        self.radioButtonSetGreen.raise_()
        self.radioButtonSetDark.raise_()
        self.label_2.raise_()
        self.radioButtonSetTimeMInuteThirty.raise_()
        self.radioButtonSetTimeMInute.raise_()
        self.radioButtonSetTimeTwoMinutes.raise_()
        self.Back.raise_()
        self.RestoreSettings.raise_()

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.S.setText(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Theme :", None))
        self.radioButtonSetGreen.setText(QCoreApplication.translate("SettingsWindow", u"Green", None))
        self.radioButtonSetDark.setText(QCoreApplication.translate("SettingsWindow", u"Gray", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Time :", None))
        self.radioButtonSetTimeMInuteThirty.setText(QCoreApplication.translate("SettingsWindow", u"1:30", None))
        self.radioButtonSetTimeMInute.setText(QCoreApplication.translate("SettingsWindow", u"1:00", None))
        self.radioButtonSetTimeTwoMinutes.setText(QCoreApplication.translate("SettingsWindow", u"2:00", None))
        self.Back.setText(QCoreApplication.translate("SettingsWindow", u"Save and go back", None))
        self.RestoreSettings.setText(QCoreApplication.translate("SettingsWindow", u"Restore settings", None))
    # retranslateUi


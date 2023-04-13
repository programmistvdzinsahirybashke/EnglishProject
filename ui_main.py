# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(540, 516)
        StartWindow.setMinimumSize(540, 516)
        StartWindow.setMaximumSize(540, 516)
        font = QFont()
        font.setStrikeOut(False)
        StartWindow.setFont(font)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 491, 81))
        font1 = QFont()
        font1.setFamilies([u"Montserrat ExtraBold"])
        font1.setPointSize(60)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 541, 517))
        self.frame.setStyleSheet(u"border: 9px solid #66CDAA;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.SettingsButton = QPushButton(self.frame)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(40, 430, 150, 50))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 254, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(44, 182, 125, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 254, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.SettingsButton.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.SettingsButton.setFont(font2)
        self.SettingsButton.setStyleSheet(u"QPushButton {\n"
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
        self.StartButton = QPushButton(self.frame)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(200, 430, 150, 50))
        self.StartButton.setFont(font2)
        self.StartButton.setAcceptDrops(False)
        self.StartButton.setStyleSheet(u"QPushButton {\n"
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
"font-size: 28px;\n"
"line-height: 29px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFE;\n"
"}")
        self.StartButton.setAutoDefault(False)
        self.ExitButton = QPushButton(self.frame)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(360, 430, 150, 50))
        self.ExitButton.setFont(font2)
        self.ExitButton.setAcceptDrops(False)
        self.ExitButton.setStyleSheet(u"QPushButton {\n"
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
        self.ExitButton.setAutoDefault(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap("media/top_logo.png"))
        self.label_2.setGeometry(QRect(30, 80, 480, 340))
        self.label_2.setScaledContents(True)
        StartWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"Crocodile!", None))
        self.label.setText(QCoreApplication.translate("StartWindow", u"Crocodile!", None))
        self.SettingsButton.setText(QCoreApplication.translate("StartWindow", u"Settings", None))
        self.StartButton.setText(QCoreApplication.translate("StartWindow", u"Start!", None))
        self.ExitButton.setText(QCoreApplication.translate("StartWindow", u"Exit", None))
        self.label_2.setText("")
    # retranslateUi


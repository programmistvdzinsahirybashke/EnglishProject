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
        StartWindow.resize(412, 382)
        font = QFont()
        font.setStrikeOut(False)
        StartWindow.setFont(font)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 291, 51))
        font1 = QFont()
        font1.setFamilies([u"Montserrat ExtraBold"])
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {  color : rgb(0, 170, 127); }")
        self.SettingsButton = QPushButton(self.centralwidget)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(80, 290, 251, 45))
        palette = QPalette()
        brush = QBrush(QColor(120, 120, 120, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(3, 255, 150, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 128))
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
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.SettingsButton.setFont(font2)
        self.SettingsButton.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 1px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(3, 255, 150);\n"
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
"   color:rgb(120,120,120);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap("top_logo.png"))
        self.label_2.setGeometry(QRect(80, 90, 251, 131))
        self.label_2.setScaledContents(True)
        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(80, 230, 251, 45))
        self.StartButton.setFont(font2)
        self.StartButton.setAcceptDrops(False)
        self.StartButton.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 1px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(3, 255, 150);\n"
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
"   color:rgb(120,120,120);\n"
"}")
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
        self.StartButton.setText(QCoreApplication.translate("StartWindow", u"Start", None))
    # retranslateUi


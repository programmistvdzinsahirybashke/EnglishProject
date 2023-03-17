import sys
from PySide6 import QtWidgets
from ui_main import *
from ui_game import *
from ui_settings import *


class CrocodileGame(QMainWindow):
    def __init__(self):
        super(CrocodileGame, self).__init__()
        self.main_window = Ui_StartWindow()
        self.main_window.setupUi(self)
        self.setWindowIcon(QIcon('top_logo.png'))
        self.main_window.StartButton.clicked.connect(self.open_game_window)
        self.main_window.SettingsButton.clicked.connect(self.open_settings_window)

    def open_main_window(self):
        self.new_window.hide()
        self.show()

    def open_game_window(self):
        self.hide()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_GameWindow()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.new_window.show()

    def open_settings_window(self):
        self.hide()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_SettingsWindow()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.new_window.show()
        self.ui_window.radioButtonSetWhite.toggled.connect(self.on_clicked)
        self.ui_window.radioButtonSetGreen.toggled.connect(self.on_clicked)

    def on_clicked(self):
        if self.sender().isChecked():
            color = self.sender().text()
            self.setStyleSheet(f'background-color: {color};')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrocodileGame()
    window.show()

    sys.exit(app.exec())

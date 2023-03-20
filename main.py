import sqlite3
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui_main import *
from ui_game import *
from ui_settings import *

conn = sqlite3.connect('db/words.db', check_same_thread=False)
cursor = conn.cursor()

word_count = []
used_words = []

def count_words_in_table():
    cursor.execute("SELECT * FROM allwords")
    all = cursor.fetchall()

    for row in all:
        word_count.append(row[0])

    print(f'В базе данных {len(word_count)} слов')

count_words_in_table()


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
        used_words.clear()
        self.show()

    def create_new_window(self, page):
        self.hide()
        self.new_window = QtWidgets.QWidget()
        self.ui_window = page()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.new_window.setWindowIcon(QIcon('top_logo.png'))
        self.new_window.show()

    def open_game_window(self):
        self.create_new_window(Ui_GameWindow)
        self.select_random_word()
        self.ui_window.NextWord.clicked.connect(self.get_next_word)

    def open_settings_window(self):
        self.create_new_window(Ui_SettingsWindow)

        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.ui_window.radioButtonSetGreen.toggled.connect(self.set_green_theme)
        self.ui_window.radioButtonSetDark.toggled.connect(self.set_dark_theme)
        self.ui_window.RestoreSettings.clicked.connect(self.restore_setting)

    def set_green_theme(self):
        color = "#66CDAA"
        app.setStyleSheet(f'QWidget {{background-color: {color};}}')

    def set_dark_theme(self):
        color = "#baedff"
        app.setStyleSheet(f'QWidget {{background-color: {color};}}')

    def restore_setting(self):
        color = "#f0f0f0"
        app.setStyleSheet(f'QWidget {{background-color: {color};}}')

    def select_random_word(self):
        cursor.execute("SELECT * FROM allwords ORDER BY RANDOM() LIMIT 1")
        record = cursor.fetchall()

        for row in record:
            random_word = row[1]
            random_picture = QPixmap()
            random_picture.loadFromData(row[2])

            self.ui_window.RandomWord.setText(f'{random_word}')
            self.ui_window.RandomPicture.setPixmap(random_picture)
            used_words.append(random_word)

    def get_next_word(self):
        print(used_words, word_count)
        cursor.execute("SELECT * FROM allwords ORDER BY RANDOM() LIMIT 1")
        record = cursor.fetchall()

        for row in record:
            random_word = row[1]
            random_picture = QPixmap()
            random_picture.loadFromData(row[2])

            self.ui_window.RandomWord.setText(f'{random_word}')
            self.ui_window.RandomPicture.setPixmap(random_picture)
            if random_word in used_words:
                pass
            else:
                used_words.append(random_word)

        if len(used_words) == len(word_count):
            for row in record:
                random_word = row[1]

                random_picture = QPixmap()
                random_picture.loadFromData(row[2])

                self.ui_window.RandomWord.setText(f'{random_word}')
                self.ui_window.RandomPicture.setPixmap(random_picture)

            QMessageBox.about(self, "Game over!", "The database out of words :(")
            self.ui_window.NextWord.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CrocodileGame()
    window.show()

    sys.exit(app.exec())

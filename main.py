import sqlite3
import sys

import qdarktheme
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QInputDialog

from ui_main import *
from ui_game import *
from ui_settings import *

# Creating connection with database
conn = sqlite3.connect('db/words.db')
cursor = conn.cursor()

word_count = []
used_words = []
time = [300]
score = []

# Counting words in the database (table)
cursor.execute("SELECT * FROM allwords")
all_words = cursor.fetchall()
for row in all_words:
    word_count.append(row[0])

print(f'There are {len(word_count)} words in the database')


class CrocodileGame(QMainWindow):
    def __init__(self):
        super(CrocodileGame, self).__init__()
        self.ui_window = None
        self.new_window = None
        self.main_window = Ui_StartWindow()
        self.main_window.setupUi(self)
        self.setWindowIcon(QIcon('media/top_logo.png'))
        self.main_window.StartButton.clicked.connect(self.open_game_window)
        self.main_window.SettingsButton.clicked.connect(self.open_settings_window)
        self.main_window.ExitButton.clicked.connect(self.exit)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

    # Creating and opening start window
    def open_main_window(self):
        self.new_window.hide()
        self.ui_window.start = False
        used_words.clear()
        self.show()

    # Creating a new window
    def create_new_window(self, page):
        self.hide()
        self.new_window = QtWidgets.QWidget()
        self.ui_window = page()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.new_window.setWindowIcon(QIcon('media/top_logo.png'))
        self.new_window.show()

    # Creating and opening game window
    def open_game_window(self):
        score.clear()
        self.create_new_window(Ui_GameWindow)
        self.ui_window.label.setText("Score: " + '0')

        cursor.execute("SELECT * FROM allwords ORDER BY RANDOM() LIMIT 1")
        record = cursor.fetchall()
        for row in record:
            random_word = "Your word: " + row[1]
            random_picture = QPixmap()
            random_picture.loadFromData(row[2])

            self.ui_window.RandomWord.setText(random_word)
            self.ui_window.RandomPicture.setPixmap(random_picture)
            used_words.append(random_word)

        self.ui_window.NextWord.clicked.connect(self.get_next_word)
        self.ui_window.SetTime.clicked.connect(self.set_time)
        self.ui_window.StartTimer.clicked.connect(self.start_timer)
        self.ui_window.StopTimer.clicked.connect(self.stop_timer)
        self.ui_window.ResetTimer.clicked.connect(self.reset_timer)

        self.ui_window.start = False
        self.ui_window.StopTimer.setEnabled(False)
        self.ui_window.ResetTimer.setEnabled(False)
        self.ui_window.count = time[0]
        self.ui_window.Time.setText("Time: " + str(time[0]/10) + ' s')

    # Retreive a random word from the database and check if the words are finished
    def get_next_word(self):
        self.ui_window.StopTimer.setEnabled(False)
        self.ui_window.ResetTimer.setEnabled(False)
        self.ui_window.count = time[0]
        self.ui_window.Time.setText("Time: " + str(time[0]/10) + ' s')

        cursor.execute("SELECT * FROM allwords ORDER BY RANDOM() LIMIT 1")
        record = cursor.fetchall()
        for row in record:
            random_word = "Your word: " + row[1]
            random_picture = QPixmap()
            random_picture.loadFromData(row[2])

            if random_word in used_words and len(used_words) != len(word_count):
                self.ui_window.NextWord.click()
            elif random_word not in used_words and len(used_words) != len(word_count):
                self.ui_window.RandomWord.setText(random_word)
                self.ui_window.RandomPicture.setPixmap(random_picture)
                if random_word not in used_words:
                    used_words.append(random_word)
            if len(used_words) == len(word_count):
                self.ui_window.NextWord.setEnabled(False)

    # Timer controllers
    def update_time(self):
        # checking if flag is true
        if self.ui_window.start:
            # incrementing the counter
            self.ui_window.StopTimer.setEnabled(True)
            self.ui_window.ResetTimer.setEnabled(True)
            self.ui_window.count -= 1
            # getting text from count
            text = "Time: " + str(self.ui_window.count / 10) + " s"
            # showing text
            self.ui_window.Time.setText(text)
            # timer is completed
            if self.ui_window.count == 0 and len(used_words) != len(word_count):
                # making flag false
                self.ui_window.start = False
                self.ui_window.StopTimer.setEnabled(False)
                self.ui_window.ResetTimer.setEnabled(False)
                self.enable_buttons()

                # Creating dialog window and asking if players guessed the word
                dlg = QMessageBox(self)
                dlg.setStyleSheet("QLabel {font-size: 18px; }")
                dlg.setWindowTitle("Time out!")
                dlg.setText("The word is guessed?")
                dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                button = dlg.exec()
                if button == QMessageBox.Yes:
                    score.append(1)
                    self.ui_window.label.setText("Score: " + str(sum(score)))
                    self.ui_window.NextWord.click()
                elif button == QMessageBox.No:
                    self.ui_window.NextWord.click()

            elif self.ui_window.count != 0 and len(used_words) == len(word_count):
                self.ui_window.StopTimer.setEnabled(False)
            elif self.ui_window.count == 0 and len(used_words) == len(word_count):
                self.ui_window.start = False
                dlg = QMessageBox(self)
                dlg.setStyleSheet("QLabel {font-size: 18px; }")
                dlg.setWindowTitle("Time out!")
                dlg.setText("The word is guessed?")
                dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                button = dlg.exec()
                if button == QMessageBox.Yes:
                    score.append(1)
                    self.ui_window.label.setText("Score: " + str(sum(score)))

                QMessageBox.about(self, "Game over!", "<font>" "<p style='font-size: 26px'>"
                                                      "The database out of words :( </p>")
                print(used_words, word_count)
                self.disable_all_buttons()

    def set_time(self):
        # making flag false
        self.ui_window.start = False
        # getting seconds and flag from user
        second, done = QInputDialog.getInt(self, 'Setting time', 'Enter Seconds:')

        while second <= 0 and done:
            second, done = QInputDialog.getInt(self, 'Setting time', 'Time must be more then 0:')
        if second > 0 and done:
            # changing the value of count
            self.ui_window.count = second * 10
            time.clear()
            time.append(second * 10)
            # setting text to the label
            self.ui_window.Time.setText("Time: " + str(time[0]/10) + ' s')
        else:
            self.ui_window.Time.setText("Time: " + str(time[0]/10) + ' s')

    def start_timer(self):
        # making flag true
        self.ui_window.start = True
        self.timer.start(100)

        if self.ui_window.count != 0:
            self.disable_buttons()
        elif self.ui_window.count == 0:
            self.ui_window.start = False

    def stop_timer(self):
        self.ui_window.start = False
        dlg = QMessageBox(self)
        dlg.setStyleSheet("QLabel {font-size: 18px; }")
        dlg.setWindowTitle("Stop timer")
        dlg.setText("The word is guessed?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No |
                               QMessageBox.StandardButton.Cancel)

        button = dlg.exec()
        if button == QMessageBox.Yes:
            score.append(1)
            self.ui_window.label.setText("Score: " + str(sum(score)))
            self.enable_buttons()
            self.ui_window.NextWord.click()
        elif button == QMessageBox.No:
            self.enable_buttons()
            self.ui_window.NextWord.click()
        elif button == QMessageBox.Cancel:
            self.ui_window.start = True

    def reset_timer(self):
        self.ui_window.start = False
        dlg = QMessageBox(self)
        dlg.setStyleSheet("QLabel {font-size: 18px; }")
        dlg.setWindowTitle("Reset timer")
        dlg.setText("You want to reset timer?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.ui_window.count = time[0]
            self.ui_window.Time.setText("Time: " + str(self.ui_window.count / 10) + ' s')
            self.ui_window.StopTimer.setEnabled(False)
            self.ui_window.StartTimer.setEnabled(True)
            self.ui_window.SetTime.setEnabled(True)
            self.ui_window.NextWord.setEnabled(True)
            self.ui_window.ResetTimer.setEnabled(False)
        elif button == QMessageBox.No:
            self.ui_window.start = True

    # Creating and opening settings window
    def open_settings_window(self):
        self.create_new_window(Ui_SettingsWindow)
        self.ui_window.start = None

        self.ui_window.Back.clicked.connect(self.open_main_window)
        self.ui_window.radioButtonSetGreen.toggled.connect(self.set_green_theme)
        self.ui_window.radioButtonSetDark.toggled.connect(self.set_dark_theme)
        self.ui_window.RestoreSettings.clicked.connect(self.restore_setting)
        self.ui_window.radioButtonSetTimeMInute.toggled.connect(self.set_minute)
        self.ui_window.radioButtonSetTimeMInuteThirty.toggled.connect(self.set_minute_thirty)
        self.ui_window.radioButtonSetTimeTwoMinutes.toggled.connect(self.set_two_minutes)

    def set_dark_theme(self):
        self.main_window.label.setGeometry(QRect(30, 30, 491, 81))
        self.main_window.label_2.setGeometry(QRect(30, 80, 480, 340))
        qdarktheme.setup_theme(custom_colors={"primary": "#66CDAA"})

    def restore_setting(self):
        self.main_window.label.setGeometry(QRect(30, 30, 491, 81))
        self.main_window.label_2.setGeometry(QRect(30, 80, 480, 340))
        qdarktheme.setup_theme("light", custom_colors={"primary": "#66CDAA"})
        time.clear()
        time.append(300)

    def set_green_theme(self):
        self.main_window.label_2.setGeometry(QRect(20, 120, 500, 289))
        self.main_window.label.setGeometry(QRect(60, 30, 491, 81))
        color = "#1e997c"
        app.setStyleSheet(f'QWidget {{background-color: {color}; color: white;}}'
                          "QPushButton {\n"
                          "width : 100px; \n"
                          "    color: #333;\n"
                          "    border: 2px solid white;\n"
                          "    border-radius: 15px;\n"
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

    def set_minute(self):
        time.clear()
        time.append(600)

    def set_minute_thirty(self):
        time.clear()
        time.append(900)

    def set_two_minutes(self):
        time.clear()
        time.append(1200)

    def disable_buttons(self):
        self.ui_window.NextWord.setEnabled(False)
        self.ui_window.StartTimer.setEnabled(False)
        self.ui_window.SetTime.setEnabled(False)

    def enable_buttons(self):
        self.ui_window.NextWord.setEnabled(True)
        self.ui_window.StartTimer.setEnabled(True)
        self.ui_window.SetTime.setEnabled(True)

    def disable_all_buttons(self):
        self.ui_window.NextWord.setEnabled(False)
        self.ui_window.SetTime.setEnabled(False)
        self.ui_window.StartTimer.setEnabled(False)
        self.ui_window.StopTimer.setEnabled(False)
        self.ui_window.ResetTimer.setEnabled(False)

    def exit(self):
        dlg = QMessageBox(self)
        dlg.setStyleSheet("QLabel {font-size: 14px; }")
        dlg.setWindowTitle("Exit")
        dlg.setText("Are you sure you want to exit?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        button = dlg.exec()
        if button == QMessageBox.Yes:
            sys.exit(app.exec())
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light", custom_colors={"primary": "#66CDAA"})
    window = CrocodileGame()
    window.show()
    sys.exit(app.exec())

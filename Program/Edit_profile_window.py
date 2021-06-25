import datetime
import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class EditProfile(QMainWindow):
    def __init__(self, home_page, profile):
        super(EditProfile, self).__init__()
        self.data = dict()
        self.home_page = home_page
        self.profile = profile

        loadUi("./new_design/profile.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()
        self.load_data()
        self.load_photo()


    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close_goal_window())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # изменение фото
        self.change_photo.clicked.connect(lambda: self.change_photo_function())
        self.set_default_photo.clicked.connect(lambda: self.set_default_photo_function())
        # сохранение
        self.save.clicked.connect(lambda: self.save_data())


    def change_photo_function(self):
        filename = QFileDialog.getOpenFileName(filter="Image (*.jpg)")[0]
        if os.path.exists(filename):
            self.profile.photo_change(filename)
            pixmap = QtGui.QPixmap(self.profile.get_photo_path())
            self.photo_label.setPixmap(pixmap)

    def set_default_photo_function(self):
        self.profile.data_change('photo_path', './source/default_photo.jpg')
        pixmap = QtGui.QPixmap(self.profile.get_photo_path())
        self.photo_label.setPixmap(pixmap)

    def save_data(self):
        if self.name.text() == "":
            return
        else:
            self.profile.data_change('name', self.name.text())

        self.profile.data_change('gender', self.gender.currentIndex())
        try:
            weight = float(self.weight.text().replace(',', '.'))
            if weight <= 0:
                self.weight.setText("")
                return
            self.profile.data_change('weight', weight)
            if self.birthday.dateTime() > QtCore.QDateTime.currentDateTime():
                self.birthday.setDateTime(QtCore.QDateTime.currentDateTime())
                return
            self.profile.data_change('birthday', self.birthday.dateTime().toString())
            self.home_page.update()
            self.hide()
        except:
            self.weight.setText("")


    def close_goal_window(self):
        self.home_page.update()
        self.hide()

    def load_data(self):
        data = self.profile.get_data_dict()
        self.name.setText(data['name'])
        self.gender.setCurrentIndex(int(data['gender']))
        if data['weight'] is None:
            self.weight.setText("")
        else:
            self.weight.setText(str(data['weight']))
        if data['birthday'] is None:
            self.birthday.setDateTime(QtCore.QDateTime.currentDateTime())
        else:
            self.birthday.setDateTime(QtCore.QDateTime.fromString(data['birthday']))

    def load_photo(self):
        filename = self.profile.get_photo_path()
        if filename is not None:
            pixmap = QtGui.QPixmap(filename)
            self.photo_label.setPixmap(pixmap)

    def moveWindow(self, e):
        if not self.isMaximized():
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditProfile()
    window.show()
    sys.exit(app.exec_())
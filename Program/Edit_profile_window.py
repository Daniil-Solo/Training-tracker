import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class EditProfile(QMainWindow):
    def __init__(self, data_transfer=dict()):
        super(EditProfile, self).__init__()
        self.data_transfer = data_transfer

        loadUi("new_design/profile.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()


    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        #
        self.change_photo.clicked.connect(lambda: self.change_photo_function())
        self.save.clicked.connect(lambda: self.save_data())

    def change_photo_function(self):
        filename = QFileDialog.getOpenFileName(filter="Image (*.jpg)")[0]
        if os.path.exists(filename):
            self.data_transfer['photo_path'] = filename
            new_filename = filename
            pixmap = QtGui.QPixmap(new_filename)
            self.photo_label.setPixmap(pixmap)

    def save_data(self):
        self.data_transfer['name'] = self.name.text()
        self.data_transfer['gender'] = self.gender.currentIndex()
        self.data_transfer['weight'] = self.weight.text()
        self.data_transfer['birthday'] = self.birthday.dateTime().toString()
        print(str(self.data_transfer))

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
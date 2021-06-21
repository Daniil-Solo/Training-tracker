import sys
import os
from PyQt5 import QtSql

from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class NewRecord(QMainWindow):
    def __init__(self, home_page, record_mangager):
        super(NewRecord, self).__init__()
        self.data = dict()
        self.home_page = home_page
        self.record_manager = record_mangager

        loadUi("new_design/new_record.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()


    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close_goal_window())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # сохранение
        self.create.clicked.connect(lambda: self.create_new_record())



    def create_new_record(self):
        w_time1 = self.timeEdit.text()
        w_distance1 = self.distance.text()


        self.close_goal_window()

    def close_goal_window(self):
        self.home_page.update()
        self.hide()


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
    window = NewRecord()
    window.show()
    sys.exit(app.exec_())
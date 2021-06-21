import sys
import os

from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class ViewMyRecords(QMainWindow):
    def __init__(self, home_page, record_manager):
        super(ViewMyRecords, self).__init__()
        self.home_page = home_page
        self.record_manager = record_manager
        self.list_objects = []
        loadUi("new_design/my_records.ui", self)
        self.pack_objects()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()


    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close_goal_window())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # скроллер
        self.verticalScrollBar.valueChanged.connect(self.view_records)
        # кнопки
        for i in range(10):
            share_btn = self.list_objects[i][3]
            share_btn.clicked.connect(lambda: self.share(i))

    def share(self, number):
        pass

    def view_records(self):
        value = self.verticalScrollBar.value()
        print(str(value))

        list_records = self.record_manager.get_list_records()
        n_records = len(list_records)
        

    def pack_objects(self):
        item1 = (self.number_1, self.distance_1, self.time_1, self.share_1)
        item2 = (self.number_2, self.distance_2, self.time_2, self.share_2)
        item3 = (self.number_3, self.distance_3, self.time_3, self.share_3)
        item4 = (self.number_4, self.distance_4, self.time_4, self.share_4)
        item5 = (self.number_5, self.distance_5, self.time_5, self.share_5)
        item6 = (self.number_6, self.distance_6, self.time_6, self.share_6)
        item7 = (self.number_7, self.distance_7, self.time_7, self.share_7)
        item8 = (self.number_8, self.distance_8, self.time_8, self.share_8)
        item9 = (self.number_9, self.distance_9, self.time_9, self.share_9)
        item10 = (self.number_10, self.distance_10, self.time_10, self.share_10)
        self.list_objects = [item1, item2, item3, item4, item5,
                             item6, item7, item8, item9, item10]


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
    window = ViewMyRecords()
    window.show()
    sys.exit(app.exec_())
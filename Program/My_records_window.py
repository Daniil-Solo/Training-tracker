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
        loadUi("new_design/my_records.ui", self)
        self.list_objects = self.pack_objects()
        self.list_records = self.record_manager.get_list_records()
        self.n_records = len(self.list_records)
        self.old_left = 0

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.diactivate_excess_objects(self.n_records)
        self.all_connections()
        self.print_records(0, min(10, self.n_records))

    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close_goal_window())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # скроллер
        self.verticalScrollBar.valueChanged.connect(self.view_records)
        # кнопки
        self.share_1.clicked.connect(lambda: self.share(0))
        self.share_2.clicked.connect(lambda: self.share(1))
        self.share_3.clicked.connect(lambda: self.share(2))
        self.share_4.clicked.connect(lambda: self.share(3))
        self.share_5.clicked.connect(lambda: self.share(4))
        self.share_6.clicked.connect(lambda: self.share(5))
        self.share_7.clicked.connect(lambda: self.share(6))
        self.share_8.clicked.connect(lambda: self.share(7))
        self.share_9.clicked.connect(lambda: self.share(8))
        self.share_10.clicked.connect(lambda: self.share(9))

    def share(self, number):
        print(number)
        index = self.old_left + number
        record = self.list_records[index]
        distance_text = self.get_distance_text(record[0])
        time_text = record[1]
        print(distance_text, time_text)
        # сформировать share

    def view_records(self):
        value = self.verticalScrollBar.value()
        k = int(value * (self.n_records - 1) / 99)
        left, right = self.get_index(k, self.n_records, 10)
        if self.old_left != left:
            self.old_left = left
            self.print_records(left, right)

    @staticmethod
    def get_distance_text(distance_text):
        distance = float(distance_text)
        if distance >= 1000:
            distance = distance / 1000
            distance_text = str(distance) + " км"
        else:
            distance_text = str(distance) + " м"
        return distance_text

    def print_records(self, left, right):
        for i in range(0, right - left):
            record = self.list_records[left + i]
            distance = record[0]
            time = record[1]
            object = self.list_objects[i]
            number_label = object[0]
            number_label.setText(str(left + i))
            distance_label = object[1]
            distance_label.setText(self.get_distance_text(distance))
            time_label = object[2]
            time_label.setText(time)

    @staticmethod
    def get_index(k, n, m):
        if k == 0:
            return 0, m
        elif k == n - 1:
            return n - m, n
        else:
            if k < int(n / 2):
                if k >= int(m / 2):
                    left = k - int(m / 2)
                    right = k + int(m / 2)
                else:
                    left = 0
                    right = m
            elif k > int(n / 2):
                if k <= n - int(m / 2):
                    left = k - int(m / 2)
                    right = k + int(m / 2)
                else:
                    left = n - m
                    right = n
            else:
                left = k - int(m / 2)
                right = k + int(m / 2)
            return left, right

    def diactivate_excess_objects(self, n):
        if n > 10:
            return
        self.verticalScrollBar.setEnabled(False)
        for i in range(n, 10):
            for object in self.list_objects[i]:
                object.hide()

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
        list_objects = [item1, item2, item3, item4, item5,
                        item6, item7, item8, item9, item10]
        return list_objects

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

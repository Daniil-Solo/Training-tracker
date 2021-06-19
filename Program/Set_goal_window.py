import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class SetGoal(QMainWindow):
    def __init__(self, home_page, profile):
        super(SetGoal, self).__init__()
        self.goal = dict()
        self.home_page = home_page
        self.profile = profile

        loadUi("new_design/dream_window.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()

    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.hide())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # сохранение
        self.create_r.clicked.connect(lambda: self.save_wishful_record_as_goal())
        self.create_w.clicked.connect(lambda: self.save_wishful_weight_as_goal())
        self.create_v.clicked.connect(lambda: self.save_wishful_nice_days_as_goal())
        # Рекорд
        self.distantion.textChanged.connect(lambda: self.auto_goal_r())
        self.dist_val.currentTextChanged.connect(lambda: self.auto_goal_r())
        self.time.timeChanged.connect(lambda: self.auto_goal_r())


    def auto_goal_r(self):
        self.goal = dict()
        distance = self.distantion.text()
        is_m = self.dist_val.currentIndex()
        time = self.time.dateTime().time()
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        goal_name = "Преодолеть " + distance + " "
        if is_m:
            goal_name += "м "
        else:
            goal_name += "км "
            distance = float(distance) * 1000
        goal_name += "за "
        if hour:
            goal_name += str(hour) + " часов "
        if minute:
            goal_name += str(minute) + " минут "
        if second:
            goal_name += str(second) + " секунд"
        self.goal['title'] = goal_name
        self.goal['type'] = 'record'
        self.goal['values'] = []
        self.goal['values'].append(time.toString())
        self.goal['values'].append(distance)
        self.goal_name_r.setPlaceholderText(goal_name)


    def save_wishful_record_as_goal(self):
        if self.goal_name_r.text() != "":
            self.goal['title'] = self.goal_name_r.text()

        self.profile.data_change('goal', self.goal)
        self.close_goal_window()

    def save_wishful_weight_as_goal(self):
        pass

    def save_wishful_nice_days_as_goal(self):
        pass

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
    window = SetGoal()
    window.show()
    sys.exit(app.exec_())
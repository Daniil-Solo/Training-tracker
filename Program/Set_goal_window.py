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

        self.r_ready = False
        self.w_ready = False
        self.v_ready = False

        loadUi("new_design/dream_window.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.all_connections()
        self.auto_goal_r()
        self.auto_goal_w()
        self.auto_goal_v()

    def all_connections(self):
        # закрытие окна
        self.close.clicked.connect(lambda: self.close_goal_window())
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
        # Вес
        self.weight.textChanged.connect(lambda: self.auto_goal_w())
        # Посещаемость
        self.nice_days.textChanged.connect(lambda: self.auto_goal_v())

    def auto_goal_r(self):
        self.goal = dict()
        distance = self.distantion.text()
        if distance == "":
            self.goal_name_r.setPlaceholderText("Пожалуйста введите дистанцию")
            self.r_ready = False
            return
        try:
            check_dist = float(distance.replace(',', '.'))
            is_m = self.dist_val.currentIndex()
            time = self.time.dateTime().time()
            hour = time.hour()
            minute = time.minute()
            second = time.second()

            if check_dist <= 0:
                self.goal_name_r.setPlaceholderText("Дистанция должна быть больше 0")
                self.r_ready = False
                return
            if hour == 0 and minute == 0 and second == 0:
                self.goal_name_r.setPlaceholderText("Время должно быть не нулевым")
                self.r_ready = False
                return
            goal_name = "Преодолеть " + distance + " "
            if is_m:
                goal_name += "м "
            else:
                goal_name += "км "
                distance = check_dist * 1000
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
            self.goal['values'].append(check_dist)
            self.goal_name_r.setPlaceholderText(goal_name)
            self.r_ready = True
        except:
            self.distantion.setText("")
            self.r_ready = False
            return


    def auto_goal_w(self):
        self.goal = dict()
        weight = self.weight.text()
        if weight == "":
            self.goal_name_w.setPlaceholderText("Пожалуйста введите вес")
            self.w_ready = False
            return
        try:
            check_weight = float(weight.replace(',', '.'))

            if check_weight <= 0:
                self.goal_name_w.setPlaceholderText("Вес должен быть больше 0")
                self.w_ready = False
                return
            goal_name = "Похудеть до " + weight + " кг"
            self.goal['title'] = goal_name
            self.goal['weight'] = 'record'
            self.goal['values'] = []
            self.goal['values'].append(float(weight.replace(',', '.')))
            self.goal_name_w.setPlaceholderText(goal_name)
            self.w_ready = True
        except:
            self.weight.setText("")
            self.w_ready = False
            return

    def auto_goal_v(self):
        self.goal = dict()
        nice_days = self.nice_days.text()
        if nice_days == "":
            self.goal_name_v.setPlaceholderText("Пожалуйста введите количество дней")
            self.v_ready = False
            return
        try:
            check_days = int(nice_days)

            if check_days <= 0:
                self.goal_name_v.setPlaceholderText("Число дней должно быть больше 0")
                self.v_ready = False
                return
            goal_name = "Заниматься " + nice_days + " дней без пропуска"
            self.goal['title'] = goal_name
            self.goal['weight'] = 'nice_days'
            self.goal['values'] = []
            self.goal['values'].append(nice_days)
            self.goal_name_v.setPlaceholderText(goal_name)
            self.v_ready = True
        except:
            self.nice_days.setText("")
            self.goal_name_v.setPlaceholderText("Число дней должно быть целым")
            self.v_ready = False
            return

    def save_wishful_record_as_goal(self):
        if not self.r_ready:
            return
        if self.goal_name_r.text() != "":
            self.goal['title'] = self.goal_name_r.text()
        self.profile.data_change('goal', self.goal)
        self.close_goal_window()

    def save_wishful_weight_as_goal(self):
        if not self.w_ready:
            return
        if self.goal_name_w.text() != "":
            self.goal['title'] = self.goal_name_w.text()
        self.profile.data_change('goal', self.goal)
        self.close_goal_window()

    def save_wishful_nice_days_as_goal(self):
        if not self.v_ready:
            return
        if self.goal_name_v.text() != "":
            self.goal['title'] = self.goal_name_v.text()
        self.profile.data_change('goal', self.goal)
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
    window = SetGoal()
    window.show()
    sys.exit(app.exec_())
import datetime
import sys
import os
from time import sleep

from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime
import PyQt5
from PyQt5 import QtSql


class NewWorkoutWindow(QMainWindow):
    def __init__(self, home_page, training_manager, profile):
        super(NewWorkoutWindow, self).__init__()
        self.home_page = home_page
        self.training_manager = training_manager
        self.profile = profile
        loadUi("new_design/new_training.ui", self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.dateEdit.setDate(QDate.currentDate())
        self.all_connections()

    def all_connections(self):
        # закрытие окна
        self.close_icon.clicked.connect(lambda: self.close_goal_window())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # создание новой тренировки
        self.create.clicked.connect(lambda: self.cr_new())
        #self.dateEdit.setEnabled(False)

    def cr_new(self):

        w_date1 = self.dateEdit.text()
        w_time1 = self.timeEdit.text()
        w_distance1 = self.distance.text()
        km = w_distance1.replace(',', '.')

        if self.timeEdit.time().second() != 0 or self.timeEdit.time().minute() != 0 or self.timeEdit.time().hour() != 0:
            pass
        else:
            return

        if float(km) == 0.:
            return
        else:
            pass

        time_sec = 0
        time_sec += int(w_time1[0])*60*60 + int(w_time1[2])*10*60 + int(w_time1[3])*60 + int(w_time1[5])*10 + int(w_time1[6])
        c_temp = float(time_sec) / float(km)
        if ((c_temp - (c_temp // 60) * 60) < 10):
            w_temp1 = str(int(c_temp // 60)) + ".0" + str(int((c_temp - (c_temp // 60) * 60)))
        else:
            w_temp1 = str(int(c_temp // 60)) + "." + str(int((c_temp - (c_temp // 60) * 60)))

        w_heart1 = self.heart.text()
        w_description1 = self.description.toPlainText()

        today_train_date = datetime.date(int(w_date1.split('.')[2]), int(w_date1.split('.')[1]), int(w_date1.split('.')[0]))
        last_date = self.training_manager.get_last_date()
        if last_date is None:
            self.profile.data_change('nice_days', 1)
        else:
            last_train_date = datetime.date(int(last_date.split('.')[2]), int(last_date.split('.')[1]), int(last_date.split('.')[0]))
            date_delta = (today_train_date - last_train_date).days
            if date_delta == 1:
                current_nice_days = self.profile.get_data_dict()['nice_days']
                current_nice_days += 1
                self.profile.data_change('nice_days', current_nice_days)

        global cQuery
        cQuery = QtSql.QSqlQuery()
        cQuery.prepare(
            """
            INSERT INTO workout (
                w_date,
                w_time,
                w_distance,
                w_temp,
                w_heart,
                w_description
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """
        )
        cQuery.addBindValue(w_date1)
        cQuery.addBindValue(w_time1)
        cQuery.addBindValue(w_distance1)
        cQuery.addBindValue(w_temp1)
        cQuery.addBindValue(w_heart1)
        cQuery.addBindValue(w_description1)
        cQuery.exec()
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
    window = NewWorkoutWindow()
    window.show()
    sys.exit(app.exec_())
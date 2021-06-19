import sys
import os

from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime
import PyQt5
from PyQt5 import QtSql

class NewWorkoutWindow(QMainWindow):
    def __init__(self):
        super(NewWorkoutWindow, self).__init__()
        loadUi("new_design/new_workout.ui", self)
        self.dateEdit.setDate(QDate.currentDate())
        self.create.clicked.connect(self.cr_new)

    def cr_new(self):

        w_date1 = self.dateEdit.text()
        w_time1 = self.timeEdit.text()
        w_distance1 = self.distance.text()

        time_sec = 0
        time_sec += int(w_time1[0])*60*60 + int(w_time1[2])*10*60 + int(w_time1[3])*60 + int(w_time1[5])*10 + int(w_time1[6])
        km = w_distance1.replace(',','.')
        c_temp = float(time_sec) / float(km)
        if ((c_temp - (c_temp // 60) * 60) < 10):
            w_temp1 = str(int(c_temp // 60)) + ".0" + str(int((c_temp - (c_temp // 60) * 60)))
        else:
            w_temp1 = str(int(c_temp // 60)) + "." + str(int((c_temp - (c_temp // 60) * 60)))

        w_heart1 = self.heart.text()
        w_description1 = self.description.toPlainText()
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

        self.hide()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWorkoutWindow()
    window.show()
    sys.exit(app.exec_())
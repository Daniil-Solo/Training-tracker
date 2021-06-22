import PyQt5
from PyQt5 import QtSql
import math

class TrainingsManager:
    def __init__(self):
        self.n_pages = 0

    def load_database(self):
        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName("source/workout.db")
        conn.open()
        global cQuery
        cQuery = QtSql.QSqlQuery()
        cQuery.exec(
            """
            CREATE TABLE workout(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                w_date TEXT,
                w_time TEXT,
                w_distance REAL,
                w_temp TEXT,
                w_heart INT,
                w_description TEXT
            )
            """
        )
        # открываем таблицу, если её нет, то создаем

    def update_n_pages(self):
        cQuery.exec("SELECT id from workout")
        count_str = 0
        while (cQuery.next()):
            count_str += 1
        self.n_pages = math.ceil(count_str/4)
        # записываем в self.n_pages число записей в таблице, деленное на 4

    def del_workout(self, w_date1, w_time1):
        cQuery.prepare("DELETE FROM workout WHERE w_date=:x and w_time=:y")
        cQuery.bindValue(':x', w_date1)
        cQuery.bindValue(':y', w_time1)
        cQuery.exec()

    def view_workout(self, w_date1, w_time1):
        cQuery.prepare("SELECT w_temp, w_heart, w_description FROM workout WHERE w_date=:x and w_time=:y")
        cQuery.bindValue(':x', w_date1)
        cQuery.bindValue(':y', w_time1)
        cQuery.exec()
        cQuery.next()
        temp = cQuery.value(0)
        heart = cQuery.value(1)
        description = cQuery.value(2)
        return temp, heart, description

    def get_n_page(self):
        #print(self.n_pages)
        cQuery.exec("SELECT id from workout")
        count_str = 0
        while (cQuery.next()):
            count_str += 1

        self.n_pages = math.ceil(count_str / 4)
        return self.n_pages

    def get_last_date(self):
        try:
            cQuery.exec("SELECT w_date from workout ORDER BY w_date")
            while (cQuery.next()):
                last = cQuery.value(0)
            return last
        except:
            return None

    def get_4_trainings(self, page=0):
        # берем из таблицы записи, соответствующие номеру страницы page
        # по умолчанию 0, то есть берется первые 4 недавние тренировки
        # если тренировки нет, то возвращаем для данной тренировки ["Нет информации", "", ""]
        # если тренировка есть, то берем из нее дату, время, дистаницию и возвращаем её в виде списка
        # ниже написано, что должно вернуть в качестве примера
        train1 = ["Нет информации", "", ""]
        train2 = ["Нет информации", "", ""]
        train3 = ["Нет информации", "", ""]
        train4 = ["Нет информации", "", ""]

        cQuery.exec("SELECT w_date, w_time, w_distance from workout ORDER BY w_date")
        page_index = 0
        while (cQuery.next()):
            page_index += 1

        pass_rec = 0
        while(cQuery.previous()):
            if (pass_rec < page * 4):
                pass_rec += 1
                continue

            train1[0] = "Дата: " + cQuery.value(0)
            train1[1] = "Продолжительность: " + cQuery.value(1)
            train1[2] = "Дистанция: " + cQuery.value(2)
            if(cQuery.previous()):
                train2[0] = "Дата: " + cQuery.value(0)
                train2[1] = "Продолжительность: " + cQuery.value(1)
                train2[2] = "Дистанция: " + cQuery.value(2)
                if (cQuery.previous()):
                    train3[0] = "Дата: " + cQuery.value(0)
                    train3[1] = "Продолжительность: " + cQuery.value(1)
                    train3[2] = "Дистанция: " + cQuery.value(2)
                    if (cQuery.previous()):
                        train4[0] = "Дата: " + cQuery.value(0)
                        train4[1] = "Продолжительность: " + cQuery.value(1)
                        train4[2] = "Дистанция: " + cQuery.value(2)

            break

        return [train1, train2, train3, train4]

    def is_page_exist(self, page):
        if (page < 0):
            return False
        elif (page >= self.get_n_page()):
            return False
        else:
            return True
        # проверяет, есть ли данная страница в таблице
        # учесть отрицательные значения
        # возвращает True, False

    def add_new_training(self, data):
        pass
        # создается новая тренировка и добавляется сразу же в базу данных
        # пересчитывается self.n_pages

    def delete_training(self, page, number):
        pass
        # удаляется запись с номером n=page*4 + number
        # страницы и номера тренировок на странице нумеруются с нуля
        # пересчитывается self.n_pages

    def edit_training(self, page, number, data):
        pass
        # редактируется запись с номером n=page*4 + number
        # страницы и номера тренировок на странице нумеруются с нуля
        # в запись помещаются новые данные из data
        # пересчитывается self.n_pages
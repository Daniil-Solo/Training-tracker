import json
import sys
import os
import datetime
import random

from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QListWidget, QVBoxLayout, QAction
from PyQt5.QtCore import QEvent, Qt

from My_profile import Profile
from Edit_profile_window import EditProfile
from My_records_window import ViewMyRecords
from New_workout_window import NewWorkoutWindow
from New_record_window import NewRecord
from Records_Manager import RecordManager
from Set_goal_window import SetGoal
from Trainings_Manager import TrainingsManager



class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("new_design/new_interface_without_excess.ui", self)
        self.my_profile = Profile()
        self.training_manager = TrainingsManager()
        self.record_manager = RecordManager()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.training_manager.load_database()
        self.curent_page = 0
        self.start_filling()
        self.filling_values()
        self.all_connection()
        self.context_menu()


    def context_menu(self):
        self.last_w_1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.last_w_1.customContextMenuRequested.connect(self.wr_context_menu1)
        self.last_w_1.installEventFilter(self)
        self.last_w_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.last_w_2.customContextMenuRequested.connect(self.wr_context_menu2)
        self.last_w_2.installEventFilter(self)
        self.last_w_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.last_w_3.customContextMenuRequested.connect(self.wr_context_menu3)
        self.last_w_3.installEventFilter(self)
        self.last_w_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.last_w_4.customContextMenuRequested.connect(self.wr_context_menu4)
        self.last_w_4.installEventFilter(self)
        self.copy_all_action1 = QAction('Удалить', self)
        self.copy_all_action1.triggered.connect(self.del_action1)
        self.edit_all_action1 = QAction('Подробнее', self)
        self.edit_all_action1.triggered.connect(self.edit_action1)
        self.copy_all_action2 = QAction('Удалить', self)
        self.copy_all_action2.triggered.connect(self.del_action2)
        self.edit_all_action2 = QAction('Подробнее', self)
        self.edit_all_action2.triggered.connect(self.edit_action2)
        self.copy_all_action3 = QAction('Удалить', self)
        self.copy_all_action3.triggered.connect(self.del_action3)
        self.edit_all_action3 = QAction('Подробнее', self)
        self.edit_all_action3.triggered.connect(self.edit_action3)
        self.copy_all_action4 = QAction('Удалить', self)
        self.copy_all_action4.triggered.connect(self.del_action4)
        self.edit_all_action4 = QAction('Подробнее', self)
        self.edit_all_action4.triggered.connect(self.edit_action4)

    def eventFilter(self, obj, event):
        type(obj), type(event)
        if event.type() == QEvent.ContextMenu and obj is self.last_w_1:
            menu = QMenu(self)
            menu.addAction(self.copy_all_action1)
            menu.addAction(self.edit_all_action1)
            menu.exec_(event.globalPos())
            return True
        elif event.type() == QEvent.ContextMenu and obj is self.last_w_2:
            menu = QMenu(self)
            menu.addAction(self.copy_all_action2)
            menu.addAction(self.edit_all_action2)
            menu.exec_(event.globalPos())
            return True
        elif event.type() == QEvent.ContextMenu and obj is self.last_w_3:
            menu = QMenu(self)
            menu.addAction(self.copy_all_action3)
            menu.addAction(self.edit_all_action3)
            menu.exec_(event.globalPos())
            return True
        elif event.type() == QEvent.ContextMenu and obj is self.last_w_4:
            menu = QMenu(self)
            menu.addAction(self.copy_all_action4)
            menu.addAction(self.edit_all_action4)
            menu.exec_(event.globalPos())
            return True
        return False


    def wr_context_menu1(self, pos):
        menu = QMenu(self)
        menu.addAction(self.copy_all_action1)
        menu.addAction(self.edit_all_action1)
        menu.exec_(self.mapToGlobal(pos))
    def wr_context_menu2(self, pos):
        menu = QMenu(self)
        menu.addAction(self.copy_all_action2)
        menu.addAction(self.edit_all_action2)
        menu.exec_(self.mapToGlobal(pos))
    def wr_context_menu3(self, pos):
        menu = QMenu(self)
        menu.addAction(self.copy_all_action3)
        menu.addAction(self.edit_all_action3)
        menu.exec_(self.mapToGlobal(pos))
    def wr_context_menu4(self, pos):
        menu = QMenu(self)
        menu.addAction(self.copy_all_action4)
        menu.addAction(self.edit_all_action4)
        menu.exec_(self.mapToGlobal(pos))

    def del_action1(self):
        w_date = self.date1.text().partition(' ')[2]
        w_time = self.time1.text().partition(' ')[2]
        self.training_manager.del_workout(w_date, w_time)
        self.update()

    def edit_action1(self):
        if self.date1.text() == "Нет информации":
            return
        w_date = self.date1.text().partition(' ')[2]
        w_time = self.time1.text().partition(' ')[2]
        dist = self.distance1.text().partition(' ')[2]
        temp, heart, description = self.training_manager.view_workout(w_date, w_time)
        self.setEnabled(False)
        data = [w_date, w_time, dist, temp, heart, description]
        self.window_new_training = NewWorkoutWindow(self, self.training_manager, self.my_profile, data=data)
        self.window_new_training.show()

    def del_action2(self):
        w_date = self.date2.text().partition(' ')[2]
        w_time = self.time2.text().partition(' ')[2]
        self.training_manager.del_workout(w_date, w_time)
        self.update()

    def edit_action2(self):
        if self.date2.text() == "Нет информации":
            return
        w_date = self.date2.text().partition(' ')[2]
        w_time = self.time2.text().partition(' ')[2]
        dist = self.distance2.text().partition(' ')[2]
        temp, heart, description = self.training_manager.view_workout(w_date, w_time)
        self.setEnabled(False)
        data = [w_date, w_time, dist, temp, heart, description]
        self.window_new_training = NewWorkoutWindow(self, self.training_manager, self.my_profile, data=data)
        self.window_new_training.show()

    def del_action3(self):
        w_date = self.date3.text().partition(' ')[2]
        w_time = self.time3.text().partition(' ')[2]
        self.training_manager.del_workout(w_date, w_time)
        self.update()

    def edit_action3(self):
        if self.date3.text() == "Нет информации":
            return
        w_date = self.date3.text().partition(' ')[2]
        w_time = self.time3.text().partition(' ')[2]
        dist = self.distance3.text().partition(' ')[2]
        temp, heart, description = self.training_manager.view_workout(w_date, w_time)
        self.setEnabled(False)
        data = [w_date, w_time, dist, temp, heart, description]
        self.window_new_training = NewWorkoutWindow(self, self.training_manager, self.my_profile, data=data)
        self.window_new_training.show()

    def del_action4(self):
        w_date = self.date4.text().partition(' ')[2]
        w_time = self.time4.text().partition(' ')[2]
        self.training_manager.del_workout(w_date, w_time)
        self.update()

    def edit_action4(self):
        if self.date4.text() == "Нет информации":
            return
        w_date = self.date4.text().partition(' ')[2]
        w_time = self.time4.text().partition(' ')[2]
        dist = self.distance4.text().partition(' ')[2]
        temp, heart, description = self.training_manager.view_workout(w_date, w_time)
        self.setEnabled(False)
        data = [w_date, w_time, dist, temp, heart, description]
        self.window_new_training = NewWorkoutWindow(self, self.training_manager, self.my_profile, data=data)
        self.window_new_training.show()

    def update(self):
        self.setEnabled(True)
        self.filling_values()
        self.my_profile.save_changes()
        self.record_manager.save_changes()


    def all_connection(self):
        # иконка скрыть
        self.wrap.clicked.connect(lambda: self.showMinimized())
        # иконка расширить или уменьшить
        self.maximize.clicked.connect(self.restore_or_maximize_window)
        # иконка закрыть
        self.close.clicked.connect(lambda: self.close())
        self.exit_btn.clicked.connect(lambda: self.close())
        # передвижение окна
        self.header_frame.mouseMoveEvent = self.moveWindow
        # to share
        self.share_days.clicked.connect(self.to_share_d)
        self.share_goal.clicked.connect(self.to_share_g)

        # Движение слайдера: общее движение и отдельное для каждой иконки
        self.open_left.clicked.connect(lambda: self.move_slider())
        self.my_profile_btn.clicked.connect(lambda: self.move_slider(0))
        self.workouts_btn.clicked.connect(lambda: self.move_slider(1))
        self.my_records_btn.clicked.connect(lambda: self.move_slider(2))
        self.connect_developers_btn.clicked.connect(lambda: self.move_slider(3))
        self.settings_btn.clicked.connect(lambda: self.move_slider(4))
        self.give_mark_btn.clicked.connect(lambda: self.move_slider(5))
        self.exit_2_btn.clicked.connect(lambda: self.move_slider())

        # Оценивание
        self.star1.clicked.connect(lambda: self.set_mark(1))
        self.star2.clicked.connect(lambda: self.set_mark(2))
        self.star3.clicked.connect(lambda: self.set_mark(3))
        self.star4.clicked.connect(lambda: self.set_mark(4))
        self.star5.clicked.connect(lambda: self.set_mark(5))

        # Кнопки для переключения страниц тренировок
        self.swipe_left.clicked.connect(self.move_left_page)
        self.swipe_right.clicked.connect(self.move_right_page)

        # Кнопки меню
        self.create_workout.clicked.connect(self.create_new_training)
        self.reduct_profile.clicked.connect(self.edit_profile)
        self.set_goal.clicked.connect(self.set_goal_function)
        self.all_records.clicked.connect(self.view_my_records)
        self.new_record.clicked.connect(self.create_new_record)

        # ссылки
        self.git_hub.setText('<a style="color:rgb(230, 5, 64);" href="https://github.com/Daniil-Solo/Training-tracker"> Наш GitHub </a>')
        self.mail.setText('<a style="color:rgb(230, 5, 64);" href="daniil.solo1723@gmail.com"> Наша почта </a>')
        self.vk_group.setText('<a style="color:rgb(230, 5, 64);" href="https://vk.com/public205217752"> Наша группа Vk </a>')

    def to_share_d(self):
        today_train_date = datetime.date.today()
        days = self.training_manager.day_count(today_train_date)
        c = QApplication.clipboard()
        text_r = "Я занимаюсь спортом {0} дней без пропуска вместе с приложением RunWithMe!".format(days)
        if c != None:
            c.setText(text_r)

    def to_share_g(self):
        goal = self.user_goal.text()
        c = QApplication.clipboard()
        text_r = "Я иду к достижению цели {0} вместе с приложением RunWithMe!".format(goal.partition(' ')[2])
        if c != None:
            c.setText(text_r)


    def move_left_page(self):
        self.curent_page -= 1
        self.update_trainings()
        if self.training_manager.is_page_exist(self.curent_page-1):
            self.swipe_left.setEnabled(True)
        else:
            self.swipe_left.setEnabled(False)
    def move_right_page(self):
        self.curent_page += 1
        self.update_trainings()
        if self.training_manager.is_page_exist(self.curent_page + 1):
            self.swipe_right.setEnabled(True)
        else:
            self.swipe_right.setEnabled(False)

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.maximize.setIcon(QtGui.QIcon('new_design/icons/maximize-2.svg'))
        else:
            self.showMaximized()
            self.maximize.setIcon(QtGui.QIcon('new_design/icons/minimize-2.svg'))

    def moveWindow(self, e):
        if not self.isMaximized():
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def filling_values(self):
        self.update_trainings()
        data = self.my_profile.get_data_dict()
        # установка фото
        filename = self.my_profile.get_photo_path()
        if filename is not None:
            pixmap = QtGui.QPixmap(filename)
            self.user_photo.setPixmap(pixmap)
        # установка имени
        if data['name'] is not None:
            self.user_name.setText(data['name'])
        else:
            self.user_name.setText("Нет имени")
        # установка цели
        if data['goal']['title'] is not None:
            self.user_goal.setText("Цель: " + data['goal']['title'])
        else:
            self.user_goal.setText("Нет цели")
        # установка количества дней без пропусков
        self.day_shot.setText("Количество дней без пропуска: " + str(data['nice_days']))
        # установка рейтинга приложения
        self.set_mark(int(data['raiting_app']))

    def update_trainings(self):
        trainings_places = [[self.date1, self.time1, self.distance1],
                            [self.date2, self.time2, self.distance2],
                            [self.date3, self.time3, self.distance3],
                            [self.date4, self.time4, self.distance4]]
        training_values = self.training_manager.get_4_trainings(page=self.curent_page)
        for training_place, training_value in zip(trainings_places, training_values):
            training_place[0].setText(training_value[0])
            training_place[1].setText(training_value[1])
            training_place[2].setText(training_value[2])
        if self.training_manager.is_page_exist(self.curent_page-1):
            self.swipe_left.setEnabled(True)
        else:
            self.swipe_left.setEnabled(False)
        if self.training_manager.is_page_exist(self.curent_page+1):
            self.swipe_right.setEnabled(True)
        else:
            self.swipe_right.setEnabled(False)

        today_train_date = datetime.date.today()
        nice_days = self.training_manager.day_count(today_train_date)
        self.my_profile.data_change('nice_days', nice_days)


    def move_slider(self, number=5):
        self.toolBox.setCurrentIndex(number)
        width = self.slider_menu_container.width()
        if width == 0:
            newWidth = 200
            self.open_left.setIcon(QtGui.QIcon('new_design/icons/chevrons-left.svg'))
        else:
            newWidth = 0
            self.open_left.setIcon(QtGui.QIcon('new_design/icons/chevrons-right.svg'))
        self.animation1 = QPropertyAnimation(self.slider_menu_container, b"maximumWidth")
        self.animation1.setDuration(250)
        self.animation1.setStartValue(width)
        self.animation1.setEndValue(newWidth)
        self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation1.start()
        self.animation2 = QPropertyAnimation(self.icons, b"maximumWidth")
        self.animation2.setDuration(250)
        self.animation2.setStartValue(newWidth//5)
        self.animation2.setEndValue(width//5)
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation2.start()

    def set_mark(self, n_stars):
        stars = [self.star1, self.star2, self.star3, self.star4, self.star5]
        messages = [
            ["Пожалуйста оцените наше приложение", "Пожалуйста оцените наше приложение"],
            ["Спасибо за Вашу оценку! Мы будем работать над нашими ошибками",
             "Спасибо за Вашу оценку! Мы постараемся улучшить приложение"],
            ["Спасибо за Вашу оценку! Мы будем работать над нашими ошибками",
             "Спасибо за Вашу оценку! Мы постараемся улучшить приложение"],
            ["Спасибо за Вашу оценку! Мы рады, что вам нравится наше приложение",
             "Спасибо за Вашу оценку! Приложение будет усовершенствоваться!"],
            ["Спасибо за Вашу оценку! Мы стараемся для Вас!",
             "Спасибо за Вашу оценку! Рады стараться!"],
            ["Спасибо за Вашу оценку! Мы рады, что вы с нами!",
             "Спасибо за Вашу оценку! Заходите сюда почаще!"]
        ]
        for i in range(5, 0, -1):
            if n_stars >= i:
                stars[i-1].setIcon(QtGui.QIcon('new_design/icons/star-fill.svg'))
            else:
                stars[i - 1].setIcon(QtGui.QIcon('new_design/icons/star.svg'))
                self.thanks_for_raiting.setText(messages[i-1][random.randint(0, 1)])
        if n_stars == 5:
            self.thanks_for_raiting.setText(messages[5][random.randint(0, 1)])
        self.my_profile.data_change('raiting_app', n_stars)
        self.my_profile.save_changes()

    def create_new_training(self):
        self.setEnabled(False)
        self.window_new_training = NewWorkoutWindow(self, self.training_manager, self.my_profile)
        self.window_new_training.show()

    def edit_profile(self):
        self.setEnabled(False)
        self.window_edit_profile = EditProfile(self, self.my_profile)
        self.window_edit_profile.show()

    def set_goal_function(self):
        self.setEnabled(False)
        self.window_set_goal = SetGoal(self, self.my_profile)
        self.window_set_goal.show()

    def view_my_records(self):
        self.setEnabled(False)
        self.window_view_my_records = ViewMyRecords(self, self.record_manager)
        self.window_view_my_records.show()

    def create_new_record(self):
        self.setEnabled(False)
        self.window_create_new_record = NewRecord(self, self.record_manager)
        self.window_create_new_record.show()

    def start_filling(self):
        # Установка цитаты
        with open(r"Quotes/Daily_quotes.json", "r") as read_file:
            quote_dict = json.load(read_file)
        number = random.randint(1, 31)
        random_quote = quote_dict[str(number)]
        self.quote.setText(random_quote['text'] + "\nАвтор: " + random_quote['author'])
        # Установка оценки
        mark = int(self.my_profile.get_data_dict()['raiting_app'])
        self.set_mark(mark)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())

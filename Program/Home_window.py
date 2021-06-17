import sys
import os

from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from My_profile import Profile


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("new_design/new_interface.ui", self)
        self.my_profile = Profile()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.my_profile.save_changes()
        data = self.my_profile.load_data()
        self.default_filling_values()
        self.filling_values(data)
        self.all_connection()

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

    def default_filling_values(self):
        pixmap = QtGui.QPixmap('source/default_photo.jpg')
        self.user_photo.setPixmap(pixmap)
        self.user_name.setText("Нет имени")
        self.user_goal.setText("Нет цели")
        self.day_shot.setText("0 дней без пропусков")
        self.set_mark(0)

    def filling_values(self, data):
        if os.path.exists('source/my_photo.jpg'):
            pixmap = QtGui.QPixmap('source/my_photo.jpg')
            self.user_photo.setPixmap(pixmap)
        if data['name'] is not None:
            self.user_name.setText(data['name'])
        if data['goal']['title'] is not None:
            self.user_goal.setText(data['goal']['title'])
        if data['nice_days'] is not None:
            self.day_shot.setText(data['nice_days'] + " дней без пропусков")
        if data['raiting_app'] != 0:
            self.set_mark(int(data['raiting_app']))

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
        for i in range(5, 0, -1):
            if n_stars >= i:
                stars[i-1].setIcon(QtGui.QIcon('new_design/icons/star-fill.svg'))
            else:
                stars[i - 1].setIcon(QtGui.QIcon('new_design/icons/star.svg'))









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())

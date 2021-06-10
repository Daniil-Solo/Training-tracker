import os

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

from My_profile import Profile
from Train_Window import TrainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(802, 618)
        self.setWindowTitle('Example')

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        theme1 = QAction("Тема 1", self)
        theme1.triggered.connect(self.set_theme1)
        theme2 = QAction("Тема 2", self)
        theme2.triggered.connect(self.set_theme2)
        theme3 = QAction("Тема 3", self)
        theme3.triggered.connect(self.set_theme3)

        menubar = self.menuBar()
        themes = menubar.addMenu('&Темы')
        themes.addAction(theme1)
        themes.addAction(theme2)
        themes.addAction(theme3)

        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 40, 791, 521))
        self.tableView.setObjectName("tableView")

        self.redact = QtWidgets.QPushButton(self.tab)
        self.redact.setGeometry(QtCore.QRect(140, 10, 121, 25))
        self.redact.setObjectName("redact")
        self.redact.setStyleSheet("background-color: rgb(147, 129, 255);\n"
                                  "color: rgb(248, 247, 255);")
        self.remove_kebab = QtWidgets.QPushButton(self.tab)
        self.remove_kebab.setGeometry(QtCore.QRect(660, 10, 121, 25))
        self.remove_kebab.setObjectName("remove_kebab")
        self.create = QtWidgets.QPushButton(self.tab)
        self.create.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.create.setObjectName("create")
        self.create.setStyleSheet("background-color: rgb(147, 129, 255);\n"
                                  "color: rgb(248, 247, 255);")
        self.show_graph = QtWidgets.QPushButton(self.tab)
        self.show_graph.setGeometry(QtCore.QRect(280, 10, 151, 25))
        self.show_graph.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.show_graph.setObjectName("show_graph")
        self.show_graph.setStyleSheet("background-color: rgb(147, 129, 255);\n"
                                      "color: rgb(248, 247, 255);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 261))
        self.label.setText("")

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(300, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(110, 350, 241, 211))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 64, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_6.setGeometry(QtCore.QRect(80, 10, 121, 191))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.m100 = QtWidgets.QLineEdit(self.splitter_6)
        self.m100.setObjectName("m100")
        self.m100.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m200 = QtWidgets.QLineEdit(self.splitter_6)
        self.m200.setObjectName("m200")
        self.m200.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m400 = QtWidgets.QLineEdit(self.splitter_6)
        self.m400.setObjectName("m400")
        self.m400.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m800 = QtWidgets.QLineEdit(self.splitter_6)
        self.m800.setObjectName("m800")
        self.m800.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m1000 = QtWidgets.QLineEdit(self.splitter_6)
        self.m1000.setObjectName("m1000")
        self.m1000.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 350, 241, 211))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 81, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.splitter_7 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_7.setGeometry(QtCore.QRect(100, 10, 121, 191))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.m100_2 = QtWidgets.QLineEdit(self.splitter_7)
        self.m100_2.setObjectName("m100_2")
        self.m100_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m200_2 = QtWidgets.QLineEdit(self.splitter_7)
        self.m200_2.setObjectName("m200_2")
        self.m200_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m400_2 = QtWidgets.QLineEdit(self.splitter_7)
        self.m400_2.setObjectName("m400_2")
        self.m400_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m800_2 = QtWidgets.QLineEdit(self.splitter_7)
        self.m800_2.setObjectName("m800_2")
        self.m800_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m1000_2 = QtWidgets.QLineEdit(self.splitter_7)
        self.m1000_2.setObjectName("m1000_2")
        self.m1000_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.changePhoto = QtWidgets.QPushButton(self.tab_2)
        self.changePhoto.setGeometry(QtCore.QRect(50, 300, 151, 31))
        self.changePhoto.setStyleSheet("background-color: rgb(147, 129, 255);\n"
                                       "color: rgb(248, 247, 255);")
        self.changePhoto.setObjectName("changePhoto")
        self.changePhoto.clicked.connect(self.change_photo)
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setGeometry(QtCore.QRect(300, 50, 297, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_2.setGeometry(QtCore.QRect(300, 100, 161, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_3.setGeometry(QtCore.QRect(300, 140, 300, 31))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.height = QtWidgets.QLineEdit(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.height.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.splitter_4 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_4.setGeometry(QtCore.QRect(300, 190, 301, 31))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.weight = QtWidgets.QLineEdit(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.splitter_5 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_5.setGeometry(QtCore.QRect(300, 240, 301, 27))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_7 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(20, 60, 771, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab_3, "")

        self.setCentralWidget(self.central_widget)
        self.retranslateUi()

        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

        # работа с базой данных
        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName("source/workout.db")
        if conn.open():
            print("база данных окрыта")
        else:
            print("не открылась, жалко")

        global createTableQuery
        createTableQuery = QtSql.QSqlQuery()
        createTableQuery.exec(
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

        self.model = QtSql.QSqlTableModel()
        self.model.setTable("workout")
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")  # устанавливаем названия
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Продолжит-сть")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Расстояние")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Темп")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "ЧСС")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Описание")

        self.tableView.setModel(self.model)
        self.tableView.setColumnHidden(0, 1)  # убираем колонку с id
        self.tableView.setColumnWidth(1, 80)  # устанавливаем ширину колонок
        self.tableView.setColumnWidth(2, 120)
        self.tableView.setColumnWidth(3, 100)
        self.tableView.setColumnWidth(4, 80)
        self.tableView.setColumnWidth(5, 80)
        # self.tableView.resizeColumnToContents(6) #выравниваение колонки по содержанию
        self.tableView.setColumnWidth(6, 330)
        self.row1 = -6  # для индекса удаления

        self.my_profile = Profile()
        self.initial_fill()
        self.username.textChanged.connect(self.change_username)
        self.comboBox.currentIndexChanged.connect(self.change_gender)
        self.height.textChanged.connect(self.change_height)
        self.weight.textChanged.connect(self.change_weight)
        self.dateEdit.dateChanged.connect(self.change_birthday)
        self.m100.textChanged.connect(self.change_records)
        self.m200.textChanged.connect(self.change_records)
        self.m400.textChanged.connect(self.change_records)
        self.m800.textChanged.connect(self.change_records)
        self.m1000.textChanged.connect(self.change_records)
        self.m100_2.textChanged.connect(self.change_records)
        self.m200_2.textChanged.connect(self.change_records)
        self.m400_2.textChanged.connect(self.change_records)
        self.m800_2.textChanged.connect(self.change_records)
        self.m1000_2.textChanged.connect(self.change_records)

        self.create.clicked.connect(self.openDialog)
        self.remove_kebab.clicked.connect(self.del_string)
        self.tableView.clicked.connect(self.get_row)
        self.redact.clicked.connect(self.redact_f)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Дневник тренировок"))
        self.redact.setText(_translate("MainWindow", "Обновить"))
        self.remove_kebab.setText(_translate("MainWindow", "Удалить"))
        self.create.setText(_translate("MainWindow", "Создать"))
        self.show_graph.setText(_translate("MainWindow", "Показать график"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Тренировки"))
        self.label_2.setText(_translate("MainWindow", "Мои данные:"))
        self.label_8.setText(_translate("MainWindow", "Личные рекорды:"))
        self.label_9.setText(_translate("MainWindow", "100м"))
        self.label_10.setText(_translate("MainWindow", "200м"))
        self.label_11.setText(_translate("MainWindow", "400м"))
        self.label_12.setText(_translate("MainWindow", "800м"))
        self.label_13.setText(_translate("MainWindow", "1000м"))
        self.label_14.setText(_translate("MainWindow", "3км"))
        self.label_15.setText(_translate("MainWindow", "5км"))
        self.label_16.setText(_translate("MainWindow", "10км"))
        self.label_17.setText(_translate("MainWindow", "21,1км"))
        self.label_18.setText(_translate("MainWindow", "42,2км"))
        self.changePhoto.setText(_translate("MainWindow", "Сменить фото"))
        self.label_4.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Пол"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Мужчина"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Женщина"))
        self.label_5.setText(_translate("MainWindow", "Рост"))
        self.label_6.setText(_translate("MainWindow", "Вес"))
        self.label_7.setText(_translate("MainWindow", "Дата рождения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мой профиль"))
        self.label_19.setText(
            _translate("MainWindow", "Не следует никому давать советы и пользоваться чужими советами, \n"
                                     "кроме общего совета – правила каждому – следовать велениям души и действовать смело.\n"
                                     "\n"
                                     "©Никколо Макиавелли"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "О нас"))

    def keyPressEvent(self, event):
        if int(event.modifiers()) == QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_S:
                self.my_profile.save_changes()
        event.accept()

    def closeEvent(self, event):
        if self.my_profile.need_saving:
            close = QtWidgets.QMessageBox.warning(self, "Выход",
                                                  "Имеются несохраненные данные. Желаете их сохранить?",
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if close == QtWidgets.QMessageBox.Ok:
                self.my_profile.save_changes()

    def set_theme1(self):
        print('1')

    def set_theme2(self):
        print('2')

    def set_theme3(self):
        print('3')

    def initial_fill(self):
        # photo
        if os.path.exists('source/my_photo.jpg'):
            pixmap = QtGui.QPixmap('source/my_photo.jpg')
        else:
            pixmap = QtGui.QPixmap('source/default_photo.jpg')
        self.label.setPixmap(pixmap)

        # data
        data = self.my_profile.load_data()
        if data['name'] is None:
            self.username.setText("")
        else:
            self.username.setText(data['name'])
        if data['gender'] is None:
            self.comboBox.setCurrentIndex(0)
        else:
            self.comboBox.setCurrentIndex(int(data['gender']))
        if data['height'] is None:
            self.height.setText("")
        else:
            self.height.setText(data['height'])
        if data['weight'] is None:
            self.weight.setText("")
        else:
            self.weight.setText(data['weight'])
        if data['birthday'] is None:
            self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        else:
            self.dateEdit.setDateTime(QtCore.QDateTime.fromString(data['birthday']))
        # records
        if data['record_100'] is None:
            self.m100.setText("")
        else:
            self.m100.setText(data['record_100'])
        if data['record_200'] is None:
            self.m200.setText("")
        else:
            self.m200.setText(data['record_200'])
        if data['record_400'] is None:
            self.m400.setText("")
        else:
            self.m400.setText(data['record_400'])
        if data['record_800'] is None:
            self.m800.setText("")
        else:
            self.m800.setText(data['record_800'])
        if data['record_1_000'] is None:
            self.m1000.setText("")
        else:
            self.m1000.setText(data['record_1_000'])

        if data['record_3_000'] is None:
            self.m100_2.setText("")
        else:
            self.m100_2.setText(data['record_3_000'])
        if data['record_5_000'] is None:
            self.m200_2.setText("")
        else:
            self.m200_2.setText(data['record_5_000'])
        if data['record_10_000'] is None:
            self.m400_2.setText("")
        else:
            self.m400_2.setText(data['record_10_000'])
        if data['record_21_000'] is None:
            self.m800_2.setText("")
        else:
            self.m800_2.setText(data['record_21_000'])
        if data['record_42_000'] is None:
            self.m1000_2.setText("")
        else:
            self.m1000_2.setText(data['record_42_000'])

    def change_username(self):
        self.my_profile.data_change('name', self.username.text())

    def change_gender(self):
        self.my_profile.data_change('gender', self.comboBox.currentIndex())

    def change_height(self):
        self.my_profile.data_change('height', self.height.text())

    def change_weight(self):
        self.my_profile.data_change('weight', self.weight.text())

    def change_birthday(self):
        self.my_profile.data_change('birthday', self.dateEdit.dateTime().toString())

    def change_records(self):
        self.my_profile.data_change('record_100', self.m100.text())
        self.my_profile.data_change('record_200', self.m200.text())
        self.my_profile.data_change('record_400', self.m400.text())
        self.my_profile.data_change('record_800', self.m800.text())
        self.my_profile.data_change('record_1_000', self.m1000.text())
        self.my_profile.data_change('record_3_000', self.m100_2.text())
        self.my_profile.data_change('record_5_000', self.m200_2.text())
        self.my_profile.data_change('record_10_000', self.m400_2.text())
        self.my_profile.data_change('record_21_000', self.m800_2.text())
        self.my_profile.data_change('record_42_000', self.m1000_2.text())

    def change_photo(self):
        filename = QFileDialog.getOpenFileName(filter="Image (*.jpg)")[0]
        if os.path.exists(filename):
            new_filename = self.my_profile.photo_change(filename)
            pixmap = QtGui.QPixmap(new_filename)
            self.label.setPixmap(pixmap)

    def openDialog(self):
        print("create")
        #self.model.insertRow(self.model.rowCount())
        self.dialog = TrainWindow()
        self.dialog.show()

        self.model = QtSql.QSqlTableModel()
        self.model.setTable("workout")
        self.tableView.setModel(self.model)
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")  # устанавливаем названия
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Продолжит-сть")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Расстояние")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Темп")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "ЧСС")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Описание")


    def redact_f(self):
        #print(str(createTableQuery))
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("workout")
        self.tableView.setModel(self.model)
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")  # устанавливаем названия
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Продолжит-сть")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Расстояние")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Темп")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "ЧСС")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Описание")

    def del_string(self):
        self.model.removeRow(self.row1)
        print(self.row1)
        print("delete")

    def get_row(self):
        self.row1 = self.tableView.currentIndex().row()

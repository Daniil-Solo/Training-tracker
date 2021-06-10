from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

class TrainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(TrainWindow, self).__init__(parent)
        self.setFixedSize(852, 618)
        self.setWindowTitle('Example')
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(260, 22, 121, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(260, 70, 121, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBox.setGeometry(QtCore.QRect(260, 120, 121, 31))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(260, 170, 121, 31))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(300)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(260, 230, 551, 181))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(350, 440, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(147, 129, 255);\n"
                                      "color: rgb(248, 247, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.cr_new)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 450, 101, 31))
        self.pushButton_2.setStyleSheet("color: rgb(248, 247, 255);\n"
                                        "background-color: rgb(184, 184, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

    def cr_new(self):
        print("it work")
        w_date1 = "today"
        w_time1 = self.lineEdit.text()
        w_distance1 = self.doubleSpinBox.text()
        w_temp1 = 'в разработке'
        w_heart1 = self.spinBox.text()
        w_description1 = self.textEdit.toPlainText()
        self.createTableQuery.prepare(
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
        self.createTableQuery.addBindValue(w_date1)
        self.createTableQuery.addBindValue(w_time1)
        self.createTableQuery.addBindValue(w_distance1)
        self.createTableQuery.addBindValue(w_temp1)
        self.createTableQuery.addBindValue(w_heart1)
        self.createTableQuery.addBindValue(w_description1)
        self.createTableQuery.exec()

        self.close()
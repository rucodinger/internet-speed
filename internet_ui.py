# Form implementation generated from reading ui file '.\internet_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from internet import speed_test


class Ui_MainWindow(object):

    def test_start(self):
        test = speed_test()
        self.download.setText(f"{(test['download'] / 1024) / 1024} MB/S")
        self.upload.setText(f"{(test['upload'] / 1024) / 1024} MB/S")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_btn.setGeometry(QtCore.QRect(10, 0, 471, 51))
        self.test_btn.clicked.connect(self.test_start)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.test_btn.setFont(font)
        self.test_btn.setObjectName("test_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.upload = QtWidgets.QLabel(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(170, 70, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.upload.setFont(font)
        self.upload.setText("")
        self.upload.setObjectName("upload")
        self.download = QtWidgets.QLabel(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(170, 130, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.download.setFont(font)
        self.download.setText("")
        self.download.setObjectName("download")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Скорость интернета"))
        self.test_btn.setText(_translate("MainWindow", "Начать тест скорости интернета"))
        self.label.setText(_translate("MainWindow", "Upload speed:"))
        self.label_3.setText(_translate("MainWindow", "Download speed:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

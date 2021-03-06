# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoDetect.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 584)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "    background-color: rgb(0, 0, 127, 0.5);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: rgb(0, 0, 127, 0.3);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setMaximumSize(QtCore.QSize(50, 50))
        self.lab_video.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Arial\";")
        self.lab_video.setObjectName("lab_video")
        self.gridLayout.addWidget(self.lab_video, 2, 2, 1, 1)
        self.sld_video = myVideoSlider(self.centralwidget)
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.gridLayout.addWidget(self.sld_video, 2, 0, 1, 2)
        self.wgt_video_2 = myVideoWidget(self.centralwidget)
        self.wgt_video_2.setMinimumSize(QtCore.QSize(410, 200))
        self.wgt_video_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video_2.setPalette(palette)
        self.wgt_video_2.setAutoFillBackground(True)
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.gridLayout.addWidget(self.wgt_video_2, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 20pt \"??????\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setMinimumSize(QtCore.QSize(410, 200))
        self.wgt_video.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(True)
        self.wgt_video.setObjectName("wgt_video")
        self.gridLayout.addWidget(self.wgt_video, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 20pt \"??????\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_open = QtWidgets.QPushButton(self.splitter)
        self.btn_open.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_open.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_open.setStyleSheet("QPushButton {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 38, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "border-radius:8px;\n"
                                    "color:white;\n"
                                    "spacing:20px;\n"
                                    "    font: 16pt \"??????\";\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 33, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 33, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:disabled{\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}")
        self.btn_open.setObjectName("btn_open")
        self.btn_play = QtWidgets.QPushButton(self.splitter)
        self.btn_play.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_play.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_play.setStyleSheet("QPushButton {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 38, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "border-radius:8px;\n"
                                    "color:white;\n"
                                    "spacing:20px;\n"
                                    "    font: 16pt \"??????\";\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 33, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 33, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:disabled{\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}")
        self.btn_play.setObjectName("btn_play")
        self.btn_stop = QtWidgets.QPushButton(self.splitter)
        self.btn_stop.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_stop.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_stop.setStyleSheet("QPushButton {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 38, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "border-radius:8px;\n"
                                    "color:white;\n"
                                    "spacing:20px;\n"
                                    "    font: 16pt \"??????\";\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 33, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 33, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:disabled{\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}")
        self.btn_stop.setObjectName("btn_stop")
        self.sld_audio = QtWidgets.QSlider(self.splitter)
        self.sld_audio.setMinimumSize(QtCore.QSize(100, 50))
        self.sld_audio.setMaximumSize(QtCore.QSize(150, 20))
        self.sld_audio.setProperty("value", 99)
        self.sld_audio.setOrientation(QtCore.Qt.Horizontal)
        self.sld_audio.setObjectName("sld_audio")
        self.lab_audio = QtWidgets.QLabel(self.splitter)
        self.lab_audio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 14pt \"Arial\";")
        self.lab_audio.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_audio.setObjectName("lab_audio")
        self.btn_cast = QtWidgets.QPushButton(self.splitter)
        self.btn_cast.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_cast.setStyleSheet("QPushButton {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 38, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "border-radius:8px;\n"
                                    "color:white;\n"
                                    "spacing:20px;\n"
                                    "    font: 16pt \"??????\";\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 33, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 33, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}\n"
                                    "QPushButton:disabled{\n"
                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "}")
        self.btn_cast.setObjectName("btn_cast")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 38, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "border-radius:8px;\n"
                                      "color:white;\n"
                                      "spacing:20px;\n"
                                      "    font: 16pt \"??????\";\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(147, 33, 250, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 33, 80, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "}\n"
                                      "QPushButton:disabled{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.splitter, 3, 0, 1, 3)
        self.gridLayout.setRowStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_video.setText(_translate("MainWindow", "0%"))
        self.label.setText(_translate("MainWindow", "??????????????????"))
        self.label_2.setText(_translate("MainWindow", "??????????????????"))
        self.btn_open.setText(_translate("MainWindow", "??????"))
        self.btn_play.setText(_translate("MainWindow", "??????"))
        self.btn_stop.setText(_translate("MainWindow", "??????"))
        self.lab_audio.setText(_translate("MainWindow", "volume:100%"))
        self.btn_cast.setText(_translate("MainWindow", "??????"))


from myVideoWidget import myVideoWidget
from myvideoslider import myVideoSlider

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
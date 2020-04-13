# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_player.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class Ui_video_player(object):
    def setupUi(self, video_player):
        video_player.setObjectName("video_player")
        video_player.resize(1280, 720)
        video_player.setMinimumSize(QtCore.QSize(1280, 720))
        video_player.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ico/病毒.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        video_player.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(video_player)
        self.centralwidget.setObjectName("centralwidget")
        self.video_play_widget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        # self.video_play_widget = QtWidgets.QWidget(self.centralwidget)
        self.video_play_widget.setGeometry(QtCore.QRect(0, 0, 1071, 631))
        self.video_play_widget.setMinimumSize(QtCore.QSize(1071, 631))
        self.video_play_widget.setMaximumSize(QtCore.QSize(1071, 631))
        self.video_play_widget.setObjectName("video_play_widget")
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("../ico/landscape.jpg")))
        # self.setPalette(palette)
        self.data_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.data_widget.setGeometry(QtCore.QRect(1070, 0, 211, 701))
        self.data_widget.setMinimumSize(QtCore.QSize(211, 701))
        self.data_widget.setMaximumSize(QtCore.QSize(211, 701))
        self.data_widget.setObjectName("data_widget")
        self.data_widget.setColumnCount(0)
        self.data_widget.setRowCount(0)
        self.upload_delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_delete_button.setGeometry(QtCore.QRect(0, 640, 48, 48))
        self.upload_delete_button.setMinimumSize(QtCore.QSize(48, 48))
        self.upload_delete_button.setMaximumSize(QtCore.QSize(48, 48))
        self.upload_delete_button.setText("")
        self.upload_delete_button.setStyleSheet("border:none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ico/add_to_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_delete_button.setIcon(icon)
        self.upload_delete_button.setIconSize(QtCore.QSize(48, 48))
        self.upload_delete_button.setObjectName("upload_delete_button")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(70, 640, 48, 48))
        self.back_button.setMinimumSize(QtCore.QSize(48, 48))
        self.back_button.setMaximumSize(QtCore.QSize(48, 48))
        self.back_button.setText("")
        self.back_button.setStyleSheet("border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ico/on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QtCore.QSize(48, 48))
        self.back_button.setObjectName("back_button")
        self.on_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.on_off_button.setGeometry(QtCore.QRect(130, 640, 48, 48))
        self.on_off_button.setMinimumSize(QtCore.QSize(48, 48))
        self.on_off_button.setMaximumSize(QtCore.QSize(48, 48))
        self.on_off_button.setText("")
        self.on_off_button.setStyleSheet("border:none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ico/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.on_off_button.setIcon(icon2)
        self.on_off_button.setIconSize(QtCore.QSize(48, 48))
        self.on_off_button.setObjectName("on_button")
        self.forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.forward_button.setGeometry(QtCore.QRect(190, 640, 48, 48))
        self.forward_button.setMinimumSize(QtCore.QSize(48, 48))
        self.forward_button.setMaximumSize(QtCore.QSize(48, 48))
        self.forward_button.setText("")
        self.forward_button.setStyleSheet("border:none;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ico/de.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward_button.setIcon(icon3)
        self.forward_button.setIconSize(QtCore.QSize(48, 48))
        self.forward_button.setObjectName("forward_button")
        self.now_timer_label = QtWidgets.QLabel(self.centralwidget)
        self.now_timer_label.setGeometry(QtCore.QRect(250, 640, 31, 48))
        self.now_timer_label.setMinimumSize(QtCore.QSize(0, 48))
        self.now_timer_label.setMaximumSize(QtCore.QSize(16777215, 48))
        self.now_timer_label.setObjectName("now_timer_label")
        self.timer_slider = QtWidgets.QSlider(self.centralwidget)
        self.timer_slider.setGeometry(QtCore.QRect(290, 650, 451, 31))
        self.timer_slider.setMinimumSize(QtCore.QSize(0, 31))
        self.timer_slider.setMaximumSize(QtCore.QSize(16777215, 31))
        self.timer_slider.setOrientation(QtCore.Qt.Horizontal)
        self.timer_slider.setObjectName("timer_slider")
        self.whole_timer_label = QtWidgets.QLabel(self.centralwidget)
        self.whole_timer_label.setGeometry(QtCore.QRect(750, 640, 31, 48))
        self.whole_timer_label.setMinimumSize(QtCore.QSize(0, 48))
        self.whole_timer_label.setMaximumSize(QtCore.QSize(16777215, 48))
        self.whole_timer_label.setObjectName("whole_timer_label")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(790, 640, 31, 51))
        self.volume_label.setText("")
        self.volume_label.setPixmap(QtGui.QPixmap("../ico/high_volume.png"))
        self.volume_label.setObjectName("volume_label")
        self.volume_slider = QtWidgets.QSlider(self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(820, 650, 241, 31))
        self.volume_slider.setProperty("value", 50)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        video_player.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(video_player)
        self.statusbar.setObjectName("statusbar")
        video_player.setStatusBar(self.statusbar)

        self.retranslateUi(video_player)
        QtCore.QMetaObject.connectSlotsByName(video_player)

    def retranslateUi(self, video_player):
        _translate = QtCore.QCoreApplication.translate
        video_player.setWindowTitle(_translate("video_player", "video_player"))
        self.now_timer_label.setText(_translate("video_player", "00:00"))
        self.whole_timer_label.setText(_translate("video_player", "00:00"))

import sys

from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton
from PyQt5.QtWidgets import QMainWindow
from video_player import Ui_video_player  # 加载ui布局


class test(QMainWindow, Ui_video_player):
    def __init__(self, *args, **kwargs):
        super(test, self).__init__(*args, **kwargs)
        self.flag = 0  # 用于获取视频全长度
        self.setupUi(self)  # 初始化ui
        self.bind()  # 绑定事件

    def bind(self):
        self.upload_delete_button.clicked.connect(self.upload_file)
        self.on_off_button.clicked.connect(self.play_pause)  # 播放和暂停

    def upload_file(self):
        file = QFileDialog.getOpenFileName(self, "选择文件", "C:/Users/陈键淞/Desktop", " MP4 Files(*.mp4);;AVI Files(*.avi)")
        # 此处进行视频处理
        if file[0]:
            self.player.setVideoOutput(self.video_play_widget)  # 视频播放输出的widget
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file[0])))  # 选取视频文件
            self.player.setVolume(50)  # 设置初始播放音量
            self.player.positionChanged.connect(self.show_video_slider)  # 视频进度
            self.volume_slider.valueChanged.connect(self.drag_volume_slider)  # 拖动音量条调节音量
            self.timer_slider.sliderMoved.connect(self.drag_video_slider)  # 拖动进度条改变播放进度
            self.timer_slider.sliderReleased.connect(self.drag_video_slider_over)  # 拖动进度条调整完成
            self.on_off_button.setObjectName("off_button")
            self.on_off_button.setIcon(QIcon("../ico/stop.png"))
            self.player.play()  # 播放视频

    # 控制视频播放和暂停
    def play_pause(self):
        if self.on_off_button.objectName() == "off_button":
            self.player.pause()
            print(self.player.State)
            self.on_off_button.setObjectName("on_button")
            self.on_off_button.setIcon(QIcon("../ico/start.png"))
        elif self.on_off_button.objectName() == "on_button":
            self.player.play()
            self.on_off_button.setObjectName("off_button")
            self.on_off_button.setIcon(QIcon("../ico/stop.png"))

    # 监听视频当前进度
    def show_video_slider(self, position):
        video_length = self.player.duration()
        self.timer_slider.setRange(0, int(video_length / 1000) + 1)  # 设置进度条范围
        self.timer_slider.setValue(round(int(position / 1000)))
        self.now_timer_label.setText(  # 当前视频进度
            str(int(position / 1000) // 60).zfill(2) + ':' + str(int(position / 1000) % 60).zfill(2)
        )
        # 设置视频全长度
        if self.flag == 0:
            video_length = self.player.duration()
            self.timer_slider.setRange(0, int(video_length / 1000) + 1)  # 设置进度条范围
            self.whole_timer_label.setText(  # 全视频长度
                str(int(video_length / 1000) // 60).zfill(2) + ':' + str(int(video_length / 1000) % 60).zfill(2)
            )
            self.flag = 1

    # 拖动音量进度条，调节音量
    def drag_volume_slider(self):
        self.player.setVolume(self.volume_slider.value())
        if self.volume_slider.value() == 0:
            self.volume_label.setPixmap(QPixmap("../ico/no_volume.png"))
        elif self.volume_slider.value() < 30:
            self.volume_label.setPixmap(QPixmap("../ico/small_volume.png"))
        elif self.volume_slider.value() < 70:
            self.volume_label.setPixmap(QPixmap("../ico/center_volume.png"))
        else:
            self.volume_label.setPixmap(QPixmap("../ico/high_volume.png"))

    # 拖动视频进度条，调节视频进度， 有bug，尚未解决
    def drag_video_slider(self):
        self.player.pause()
        self.timer_slider.valueChanged.connect(self.set_video_value)

    def set_video_value(self):
        self.player.setPosition(self.timer_slider.value() * 1000)

    def drag_video_slider_over(self):
        self.player.play()


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = test()
    win.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QCheckBox, QCalendarWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget 


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setHorizontalHeaderFormat(self.calendar.HorizontalHeaderFormat.SingleLetterDayNames)
        self.start = QPushButton("Старт")
        self.stop = QPushButton("Стоп")
        self.autostart = QCheckBox("Автостарт")
        self.video = QVideoWidget()
        self.calendar.setVerticalHeaderFormat(self.calendar.VerticalHeaderFormat.NoVerticalHeader)
        panel_layout = QVBoxLayout()
        panel_layout.addWidget(self.start)
        panel_layout.addWidget(self.stop)
        panel_layout.addWidget(self.autostart)

        H_layout = QHBoxLayout()
        H_layout.addWidget(self.calendar)
        H_layout.addLayout(panel_layout)


        main_layout = QVBoxLayout()
        main_layout.addLayout(H_layout,stretch=1)
        main_layout.addWidget(self.video,stretch=1)

        self.setLayout(main_layout)

    def configure(self):
        ...

    def get_date(self):
        return self.calendar.selectedDate().day()

    def media_play(self):
        self.media = QMediaPlayer()
        self.media.setVideoOutput(self.video)
        play = QMediaContent(QUrl.fromLocalFile(f"Video\\{self.get_date()}.avi"))
        self.media.setMedia(play)
        self.media.play()

    def media_stop(self):
        self.media.stop()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.setFixedSize(500, 550)
    window.show()
    window.media_play()
    window.start.clicked.connect(window.media_play)
    window.stop.clicked.connect(window.media_stop)
    sys.exit(app.exec_())

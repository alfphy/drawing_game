import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui
import ui.playScene
import numpy as np

import time


def qimage_to_numpy(qimage):
    qimage = qimage.convertToFormat(QtGui.QImage.Format.Format_RGB888)
    width, height = qimage.width(), qimage.height()
    ptr = qimage.bits()
    ptr.setsize(height * width * 3)
    return np.array(ptr).reshape(height, width, 3)

class DrawingCanvas(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.painter = QtGui.QPainter(self.image)
        self.last_point = None
        self.brush_size = 3
        self.brush_color = QtCore.Qt.GlobalColor.black

    def resizeEvent(self, event):
        new_image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        new_image.fill(QtCore.Qt.GlobalColor.white)
        painter = QtGui.QPainter(new_image)
        painter.drawImage(0, 0, self.image)
        self.image = new_image
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.last_point:
            current_point = event.position().toPoint()
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brush_color, self.brush_size, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap, QtCore.Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(self.last_point, current_point)
            self.last_point = current_point
            self.update()

    def mouseReleaseEvent(self, event):
        self.last_point = None

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(0, 0, self.image)


class PlayPages(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.playScene.Ui_playScene()
        self.ui.setupUi(self)
        self.ui.drawing_space.hide()
        self.canvas = DrawingCanvas(self)
        self.ui.verticalLayout_4.addWidget(self.canvas)

        # Timer setup
        self.time_left = 60  # 60 seconds default
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Connect buttons (adjust names to match your UI)
        # self.ui.startButton.clicked.connect(self.start_timer)
        # self.ui.submitButton.clicked.connect(self.stop_timer)

        # Display initial time
        self.update_timer_display()
        self.start_timer(30)

    def start_timer(self, seconds=60):
        """Start the countdown timer"""
        self.time_left = seconds
        self.timer.start(1000)  # 1000ms = 1 second
        self.update_timer_display()

    def stop_timer(self):
        """Stop the timer"""
        self.timer.stop()

    def reset_timer(self, seconds=60):
        """Reset timer to initial value"""
        self.time_left = seconds
        self.update_timer_display()

    def update_timer(self):
        """Called every second by QTimer"""
        self.time_left -= 1
        self.update_timer_display()

        if self.time_left <= 0:
            self.timer.stop()
            self.times_up()

        # Visual warning when time is low
        if self.time_left <= 10:
            self.ui.label_timer.setStyleSheet("color: red; font-weight: bold;")

    def update_timer_display(self):
        """Update the timer label"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.ui.label_timer.setText(f"{minutes:02d}:{seconds:02d}")

    def times_up(self):
        """Called when timer reaches 0"""
        self.ui.label_timer.setText("TIME'S UP!")
        # Auto-submit or disable drawing here
        # self.submit_drawing()

    def get_remaining_time(self):
        """Return time left in seconds"""
        return self.time_left



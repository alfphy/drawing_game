import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui

import analyzer.clip_process
import ui.playScene
import numpy as np
import analyzer.phrases
import time
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QColorDialog, QPushButton

import random
class DrawingCanvas(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setMinimumSize(640, 640)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.last_point = None
        self.brush_size = 3
        self.brush_color = QtCore.Qt.GlobalColor.black


    def clear(self):
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.update()

    def mousePressEvent(self, event):
        if self.parent.time_left == 0:
            print("time out")
        else:
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.parent.time_left == 0:
            print("time out")
        else:
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
    def save_image(self):
        # Convert QImage to numpy array
        width = self.image.width()
        height = self.image.height()
        ptr = self.image.bits()
        ptr.setsize(height * width * 4)  # ARGB32 = 4 bytes per pixel
        arr = np.array(ptr).reshape(height, width, 4)

        # Find non-white pixels (alpha > 0 and not white)
        # White = [255, 255, 255, 255]
        non_white = np.any(arr != [255, 255, 255, 255], axis=2)

        if not np.any(non_white):
            print("Canvas is empty!")
            return

        # Find bounding box of non-white pixels
        rows = np.any(non_white, axis=1)
        cols = np.any(non_white, axis=0)

        y_min, y_max = np.where(rows)[0][[0, -1]]
        x_min, x_max = np.where(cols)[0][[0, -1]]

        # Add padding (optional)
        padding = 10
        y_min = max(0, y_min - padding)
        y_max = min(height - 1, y_max + padding)
        x_min = max(0, x_min - padding)
        x_max = min(width - 1, x_max + padding)

        # Crop the image
        cropped = self.image.copy(x_min, y_min, x_max - x_min + 1, y_max - y_min + 1)

        # Save
        cropped.save('draw.png')
        print(f"Image cropped and saved! ({x_max - x_min + 1}x{y_max - y_min + 1})")


class PlayPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.playScene.Ui_playScene()
        self.ui.setupUi(self)
        self.canvas = DrawingCanvas(self)
        self.ui.drawing_space.addWidget(self.canvas)
        self.ui.drawing_space.setAlignment(self.canvas,  QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ui.choose_color.clicked.connect(self.choose_color)
        #random by default pag kuha og phrase
        phrase_index = random.randint(0,19)
        category_index = random.randint(0,3)

        category_name, phrase = analyzer.phrases.get_phrase(category_index, phrase_index)

        self.ui.label_phrase.setText(phrase)
        self.ui.label_category.setText(str(category_name))
        # Timer setup
        self.time_left = 60  # 60 seconds default
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)


        self.update_timer_display()

    def choose_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.canvas.brush_color = color
            self.ui.widget_colorselected.setStyleSheet(f"background-color: {color.name()};")

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
        self.canvas.save_image()

        print("Generating result")
        score = analyzer.clip_process.score_drawing('draw.png',str(self.ui.label_phrase.text()))

        print("New phrase coming...")
        self.canvas.clear()
        phrase_index = random.randint(0, 19)
        category_index = random.randint(0, 3)

        category_name, phrase = analyzer.phrases.get_phrase(category_index, phrase_index)

        self.ui.label_phrase.setText(phrase)
        self.ui.label_category.setText(str(category_name))
        self.start_timer(30)



    def get_remaining_time(self):
        """Return time left in seconds"""
        return self.time_left



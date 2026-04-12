import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui
from mpmath import diag
import threading

import PlayingGround.canvas
import ResultPage
import analyzer.realtime_analysis
import analyzer.clip_process
import analyzer.scoring_analysis
import ui.playScene
import numpy as np
import roundsetting.phrases
import roundsetting.game_state
from PyQt6.QtWidgets import QColorDialog

import random


class PlayPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.playScene.Ui_playScene()
        self.ui.setupUi(self)
        self.canvas = PlayingGround.canvas.DrawingCanvas(self)
        self.ui.drawing_space.addWidget(self.canvas)
        self.ui.drawing_space.setAlignment(self.canvas,  QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ui.button_color_picker.clicked.connect(self.choose_color)


        self.ui.button_done.clicked.connect(self.done_drawing)
        # Timer setup
        self.time_left = 60  # 60 seconds default
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)


        self.update_timer_display()

        self.ui.verticalSlider.setRange(1, 20)  # Set appropriate range
        self.ui.verticalSlider.valueChanged.connect(self.adjust_brush_size)
        self.ui.button_erase.clicked.connect(self.toggle_eraser_mode)
        self.ui.button_pen.clicked.connect(self.toggle_pen_mode)
        self.ui.button_fill.clicked.connect(self.toggle_fill_mode)


        self.category_name = None
        self.phrase = None
        self.analysis_worker = analyzer.realtime_analysis.AnalysisWorker()
        self.analysis_worker.signal.connect(self.update_feedback)



        self.analysis_timer = QtCore.QTimer()
        self.analysis_timer.timeout.connect(self.run_feedback_analysis)

    def start_drawing(self):
        initial_time = roundsetting.game_state.game_config.difficulty_config.initial_time
        self.start_timer(initial_time)
        category_name, phrase = roundsetting.game_state.game_config.get_single_phrase()
        self.ui.label_difficulty.setText(roundsetting.game_state.game_config.difficulty_config.difficulty)

        self.category_name = category_name
        self.phrase = phrase
        self.analysis_timer.start(2000)
        self.ui.label_phrase.setText(phrase)
        self.ui.label_phrase.setStyleSheet("""
         font-family:'sans-serif'; font-size:21pt; font-weight:600; color:#ffffff;
        border:none;
        background:transparent;
        """)

        self.ui.label_category.setText(str(category_name))
        self.ui.label_category.setStyleSheet("""

                color:#7da5e7; font-family: "Arial", "Helvetica", sans-serif;
        border:none;
        font-weight:600;
        font-size:12pt

                """)

    def done_drawing(self):
        self.stop_timer()
        self.canvas.save_image()
        self.analysis_timer.stop()

        print("Generating result")
        score = analyzer.scoring_analysis.score_drawing('draw.png', str(self.ui.label_phrase.text()), self.category_name)

        time_spent = 60 - self.time_left
        target_phrase = str(self.ui.label_phrase.text())

        dialog_result = ResultPage.ResultPage(self, score=score, time_spent=time_spent, target_phrase=target_phrase)


        dialog_result.exec()
        self.canvas.clear()
        self.start_drawing()



    def run_feedback_analysis(self):
        current_image = self.canvas.get_image()

        if isinstance(current_image, np.ndarray) and np.all(current_image == 255):
            self.ui.label_ai_feedback.setText("waiting for you to draw...")
            return

        if not self.analysis_worker.isRunning():
            self.analysis_worker.set_data(current_image, self.phrase)
            self.analysis_worker.start()

    def update_feedback(self, commentary):
        self.ui.label_ai_feedback.setText(commentary)


    def reset_tool_buttons(self):
        self.ui.button_pen.setStyleSheet("background:transparent; border:none;")
        self.ui.button_erase.setStyleSheet("background:transparent; border:none;")
        self.ui.button_fill.setStyleSheet("background:transparent; border:none;")

    def toggle_pen_mode(self):
        if self.canvas.is_eraser:
            self.canvas.set_eraser_mode(False)
        if self.canvas.is_fill_mode:
            self.canvas.set_fill_mode(False)
        self.reset_tool_buttons()
        self.ui.button_pen.setStyleSheet("background-color: #0069EC; border-radius: 10px; border: 2px solid white;")

    def toggle_eraser_mode(self):
        if self.canvas.is_eraser:
            self.canvas.set_eraser_mode(False)
            self.ui.button_erase.setStyleSheet("background:transparent; border:none;")
        else:
            if self.canvas.is_fill_mode:
                self.canvas.set_fill_mode(False)
            self.canvas.set_eraser_mode(True)
            self.reset_tool_buttons()
            self.ui.button_erase.setStyleSheet("background-color: #0069EC; border-radius: 10px; border: 2px solid white;")

    def toggle_fill_mode(self):
        if self.canvas.is_fill_mode:
            self.canvas.set_fill_mode(False)
            self.ui.button_fill.setStyleSheet("background:transparent; border:none;")
        else:
            if self.canvas.is_eraser:
                self.canvas.set_eraser_mode(False)
            self.canvas.set_fill_mode(True)
            self.reset_tool_buttons()
            self.ui.button_fill.setStyleSheet("background-color: #0069EC; border-radius: 10px; border: 2px solid white;")

    def choose_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.canvas.brush_color = color
            self.ui.button_color_selected.setStyleSheet(f"""background-color: {color.name()}; 
border: 2px solid white;
    border-radius: 12px;
margin:0px; """)

    def start_timer(self, seconds=60):
        """Start the countdown timer"""
        self.time_left = seconds
        self.timer.start(1000)  # 1000ms = 1 second
        self.ui.label_timer.setStyleSheet(
            "color: white; font-weight: bold; font-family: 'JetBrains Mono', monospace; font-size: 28px; font-weight: 800; border:none; background:transparent; padding-left:8px;")

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
            self.ui.label_timer.setStyleSheet("color: red; font-weight: bold; font-family: 'JetBrains Mono', monospace; font-size: 28px; font-weight: 800; border:none; background:transparent; padding-left:8px;")

    def update_timer_display(self):
        """Update the timer label"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.ui.label_timer.setText(f"{minutes:02d}:{seconds:02d}")

    def times_up(self):
        """Called when timer reaches 0"""
        self.ui.label_timer.setText("00:00")
        self.done_drawing()




    def get_remaining_time(self):
        return self.time_left

    def adjust_brush_size(self, size):
        self.canvas.brush_size = size

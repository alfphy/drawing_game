import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
from PyQt6.QtGui import QPixmap

import ui.playScene
import ui.resultScene


class ResultPage(qtw.QDialog):
    def __init__(self, parent, score=0, time_spent=0, target_phrase=""):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_next.clicked.connect(self.button_next_clicked)
        self.setModal(True)
        self.set_data(score, time_spent)
        self.display_sketch()

        self.move(
            parent.x() + (parent.width() - self.width()) // 2,
            parent.y() + (parent.height() - self.height()) // 2
        )

    def set_data(self, score, time_spent):
        self.ui.label_accuracy.setText(f"{int(score)}%")
        self.ui.label_timespent.setText(f"{time_spent}s")

        
        if score >= 90:
            self.ui.label_rate.setText("PERFECT!")
            self.set_stars(5)
        elif score >= 70:
            self.ui.label_rate.setText("Good job!")
            self.set_stars(4)
        elif score >= 50:
            self.ui.label_rate.setText("Not bad!")
            self.set_stars(3)
        elif score >= 30:
            self.ui.label_rate.setText("Keep trying!")
            self.set_stars(2)
        else:
            self.ui.label_rate.setText("Keep trying!")
            self.set_stars(1)

    def display_sketch(self):
        target_size = self.ui.sketch_card.size()
        self.ui.label_sketch.setFixedSize(target_size)


        pixmap = qtg.QPixmap('draw.png')
        scaled = pixmap.scaled(
            target_size,
            qtc.Qt.AspectRatioMode.IgnoreAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation
        )

        # For border so it will look good (Because pixmap overrides css so i cant draw do border radius :<)
        rounded = qtg.QPixmap(target_size)
        rounded.fill(qtc.Qt.GlobalColor.transparent)
        painter = qtg.QPainter(rounded)
        painter.setRenderHint(qtg.QPainter.RenderHint.Antialiasing)
        path = qtg.QPainterPath()
        path.addRoundedRect(qtc.QRectF(rounded.rect()), 25, 25)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled)

        # Draw border
        pen = qtg.QPen(qtg.QColor("#3F4657"))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(qtc.Qt.BrushStyle.NoBrush)
        painter.drawRoundedRect(qtc.QRectF(rounded.rect()).adjusted(1, 1, -1, -1), 20, 20)

        painter.end()

        self.ui.label_sketch.setPixmap(rounded)

    def set_stars(self, count):
        stars = [self.ui.label_star1, self.ui.label_star2, self.ui.label_star3, self.ui.label_star4,
                 self.ui.label_star5]
        for i, star in enumerate(stars):
            if i < count:
                star.setPixmap(qtg.QPixmap(":/result/star_rate.svg"))
            else:
                star.setPixmap(qtg.QPixmap(":/result/star_unrated.svg"))

    def button_next_clicked(self):
        self.close()









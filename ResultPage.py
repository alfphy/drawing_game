import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import ui.playScene
import ui.resultScene


class ResultPage(qtw.QDialog):
    def __init__(self, parent, score=0, time_spent=0, target_phrase=""):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_next.clicked.connect(self.button_next_clicked)
        self.set_data(score, time_spent, target_phrase)
        self.setModal(True)

    def set_data(self, score, time_spent, target_phrase):
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

    def set_stars(self, count):
        stars = [self.ui.label_star1, self.ui.label_star2, self.ui.label_star3, self.ui.label_star4,
                 self.ui.label_star5]
        for i, star in enumerate(stars):
            if i < count:
                star.setPixmap(qtg.QPixmap(":/result/star_unrated.svg"))
            else:
                star.setPixmap(qtg.QPixmap(":/result/star_rated.svg"))

    def button_next_clicked(self):
        self.close()









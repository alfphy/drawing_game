import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import ui.playScene
import ui.resultScene


class ResultPage(qtw.QDialog):
    def __init__(self, parent, score=0, top_guess="", time_spent=0, target_phrase=""):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_next.clicked.connect(self.button_next_clicked)
        self.set_data(score, top_guess, time_spent, target_phrase)
        self.close()
        self.setWindowFlag(qtc.Qt.WindowType.FramelessWindowHint)
        self.setModal(True)

    def set_data(self, score, top_guess, time_spent, target_phrase):
        self.ui.label_5.setText(f"{int(score)}%")
        self.ui.label_3.setText(f"{time_spent}s")
        
        self.ui.label_ai_thinks.setText(f"AI thinks: {top_guess}")
        self.ui.label_target.setText(f"Target: {target_phrase}")
        
        if score >= 90:
            self.ui.label.setText("PERFECT!")
            self.set_stars(5)
        elif score >= 70:
            self.ui.label.setText("Good job!")
            self.set_stars(4)
        elif score >= 50:
            self.ui.label.setText("Not bad!")
            self.set_stars(3)
        elif score >= 30:
            self.ui.label.setText("Keep trying!")
            self.set_stars(2)
        else:
            self.ui.label.setText("Keep trying!")
            self.set_stars(1)

    def set_stars(self, count):
        stars = [self.ui.label_6, self.ui.label_7, self.ui.label_9, self.ui.label_8, self.ui.label_10]
        for i, star in enumerate(stars):
            if i < count:
                star.setStyleSheet("background:transparent; border:none;")
            else:
                star.setStyleSheet("opacity:0.3; background:transparent; border:none;")

    def button_next_clicked(self):
        self.close()









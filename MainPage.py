import PyQt6.QtWidgets as qtw

import roundsetting.game_state
import ui.mainPage
from roundsetting.game_state import game_config


class MainPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.mainPage.Ui_mainMenu()
        self.ui.setupUi(self)
        self.ui.button_easy.clicked.connect(self.button_easy_click)
        self.ui.button_medium.clicked.connect(self.button_medium_click)
        self.ui.button_hard.clicked.connect(self.button_hard_click)



    def button_easy_click(self):
        roundsetting.game_state.game_config = roundsetting.game_state.GameConfig(0, None)
        self.parent.ui.stack_pages.setCurrentIndex(1)

    def button_medium_click(self):
        roundsetting.game_state.game_config = roundsetting.game_state.GameConfig(1, None)

        self.parent.ui.stack_pages.setCurrentIndex(1)


    def button_hard_click(self):
        roundsetting.game_state.game_config = roundsetting.game_state.GameConfig(2, None)

        self.parent.ui.stack_pages.setCurrentIndex(1)

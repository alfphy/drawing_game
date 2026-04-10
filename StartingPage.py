import PyQt6.QtWidgets as qtw
import ui.startingScene
from PlayPage import PlayPage
import analyzer

class StartingPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.startingScene.Ui_startingScene()
        self.ui.setupUi(self)
        self.ui.button_start.clicked.connect(self.button_start_click)


    def button_start_click(self):
        self.parent.ui.stack_pages.setCurrentIndex(2)

        self.parent.playPage.start_timer(5)


import PyQt6.QtWidgets as qtw
import ui.startingScene

# DO NOT import "from main import window" here

class StartingPages(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.startingScene.Ui_startingScene()
        self.ui.setupUi(self)
        self.ui.button_start.clicked.connect(self.button_starting)


    def button_starting(self):
        self.parent.ui.stack_pages.setCurrentIndex(4)
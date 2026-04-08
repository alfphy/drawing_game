import PyQt6.QtWidgets as qtw
import ui.playScene

# DO NOT import "from main import window" here

class PlayPages(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.playScene.Ui_playScene()
        self.ui.setupUi(self)


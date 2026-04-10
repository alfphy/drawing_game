import PyQt6.QtWidgets as qtw

import ui.playScene
import ui.resultScene


class ResultPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_resultPage()
        self.ui.setupUi(self)









import PyQt6.QtWidgets as qtw
import ui as ui


class MainPage(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.mainPage.Ui_mainMenu()
        self.ui.setupUi(self)
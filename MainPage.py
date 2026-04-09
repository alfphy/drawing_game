import PyQt6.QtWidgets as qtw
import ui.mainPage



class MainPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.mainPage.Ui_mainMenu()
        self.ui.setupUi(self)
        self.ui.button_easy.clicked.connect(self.button_easy_click)

    def button_easy_click(self):
        self.parent.ui.stack_pages.setCurrentIndex(1)


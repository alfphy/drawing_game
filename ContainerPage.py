import sys
import PyQt6.QtWidgets as qtw
import ui.containerForm

from MainPage import MainPage
from PlayPage import PlayPage
from StartingPage import StartingPage

class ContainerPage(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.containerForm.Ui_ContainerForm()
        self.ui.setupUi(self)
        self.mainPage = MainPage(self)
        self.startingPage = StartingPage(self)
        self.playPage = PlayPage(self)
        self.ui.stack_pages.addWidget(self.mainPage)
        self.ui.stack_pages.addWidget(self.startingPage)
        self.ui.stack_pages.addWidget(self.playPage)
        self.ui.stack_pages.setCurrentIndex(0)

app = qtw.QApplication(sys.argv)
container_window = ContainerPage()
container_window.show()
app.exec()
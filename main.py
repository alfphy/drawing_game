import sys
import PyQt6.QtWidgets as qtw
import ui.containerForm

from MainPage import MainPages
from PlayPage import PlayPages
from StartingPage import StartingPages

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.containerForm.Ui_ContainerForm()
        self.ui.setupUi(self)
        self.ui.stack_pages.addWidget(MainPages(self))
        self.ui.stack_pages.addWidget(StartingPages(self))
        self.ui.stack_pages.addWidget(PlayPages())
        self.ui.stack_pages.setCurrentIndex(2)

app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
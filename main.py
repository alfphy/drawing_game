import sys

import PyQt6.QtWidgets as qtw
import ui.containerForm
from ui import containerForm


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = containerForm.Ui_ContainerForm()
        self.ui.setupUi(self)
        #hi

app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
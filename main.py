import sys
from os import supports_dir_fd
from pstats import add_func_stats

import PyQt6.QtWidgets as qtw
import ui.containerForm
from ui import containerForm


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = containerForm.Ui_ContainerForm()
        self.ui.setupUi(self)
        #hi

        asdfkjashdf
        asdfasdf
        add_func_stats(supports_dir_fd
                       )

app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
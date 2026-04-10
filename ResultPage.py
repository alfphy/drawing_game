import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui

import analyzer.clip_process
import ui.playScene
import numpy as np
import analyzer.phrases
import time
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QColorDialog, QPushButton


class ResultPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_resultPage()
        self.ui.setupUi(self)









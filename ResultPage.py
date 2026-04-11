import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import ui.playScene
import ui.resultScene


class ResultPage(qtw.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.resultScene.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_next.clicked.connect(self.button_next_clicked)
        self.close()
        self.setWindowFlag(qtc.Qt.WindowType.FramelessWindowHint)
        self.setModal(True)

    def button_next_clicked(self):
        self.close()









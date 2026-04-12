import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
from PyQt6.QtGui import QPalette , QColor
import ui.containerForm

from MainPage import MainPage
from PlayPage import PlayPage
from ResultPage import ResultPage
from StartingPage import StartingPage
from PyQt6.QtCore import QTimer
class ContainerPage(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = ui.containerForm.Ui_ContainerForm()
        self.ui.setupUi(self)
        for i in range(self.ui.stack_pages.count()):
            self.ui.stack_pages.removeWidget(self.ui.stack_pages.widget(0))
        self.setWindowFlags(
            qtc.Qt.WindowType.Window |
            qtc.Qt.WindowType.WindowCloseButtonHint |
            qtc.Qt.WindowType.WindowMinimizeButtonHint |
            qtc.Qt.WindowType.WindowMaximizeButtonHint
        )
        self.mainPage = MainPage(self)
        self.startingPage = StartingPage(self)
        self.playPage = PlayPage(self)
        self.ui.stack_pages.addWidget(self.mainPage)
        self.ui.stack_pages.addWidget(self.startingPage)
        self.ui.stack_pages.addWidget(self.playPage)
        self.ui.button_menu.setVisible(False)

        self.ui.button_menu.clicked.connect(self.button_menu_clicked)
        self.ui.stack_pages.currentChanged.connect(self.pages_changed)

        self.ui.stack_pages.setCurrentIndex(0)

    def pages_changed(self):
        if self.ui.stack_pages.currentIndex() == 0:
            self.ui.button_menu.setVisible(False)
        else:
            self.ui.button_menu.setVisible(True)


    def button_menu_clicked(self):
        if self.ui.stack_pages.currentIndex() == 0 :
            return
        if self.ui.stack_pages.currentIndex() == 2:
            self.playPage.done_drawing()
        self.ui.stack_pages.setCurrentIndex(self.ui.stack_pages.currentIndex() - 1)

    # def showEvent(self, event):
    #     super().showEvent(event)
    #     QTimer.singleShot(0, self.force_geometry_then_maximize)
    # #
    # def changeEvent(self, event):
    #     if event.type() == qtc.QEvent.Type.WindowStateChange:
    #         # Only react when it becomes maximized
    #         if self.windowState() & qtc.Qt.WindowState.WindowMaximized:
    #             QTimer.singleShot(0, self.force_geometry_then_maximize)
    #
    #     super().changeEvent(event)

    def force_geometry_then_maximize(self):
        screen = self.screen()
        if screen:
            geo = screen.availableGeometry()
            self.setGeometry(geo)

        QTimer.singleShot(0, lambda: self.setWindowState(
            qtc.Qt.WindowState.WindowMaximized
        ))

app = qtw.QApplication(sys.argv)
container_window = ContainerPage()
container_window.setWindowState(
    qtc.Qt.WindowState.WindowMaximized
)
container_window.show()
app.exec()
import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui
import ui.playScene


class DrawingCanvas(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 300)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.painter = QtGui.QPainter(self.image)
        self.last_point = None
        self.brush_size = 3
        self.brush_color = QtCore.Qt.GlobalColor.black

    def resizeEvent(self, event):
        new_image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        new_image.fill(QtCore.Qt.GlobalColor.white)
        painter = QtGui.QPainter(new_image)
        painter.drawImage(0, 0, self.image)
        self.image = new_image
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.last_point:
            current_point = event.position().toPoint()
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brush_color, self.brush_size, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap, QtCore.Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(self.last_point, current_point)
            self.last_point = current_point
            self.update()

    def mouseReleaseEvent(self, event):
        self.last_point = None

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(0, 0, self.image)


class PlayPages(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui.playScene.Ui_playScene()
        self.ui.setupUi(self)
        self.ui.drawing_space.hide()
        self.canvas = DrawingCanvas()
        self.ui.verticalLayout_4.addWidget(self.canvas)


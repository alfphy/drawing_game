import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore, QtGui
import numpy as np

class DrawingCanvas(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setMinimumSize(640, 640)

        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format.Format_ARGB32)
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.last_point = None
        self.brush_size = 3
        self.brush_color = QtGui.QColor(0, 0, 0)
        self.is_eraser = False
        self.is_fill_mode = False

    def set_fill_mode(self, enabled: bool):
        self.is_fill_mode = enabled

    def flood_fill(self, x: int, y: int, fill_color: QtGui.QColor):
        width = self.image.width()
        height = self.image.height()

        if x < 0 or x >= width or y < 0 or y >= height:
            return

        target_color = self.image.pixelColor(x, y)
        if target_color == fill_color:
            return

        ptr = self.image.bits()
        ptr.setsize(height * width * 4)
        arr = np.array(ptr).reshape(height, width, 4)

        queue = [(y, x)]
        visited = set()
        visited.add((y, x))

        while queue:
            cy, cx = queue.pop(0)

            if arr[cy, cx, 0] == target_color.blue() and arr[cy, cx, 1] == target_color.green() and arr[
                cy, cx, 2] == target_color.red():
                arr[cy, cx, 0] = fill_color.blue()
                arr[cy, cx, 1] = fill_color.green()
                arr[cy, cx, 2] = fill_color.red()
                arr[cy, cx, 3] = 255

                if cy > 0 and (cy - 1, cx) not in visited:
                    queue.append((cy - 1, cx))
                    visited.add((cy - 1, cx))
                if cy < height - 1 and (cy + 1, cx) not in visited:
                    queue.append((cy + 1, cx))
                    visited.add((cy + 1, cx))
                if cx > 0 and (cy, cx - 1) not in visited:
                    queue.append((cy, cx - 1))
                    visited.add((cy, cx - 1))
                if cx < width - 1 and (cy, cx + 1) not in visited:
                    queue.append((cy, cx + 1))
                    visited.add((cy, cx + 1))

        ptr[:] = arr.tobytes()
        self.update()

    def set_eraser_mode(self, enabled: bool):
        self.is_eraser = enabled

    def toggle_eraser(self):
        self.is_eraser = not self.is_eraser
        return self.is_eraser

    def clear(self):
        self.image.fill(QtCore.Qt.GlobalColor.white)
        self.update()

    def is_empty(self):
        width = self.image.width()
        height = self.image.height()
        ptr = self.image.bits()
        ptr.setsize(height * width * 4)
        arr = np.array(ptr).reshape(height, width, 4)
        non_white = np.any(arr != [255, 255, 255, 255], axis=2)
        return not np.any(non_white)

    def mousePressEvent(self, event):
        if self.parent.time_left == 0:
            print("time out")
        else:
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                if self.is_fill_mode:
                    x = int(event.position().x())
                    y = int(event.position().y())
                    self.flood_fill(x, y, self.brush_color)
                else:
                    self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.parent.time_left == 0:
            print("time out")
        else:
            if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.last_point:
                current_point = event.position().toPoint()
                painter = QtGui.QPainter(self.image)
                draw_color = QtCore.Qt.GlobalColor.white if self.is_eraser else self.brush_color
                painter.setPen(QtGui.QPen(draw_color, self.brush_size, QtCore.Qt.PenStyle.SolidLine,
                                          QtCore.Qt.PenCapStyle.RoundCap, QtCore.Qt.PenJoinStyle.RoundJoin))
                painter.drawLine(self.last_point, current_point)
                self.last_point = current_point
                self.update()

    def mouseReleaseEvent(self, event):
        self.last_point = None

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(0, 0, self.image)

    def save_image(self):
        # Convert QImage to numpy array
        width = self.image.width()
        height = self.image.height()
        ptr = self.image.bits()
        ptr.setsize(height * width * 4)  # ARGB32 = 4 bytes per pixel
        arr = np.array(ptr).reshape(height, width, 4)

        # Find non-white pixels (alpha > 0 and not white)
        # White = [255, 255, 255, 255]
        non_white = np.any(arr != [255, 255, 255, 255], axis=2)

        if not np.any(non_white):
            print("Canvas is empty!")
            return

        # Find bounding box of non-white pixels
        rows = np.any(non_white, axis=1)
        cols = np.any(non_white, axis=0)

        y_min, y_max = np.where(rows)[0][[0, -1]]
        x_min, x_max = np.where(cols)[0][[0, -1]]

        # Add padding (optional)
        padding = 10
        y_min = max(0, y_min - padding)
        y_max = min(height - 1, y_max + padding)
        x_min = max(0, x_min - padding)
        x_max = min(width - 1, x_max + padding)

        # Crop the image
        cropped = self.image.copy(x_min, y_min, x_max - x_min + 1, y_max - y_min + 1)

        # Save
        cropped.save('draw.png')
        print(f"Image cropped and saved! ({x_max - x_min + 1}x{y_max - y_min + 1})")
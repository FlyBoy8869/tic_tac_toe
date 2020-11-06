from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class CustomLabel(QLabel):
    clicked = pyqtSignal(QLabel, int)
    enter = pyqtSignal(QLabel)
    leave = pyqtSignal(QLabel)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setScaledContents(True)
        self.player_image_set = False

    # public interface ===============================

    def reset(self):
        self.player_image_set = False
        self.clear()

    def set_player_pixmap(self, pixmap):
        self.setPixmap(pixmap)
        self.player_image_set = True

    # protected interface ============================

    def enterEvent(self, event: QtCore.QEvent) -> None:
        self.enter.emit(self)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.leave.emit(self)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        index = int(self.accessibleName().split('_')[-1])
        self.clicked.emit(self, index)

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .designerforms.winner_ui import Ui_Dialog


class WinnerDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, pixmap, draw=False):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.player.setPixmap(pixmap)
        if draw:
            self.label_wins.setVisible(False)

        self.show()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.accept()

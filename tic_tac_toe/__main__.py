import sys

from PyQt5.QtWidgets import QApplication

from . import __version__
from .gui.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(f"Tic-Tac_Toe - v{__version__}")
    sys.exit(app.exec())

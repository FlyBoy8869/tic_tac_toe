from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QDialog

import tic_tac_toe.gui.helpers as helpers
from .designerforms import mainwindow_ui
from .customwidgets import CustomLabel
from .winnerdialog import WinnerDialog


class MainWindow(QDialog, mainwindow_ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._game_finished = False
        self._moves_made = None
        self._o_turn = None

        self._o_pixmap = QPixmap("resources/images/o.png")
        self._x_pixmap = QPixmap("resources/images/x.png")
        self._pixmap_game_over = QPixmap("resources/images/game_over_2.png")

        self._sound_invalid_move = QSound("resources/sounds/invalid_move.wav")
        self._sound_placed_token = QSound("resources/sounds/place_token_2.wav")

        self._position_labels = [
            self.position_top_left,
            self.position_top_center,
            self.position_top_right,
            self.position_middle_left,
            self.position_middle_center,
            self.position_middle_right,
            self.position_bottom_left,
            self.position_bottom_center,
            self.position_bottom_right
        ]

        helpers.connect_position_label_clicked_signals(self._position_labels, self._label_clicked_handler)
        helpers.connect_position_label_enter_signals(self._position_labels, self._label_enter_handler)
        helpers.connect_position_label_leave_signals(self._position_labels, self._label_leave_handler)

        self._game_grid = self._new_game_grid()
        self._new_game()

        self.show()

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_N:
            self._new_game()
        else:
            super().keyReleaseEvent(event)

    def _check_for_winner(self, player):
        draw = 0
        combos = [
            slice(0, 3),
            slice(3, 6),
            slice(6, 9),
            slice(0, 9, 3),
            slice(1, 9, 3),
            slice(2, 9, 3),
            slice(0, 9, 4),
            slice(2, 9, 2)
        ]

        for combination in combos:
            positions = self._game_grid[combination][0:3]
            if positions == [player, player, player]:
                return player

            if all(positions):
                draw += 1
                if draw == 8:
                    return "draw"

        return None

    def _clear_display_grid(self):
        for label in [child for child in self.grid_container.children() if isinstance(child, CustomLabel)]:
            label.reset()

    def _game_over(self, winner_pixmap, draw=False):
        dialog = WinnerDialog(self, winner_pixmap, draw)
        dialog.exec()

        self._game_finished = True
        self._new_game()

    def _label_enter_handler(self, label: CustomLabel):
        if not label.pixmap():
            pixmap = self._o_pixmap if self._o_turn else self._x_pixmap
            label.setPixmap(pixmap)

    @staticmethod
    def _label_leave_handler(label: CustomLabel):
        if label.pixmap() and not label.player_image_set:
            label.clear()

    def _label_clicked_handler(self, label: CustomLabel, index: int) -> None:
        if not self._game_finished:
            if self._o_turn:
                self._process_turn(label, "O", index)
            else:
                self._process_turn(label, "X", index)

    def _new_game(self):
        self._clear_display_grid()
        self._game_grid = self._new_game_grid()
        self._o_turn = False
        self._game_finished = False

    @staticmethod
    def _new_game_grid():
        return [""] * 9

    def _process_turn(self, label: CustomLabel, player: str, index: int):
        if not self._is_valid_move(index):
            if self._sound_invalid_move.isFinished():
                self._sound_invalid_move.play()
            return

        self._sound_placed_token.play()
        self._game_grid[index] = player

        pixmap = self._o_pixmap if player == "O" else self._x_pixmap
        label.set_player_pixmap(pixmap)

        # check and/or report result of player move
        result = self._check_for_winner(player)
        if result == player:
            QTimer.singleShot(100, lambda: self._game_over(pixmap))
        elif result == "draw":
            self._game_over(self._pixmap_game_over, draw=True)

        # let the other guy have a turn
        self._o_turn = not self._o_turn

    def _is_valid_move(self, index: int):
        return self._game_grid[index] == ""

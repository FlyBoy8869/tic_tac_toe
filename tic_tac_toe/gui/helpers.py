from typing import List

from tic_tac_toe.gui.customwidgets import CustomLabel


def _connect_signals(signals, handler):
    for signal in signals:
        signal.connect(handler)


def connect_position_label_clicked_signals(position_labels: List[CustomLabel], handler):
    _connect_signals([position_label.clicked for position_label in position_labels], handler)


def connect_position_label_enter_signals(position_labels: List[CustomLabel], handler):
    _connect_signals([position_label.enter for position_label in position_labels], handler)


def connect_position_label_leave_signals(position_labels: List[CustomLabel], handler):
    _connect_signals([position_label.leave for position_label in position_labels], handler)

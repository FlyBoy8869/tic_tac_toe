# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 608)
        self.grid_container = QtWidgets.QFrame(Dialog)
        self.grid_container.setGeometry(QtCore.QRect(20, 20, 601, 571))
        self.grid_container.setFrameShape(QtWidgets.QFrame.Box)
        self.grid_container.setLineWidth(6)
        self.grid_container.setObjectName("grid_container")
        self.position_bottom_right = CustomLabel(self.grid_container)
        self.position_bottom_right.setGeometry(QtCore.QRect(410, 380, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_bottom_right.sizePolicy().hasHeightForWidth())
        self.position_bottom_right.setSizePolicy(sizePolicy)
        self.position_bottom_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_bottom_right.setAlignment(QtCore.Qt.AlignCenter)
        self.position_bottom_right.setObjectName("position_bottom_right")
        self.position_bottom_center = CustomLabel(self.grid_container)
        self.position_bottom_center.setGeometry(QtCore.QRect(230, 380, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_bottom_center.sizePolicy().hasHeightForWidth())
        self.position_bottom_center.setSizePolicy(sizePolicy)
        self.position_bottom_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_bottom_center.setAlignment(QtCore.Qt.AlignCenter)
        self.position_bottom_center.setObjectName("position_bottom_center")
        self.position_top_center = CustomLabel(self.grid_container)
        self.position_top_center.setGeometry(QtCore.QRect(230, 40, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_top_center.sizePolicy().hasHeightForWidth())
        self.position_top_center.setSizePolicy(sizePolicy)
        self.position_top_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_top_center.setAlignment(QtCore.Qt.AlignCenter)
        self.position_top_center.setObjectName("position_top_center")
        self.position_middle_center = CustomLabel(self.grid_container)
        self.position_middle_center.setGeometry(QtCore.QRect(230, 210, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_middle_center.sizePolicy().hasHeightForWidth())
        self.position_middle_center.setSizePolicy(sizePolicy)
        self.position_middle_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_middle_center.setAlignment(QtCore.Qt.AlignCenter)
        self.position_middle_center.setObjectName("position_middle_center")
        self.position_top_right = CustomLabel(self.grid_container)
        self.position_top_right.setGeometry(QtCore.QRect(410, 40, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_top_right.sizePolicy().hasHeightForWidth())
        self.position_top_right.setSizePolicy(sizePolicy)
        self.position_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_top_right.setAlignment(QtCore.Qt.AlignCenter)
        self.position_top_right.setObjectName("position_top_right")
        self.position_middle_left = CustomLabel(self.grid_container)
        self.position_middle_left.setGeometry(QtCore.QRect(40, 210, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_middle_left.sizePolicy().hasHeightForWidth())
        self.position_middle_left.setSizePolicy(sizePolicy)
        self.position_middle_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_middle_left.setAlignment(QtCore.Qt.AlignCenter)
        self.position_middle_left.setObjectName("position_middle_left")
        self.position_bottom_left = CustomLabel(self.grid_container)
        self.position_bottom_left.setGeometry(QtCore.QRect(40, 380, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_bottom_left.sizePolicy().hasHeightForWidth())
        self.position_bottom_left.setSizePolicy(sizePolicy)
        self.position_bottom_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_bottom_left.setAlignment(QtCore.Qt.AlignCenter)
        self.position_bottom_left.setObjectName("position_bottom_left")
        self.position_top_left = CustomLabel(self.grid_container)
        self.position_top_left.setGeometry(QtCore.QRect(40, 40, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_top_left.sizePolicy().hasHeightForWidth())
        self.position_top_left.setSizePolicy(sizePolicy)
        self.position_top_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_top_left.setAlignment(QtCore.Qt.AlignCenter)
        self.position_top_left.setObjectName("position_top_left")
        self.label = QtWidgets.QLabel(self.grid_container)
        self.label.setGeometry(QtCore.QRect(30, 190, 541, 20))
        self.label.setFrameShape(QtWidgets.QFrame.HLine)
        self.label.setLineWidth(4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.grid_container)
        self.label_2.setGeometry(QtCore.QRect(30, 360, 541, 20))
        self.label_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_2.setLineWidth(4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.grid_container)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 20, 531))
        self.label_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_3.setLineWidth(4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.grid_container)
        self.label_4.setGeometry(QtCore.QRect(390, 20, 16, 531))
        self.label_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_4.setLineWidth(4)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.position_middle_right = CustomLabel(self.grid_container)
        self.position_middle_right.setGeometry(QtCore.QRect(410, 210, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_middle_right.sizePolicy().hasHeightForWidth())
        self.position_middle_right.setSizePolicy(sizePolicy)
        self.position_middle_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.position_middle_right.setAlignment(QtCore.Qt.AlignCenter)
        self.position_middle_right.setObjectName("position_middle_right")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.position_bottom_right.setAccessibleName(_translate("Dialog", "bottom_right_8"))
        self.position_bottom_right.setText(_translate("Dialog", "BottomRight"))
        self.position_bottom_center.setAccessibleName(_translate("Dialog", "bottom_center_7"))
        self.position_bottom_center.setText(_translate("Dialog", "BottomCenter"))
        self.position_top_center.setAccessibleName(_translate("Dialog", "top_center_1"))
        self.position_top_center.setText(_translate("Dialog", "TopCenter"))
        self.position_middle_center.setAccessibleName(_translate("Dialog", "middle_center_4"))
        self.position_middle_center.setText(_translate("Dialog", "MiddleCenter"))
        self.position_top_right.setAccessibleName(_translate("Dialog", "top_right_2"))
        self.position_top_right.setText(_translate("Dialog", "TopRight"))
        self.position_middle_left.setAccessibleName(_translate("Dialog", "middle_left_3"))
        self.position_middle_left.setText(_translate("Dialog", "MiddleLeft"))
        self.position_bottom_left.setAccessibleName(_translate("Dialog", "bottom_left_6"))
        self.position_bottom_left.setText(_translate("Dialog", "BottomLeft"))
        self.position_top_left.setAccessibleName(_translate("Dialog", "top_left_0"))
        self.position_top_left.setText(_translate("Dialog", "TopLeft"))
        self.position_middle_right.setAccessibleName(_translate("Dialog", "middle_right_5"))
        self.position_middle_right.setText(_translate("Dialog", "MiddleRight"))
from tic_tac_toe.gui.customwidgets import CustomLabel

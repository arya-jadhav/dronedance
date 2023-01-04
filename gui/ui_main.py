# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\main_singleGestureCombo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modules import HandGestureModule
from gui.widgets.notification import Notification


class Ui_MainWindow(object):
    def __init__(self, window: QtWidgets.QMainWindow):
        object.__init__(self)
        self.window = window
        self.NOTIFICATION_LIMIT = 1
        self.notification_displayed = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet("background-color: rgb(56, 58, 89);    \n"
"color: rgb(255, 255, 255);")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_instructions = QtWidgets.QWidget()
        self.page_instructions.setObjectName("page_instructions")
        self.formLayout = QtWidgets.QFormLayout(self.page_instructions)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setObjectName("formLayout")
        self.button_proceed = QtWidgets.QPushButton(self.page_instructions)
        self.button_proceed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_proceed.setStyleSheet("background-color: rgb(0, 209, 190);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.button_proceed.setObjectName("button_proceed")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button_proceed)
        self.label_description = QtWidgets.QLabel(self.page_instructions)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_description.setFont(font)
        self.label_description.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_description)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.stackedWidget.addWidget(self.page_instructions)
        self.page_capture = QtWidgets.QWidget()
        self.page_capture.setObjectName("page_capture")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_capture)
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_vidCapture = QtWidgets.QVBoxLayout()
        self.verticalLayout_vidCapture.setObjectName("verticalLayout_vidCapture")
        self.frame_vidCapture = QtWidgets.QFrame(self.page_capture)
        self.frame_vidCapture.setStyleSheet("background-color: rgb(98, 114, 164);\n"
"border-radius: 10px;")
        self.frame_vidCapture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vidCapture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vidCapture.setObjectName("frame_vidCapture")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_vidCapture)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_vidCapture = QtWidgets.QLabel(self.frame_vidCapture)
        self.label_vidCapture.setStyleSheet("border-radius: 10px;")
        self.label_vidCapture.setText("")
        self.label_vidCapture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vidCapture.setObjectName("label_vidCapture")
        self.verticalLayout.addWidget(self.label_vidCapture)
        self.verticalLayout_vidCapture.addWidget(self.frame_vidCapture)
        self.gridLayout_2.addLayout(self.verticalLayout_vidCapture, 0, 0, 1, 1)
        self.verticalLayout_stats = QtWidgets.QVBoxLayout()
        self.verticalLayout_stats.setObjectName("verticalLayout_stats")
        self.frame_stats = QtWidgets.QFrame(self.page_capture)
        self.frame_stats.setStyleSheet("background-color: rgb(98, 114, 164);\n"
"border-radius: 10px;")
        self.frame_stats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stats.setObjectName("frame_stats")
        self.verticalLayout_stats.addWidget(self.frame_stats)
        self.gridLayout_2.addLayout(self.verticalLayout_stats, 1, 0, 1, 2)
        self.verticalLayout_info = QtWidgets.QVBoxLayout()
        self.verticalLayout_info.setObjectName("verticalLayout_info")
        self.frame_info = QtWidgets.QFrame(self.page_capture)
        self.frame_info.setStyleSheet("background-color: rgb(98, 114, 164);\n"
"border-radius: 10px;")
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_info)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_info_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_info_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_info_2.setSpacing(14)
        self.verticalLayout_info_2.setObjectName("verticalLayout_info_2")
        self.frame_currentHandGesture = QtWidgets.QFrame(self.frame_info)
        self.frame_currentHandGesture.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_currentHandGesture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_currentHandGesture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_currentHandGesture.setObjectName("frame_currentHandGesture")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_currentHandGesture)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_info_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_info_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_info_3.setSpacing(0)
        self.verticalLayout_info_3.setObjectName("verticalLayout_info_3")
        self.frame_handGesture_top = QtWidgets.QFrame(self.frame_currentHandGesture)
        self.frame_handGesture_top.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"border-radius: 0px;")
        self.frame_handGesture_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_handGesture_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_handGesture_top.setObjectName("frame_handGesture_top")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_handGesture_top)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_handGesture_title = QtWidgets.QLabel(self.frame_handGesture_top)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_handGesture_title.setFont(font)
        self.label_handGesture_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_handGesture_title.setObjectName("label_handGesture_title")
        self.gridLayout_3.addWidget(self.label_handGesture_title, 0, 0, 1, 1)
        self.verticalLayout_info_3.addWidget(self.frame_handGesture_top)
        self.frame_handGesture_bottom = QtWidgets.QFrame(self.frame_currentHandGesture)
        self.frame_handGesture_bottom.setStyleSheet("border-width : 10px 1px 10px 1px;")
        self.frame_handGesture_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_handGesture_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_handGesture_bottom.setObjectName("frame_handGesture_bottom")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_handGesture_bottom)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_handGesture_prediction = QtWidgets.QLabel(self.frame_handGesture_bottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_handGesture_prediction.setFont(font)
        self.label_handGesture_prediction.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_handGesture_prediction.setText("")
        self.label_handGesture_prediction.setTextFormat(QtCore.Qt.PlainText)
        self.label_handGesture_prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_handGesture_prediction.setObjectName("label_handGesture_prediction")
        self.gridLayout_4.addWidget(self.label_handGesture_prediction, 0, 0, 1, 1)
        self.verticalLayout_info_3.addWidget(self.frame_handGesture_bottom)
        self.verticalLayout_info_3.setStretch(0, 1)
        self.verticalLayout_info_3.setStretch(1, 2)
        self.verticalLayout_5.addLayout(self.verticalLayout_info_3)
        self.verticalLayout_info_2.addWidget(self.frame_currentHandGesture)
        self.frame_gestureCaptured = QtWidgets.QFrame(self.frame_info)
        self.frame_gestureCaptured.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.frame_gestureCaptured.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gestureCaptured.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gestureCaptured.setObjectName("frame_gestureCaptured")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_gestureCaptured)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_info_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_info_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_info_4.setSpacing(0)
        self.verticalLayout_info_4.setObjectName("verticalLayout_info_4")
        self.frame_gestureCaptured_top = QtWidgets.QFrame(self.frame_gestureCaptured)
        self.frame_gestureCaptured_top.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"border-radius: 0px;")
        self.frame_gestureCaptured_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gestureCaptured_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gestureCaptured_top.setObjectName("frame_gestureCaptured_top")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_gestureCaptured_top)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_gestureCaptured_title = QtWidgets.QLabel(self.frame_gestureCaptured_top)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_gestureCaptured_title.setFont(font)
        self.label_gestureCaptured_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gestureCaptured_title.setObjectName("label_gestureCaptured_title")
        self.gridLayout_5.addWidget(self.label_gestureCaptured_title, 0, 0, 1, 1)
        self.verticalLayout_info_4.addWidget(self.frame_gestureCaptured_top)
        self.frame_gestureCaptured_bottom = QtWidgets.QFrame(self.frame_gestureCaptured)
        self.frame_gestureCaptured_bottom.setStyleSheet("border-width : 10px 1px 10px 1px;")
        self.frame_gestureCaptured_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gestureCaptured_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gestureCaptured_bottom.setObjectName("frame_gestureCaptured_bottom")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_gestureCaptured_bottom)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_gestureCaptured_output = QtWidgets.QLabel(self.frame_gestureCaptured_bottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_gestureCaptured_output.setFont(font)
        self.label_gestureCaptured_output.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_gestureCaptured_output.setText("")
        self.label_gestureCaptured_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gestureCaptured_output.setObjectName("label_gestureCaptured_output")
        self.gridLayout_6.addWidget(self.label_gestureCaptured_output, 0, 0, 1, 1)
        self.verticalLayout_info_4.addWidget(self.frame_gestureCaptured_bottom)
        self.verticalLayout_info_4.setStretch(0, 1)
        self.verticalLayout_info_4.setStretch(1, 2)
        self.verticalLayout_8.addLayout(self.verticalLayout_info_4)
        self.verticalLayout_info_2.addWidget(self.frame_gestureCaptured)
        self.frame_instructionToBeExecuted = QtWidgets.QFrame(self.frame_info)
        self.frame_instructionToBeExecuted.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.frame_instructionToBeExecuted.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_instructionToBeExecuted.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_instructionToBeExecuted.setObjectName("frame_instructionToBeExecuted")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_instructionToBeExecuted)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_info_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_info_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_info_5.setSpacing(0)
        self.verticalLayout_info_5.setObjectName("verticalLayout_info_5")
        self.frame_instructionToBeExecuted_top = QtWidgets.QFrame(self.frame_instructionToBeExecuted)
        self.frame_instructionToBeExecuted_top.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"border-radius: 0px;")
        self.frame_instructionToBeExecuted_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_instructionToBeExecuted_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_instructionToBeExecuted_top.setObjectName("frame_instructionToBeExecuted_top")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_instructionToBeExecuted_top)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_instructionToBeExecuted_title = QtWidgets.QLabel(self.frame_instructionToBeExecuted_top)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_instructionToBeExecuted_title.setFont(font)
        self.label_instructionToBeExecuted_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_instructionToBeExecuted_title.setObjectName("label_instructionToBeExecuted_title")
        self.gridLayout_11.addWidget(self.label_instructionToBeExecuted_title, 0, 0, 1, 1)
        self.verticalLayout_info_5.addWidget(self.frame_instructionToBeExecuted_top)
        self.frame_instructionToBeExecuted_bottom = QtWidgets.QFrame(self.frame_instructionToBeExecuted)
        self.frame_instructionToBeExecuted_bottom.setStyleSheet("border-width : 10px 1px 10px 1px;")
        self.frame_instructionToBeExecuted_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_instructionToBeExecuted_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_instructionToBeExecuted_bottom.setObjectName("frame_instructionToBeExecuted_bottom")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_instructionToBeExecuted_bottom)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_instructionToBeExecuted_output = QtWidgets.QLabel(self.frame_instructionToBeExecuted_bottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_instructionToBeExecuted_output.setFont(font)
        self.label_instructionToBeExecuted_output.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_instructionToBeExecuted_output.setText("")
        self.label_instructionToBeExecuted_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_instructionToBeExecuted_output.setObjectName("label_instructionToBeExecuted_output")
        self.gridLayout_12.addWidget(self.label_instructionToBeExecuted_output, 0, 0, 1, 1)
        self.verticalLayout_info_5.addWidget(self.frame_instructionToBeExecuted_bottom)
        self.verticalLayout_info_5.setStretch(0, 1)
        self.verticalLayout_info_5.setStretch(1, 2)
        self.verticalLayout_9.addLayout(self.verticalLayout_info_5)
        self.verticalLayout_info_2.addWidget(self.frame_instructionToBeExecuted)
        self.frame_prevInstructionToDrones = QtWidgets.QFrame(self.frame_info)
        self.frame_prevInstructionToDrones.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.frame_prevInstructionToDrones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prevInstructionToDrones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prevInstructionToDrones.setObjectName("frame_prevInstructionToDrones")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_prevInstructionToDrones)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_info_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_info_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_info_7.setSpacing(0)
        self.verticalLayout_info_7.setObjectName("verticalLayout_info_7")
        self.frame_prevInstructionToDrones_top = QtWidgets.QFrame(self.frame_prevInstructionToDrones)
        self.frame_prevInstructionToDrones_top.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"border-radius: 0px;")
        self.frame_prevInstructionToDrones_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prevInstructionToDrones_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prevInstructionToDrones_top.setObjectName("frame_prevInstructionToDrones_top")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_prevInstructionToDrones_top)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_prevInstructionToDrones_title = QtWidgets.QLabel(self.frame_prevInstructionToDrones_top)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_prevInstructionToDrones_title.setFont(font)
        self.label_prevInstructionToDrones_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prevInstructionToDrones_title.setObjectName("label_prevInstructionToDrones_title")
        self.gridLayout_7.addWidget(self.label_prevInstructionToDrones_title, 0, 0, 1, 1)
        self.verticalLayout_info_7.addWidget(self.frame_prevInstructionToDrones_top)
        self.frame_prevInstructionToDrones_bottom = QtWidgets.QFrame(self.frame_prevInstructionToDrones)
        self.frame_prevInstructionToDrones_bottom.setStyleSheet("border-width : 10px 1px 10px 1px;")
        self.frame_prevInstructionToDrones_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prevInstructionToDrones_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prevInstructionToDrones_bottom.setObjectName("frame_prevInstructionToDrones_bottom")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_prevInstructionToDrones_bottom)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_prevInstructionToDrones_output = QtWidgets.QLabel(self.frame_prevInstructionToDrones_bottom)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_prevInstructionToDrones_output.setFont(font)
        self.label_prevInstructionToDrones_output.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_prevInstructionToDrones_output.setText("")
        self.label_prevInstructionToDrones_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prevInstructionToDrones_output.setObjectName("label_prevInstructionToDrones_output")
        self.gridLayout_8.addWidget(self.label_prevInstructionToDrones_output, 0, 0, 1, 1)
        self.verticalLayout_info_7.addWidget(self.frame_prevInstructionToDrones_bottom)
        self.verticalLayout_info_7.setStretch(0, 1)
        self.verticalLayout_info_7.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout_info_7)
        self.verticalLayout_info_2.addWidget(self.frame_prevInstructionToDrones)
        self.verticalLayout_info_2.setStretch(0, 1)
        self.verticalLayout_info_2.setStretch(1, 1)
        self.verticalLayout_info_2.setStretch(2, 1)
        self.verticalLayout_info_2.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_info_2)
        self.verticalLayout_info.addWidget(self.frame_info)
        self.gridLayout_2.addLayout(self.verticalLayout_info, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page_capture)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Button Clicked
        self.button_proceed.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_capture))

        # Hand Gesture Module
        self.GestureModule = HandGestureModule()
        self.GestureModule.start()
        self.GestureModule.ImageUpdate.connect(self.UpdateVideoCapture)
        self.GestureModule.GesturePredictionUpdate.connect(self.UpdateGesturePrediction)
        self.GestureModule.mapper.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.connect(self.UpdateGestureCapturedAndInstructionToBeExecutedLabel)

        # Notification Widget
        self.GestureModule.mapper.emitter.SendNotification.connect(self.ShowNotification)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Drone Dance by Team MCS7"))
        self.button_proceed.setText(_translate("MainWindow", "CONTINUE"))
        self.label_description.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#00d1be;\">Welcome,</span></p><p><span style=\" font-size:12pt; color:#00d1be;\"><br/></span></p><p><span style=\" font-size:12pt; color:#00d1be;\">Before pressing the continue button, please make sure that you have a webcam and have already connected the drones via the router. Please see the user guide and follow the instructions carefully.</span></p><p><span style=\" font-size:12pt; color:#00d1be;\"><br/></span></p><p><span style=\" font-size:12pt; color:#00d1be;\">Thank you.</span></p></body></html>"))
        self.label_handGesture_title.setText(_translate("MainWindow", "Current Predicted Hand Gesture"))
        self.label_gestureCaptured_title.setText(_translate("MainWindow", "Gesture Captured"))
        self.label_instructionToBeExecuted_title.setText(_translate("MainWindow", "Instruction to be executed"))
        self.label_prevInstructionToDrones_title.setText(_translate("MainWindow", "Previous Instruction to Drone Swarm"))

    def ShowNotification(self, dct):
        if self.notification_displayed < self.NOTIFICATION_LIMIT:
                self.window.notification = Notification(display=dct['display'])
                self.window.notification.setNotify(dct['title'], dct['message'])
                # Calculate the position of window, and display the notification
                rect = QtCore.QRect(self.window.x() + round(self.window.width() / 2) - round(self.window.notification.width() / 2), 
                                                self.window.y() + 26, self.window.notification.msg.messageLabel.width() + 30, self.window.notification.msg.messageLabel.height())
                self.window.notification.setGeometry(rect)
                self.window.notification.emitter.NotificationDisplayed.connect(self.AllowNewNotification)
                self.notification_displayed = 1

    def AllowNewNotification(self, num):
                self.notification_displayed = num

    def UpdateVideoCapture(self, frame):
        self.label_vidCapture.setPixmap(QtGui.QPixmap.fromImage(frame))

    def UpdateGesturePrediction(self, prediction):
        self.label_handGesture_prediction.setText(prediction)

    def UpdateGestureCapturedAndInstructionToBeExecutedLabel(self, dct):
        if dct['do_reset']:
               self.label_gestureCaptured_output.setText('')
               self.label_instructionToBeExecuted_output.setText('')
        else:
               self.label_gestureCaptured_output.setText(dct['gesture_captured'])
               self.label_instructionToBeExecuted_output.setText(dct['instruction_to_be_executed'] if dct['instruction_to_be_executed'] is not None else '')
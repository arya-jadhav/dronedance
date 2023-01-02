from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from . mapper import instructioncopy as instruction

from tensorflow.python.keras.models import load_model

class HandGestureModule(QThread):
    ImageUpdate = pyqtSignal(QImage)
    GesturePredictionUpdate = pyqtSignal(str)
    scaled_size = QSize(490, 350)

    # Configure MediaPipe for Hand Gesture detection
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    # Load gesture recogniser model from TensorFlow
    model = load_model('HandGestureRecognition\mp_hand_gesture')

    # Load class names
    f = open('HandGestureRecognition\gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()

    # Load Mapping Module
    mapper = instruction.Instruction()

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            x, y, c = frame.shape
            if ret:
                frame = cv2.flip(frame, 1)
                framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Hand Gesture Detection and Classification
                # Get hand landmark prediction
                result = self.hands.process(framergb)
                
                className = ''

                # post process the result
                if result.multi_hand_landmarks:
                    landmarks = []
                    for handslms in result.multi_hand_landmarks:
                        for lm in handslms.landmark:
                            # Multiply width, height with normalised results from lm
                            lmx = int(lm.x * x)
                            lmy = int(lm.y * y)

                            landmarks.append([lmx, lmy])

                        # Drawing landmarks on frames
                        self.mpDraw.draw_landmarks(framergb, handslms, self.mpHands.HAND_CONNECTIONS)

                        # Predict gesture
                        prediction = self.model([landmarks])
                        classID = np.argmax(prediction)
                        className = self.classNames[classID]

                # Show the prediction on the frame
                # cv2.putText(framergb, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

                # Emit and update gesture prediction text in GUI
                # Look at the object name: label_handGesture_prediction
                self.GesturePredictionUpdate.emit(className)

                # Convert to QtFormat
                ConvertToQtFormat = QImage(framergb.data, framergb.shape[1], framergb.shape[0], QImage.Format_RGB888)
                ScaledFrame = ConvertToQtFormat.scaled(self.scaled_size, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledFrame)

                # Update Gesture Combination and map to drone instructions
                self.mapper.append_prediction(className)
                if self.mapper.identify_instruction():
                    self.mapper.carry_instruction()
                    self.mapper.check_combo()

    def stop(self):
        self.ThreadActive = False
        self.quit()

# class GestureStreaming(QLabel):
#     reSize = pyqtSignal(QSize)
#     def __init__(self, ParentWidget):
#         super(GestureStreaming, self).__init__()
#         self.initUI()

#     # def ImageUpdateSlot(self, Frame):
#     #     self.label_vidCapture.setPixmap(QPixmap.fromImage(Frame))

#     @pyqtSlot(QImage)
#     def setImage(self, Frame):
#         self.label_vidCapture.setPixmap(QPixmap.fromImage(Frame))

#     def initUI(self, ParentWidget):
#         self.setWindowTitle("Image")
#         # Create A Label
#         self.label_vidCapture = QLabel(ParentWidget)
#         self.label_vidCapture.setStyleSheet("border-radius: 10px;")
#         self.label_vidCapture.setText("")
#         self.label_vidCapture.setAlignment(Qt.AlignCenter)
#         self.label_vidCapture.setObjectName("label_vidCapture")

#         vidCap = HandGestureModule(self)
#         vidCap.ImageUpdate.connect(self.setImage)
#         self.reSize.connect(vidCap.scaled)
#         vidCap.start()

#     def resizeEvent(self, event):
#         print(self.size())
#         self.reSize.emit(self.size())
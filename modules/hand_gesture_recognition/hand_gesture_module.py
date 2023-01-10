from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from ..mapper import Instruction

from tensorflow.python.keras.models import load_model

class HandGestureModule(QThread):
    # Size of Video Capture in GUI
    scaled_size = QSize(490, 355)

    # Signals for label update in GUI
    ImageUpdate = pyqtSignal(QImage)
    GesturePredictionUpdate = pyqtSignal(str)

    # Configure MediaPipe for Hand Gesture detection
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    # Load gesture classifier model from TensorFlow
    model = load_model('.\modules\model\gesture_classifier.hdf5')

    # Load class names
    f = open('.\modules\model\gesture.names', 'r')
    class_names = f.read().split('\n')
    f.close()

    # Load Mapping Module
    mapper = Instruction()

    def pre_process_landmark(self, landmarks):
        '''
        Function:
        Pre-process information from MediaPipe Hands as input for gesture classifier
        '''
        # Convert to relative coordinates
        base_x, base_y = 0, 0
        for index, landmark_point in enumerate(landmarks):
            if index == 0:
                base_x, base_y = landmark_point[0], landmark_point[1]
            landmarks[index][0] = landmarks[index][0] - base_x
            landmarks[index][1] = landmarks[index][1] - base_y

        # Convert 2D array to 1D array
        landmarks = np.reshape(landmarks, -1)

        # Normalization
        max_value = max(list(map(abs, landmarks)))
        def normalize_(n):
            return n / max_value
        landmarks = list(map(normalize_, landmarks))
        return landmarks

    def run(self):
        '''
        Function: 
        In PyQt, this will be the function that runs when the thread is active.
        It's purpose is used to update the Video Capture in the GUI. Each frame 
        will be preprocessed to detect hand gestures using the Hand Gesture
        Detection module, then predict the gesture and finally map it to a
        drone instruction using the Mapper module.

        GUI display:
        In the GUI, user will be able to see the current predicted gesture, the
        current captured gesture and the following drone instruction to be
        executed.

        There will be a notification widget that notifies the user when an error
        occured, the drone instruction has been successfully executed and more...
        '''
        self.ThreadActive = True
        capture = cv2.VideoCapture(0) # Use first webcam on your device
        while self.ThreadActive:
            ret, frame = capture.read()
            width, height, c = frame.shape
            if ret:
                # Make frame not writeable to improve performance
                frame.flags.writeable = False
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Get hand landmark prediction
                result = self.hands.process(frame)

                frame.flags.writeable = True
                
                # Initialize class name
                class_name = ''

                # Post process the result
                if result.multi_hand_landmarks:
                    landmarks = []
                    for handslms in result.multi_hand_landmarks:
                        for lm in handslms.landmark:
                            # Multiply width, height with normalised results from lm
                            lmx = min(int(lm.x * width), width - 1)
                            lmy = min(int(lm.y * height), height - 1)

                            landmarks.append([lmx, lmy])

                        # Drawing landmarks on frames
                        self.mp_draw.draw_landmarks(frame, handslms, self.mp_hands.HAND_CONNECTIONS)

                        # Preprocess the landmarks and predict gesture
                        prediction = self.model.predict([self.pre_process_landmark(landmarks)])
                        class_id = np.argmax(prediction)
                        class_name = self.class_names[class_id]

                        # Obtain and identify instruction
                        self.mapper.append_prediction(class_name)
                        gesture = self.mapper.identify_gesture()

                        self.mapper.identify_instruction(gesture)
                    
                        if self.mapper.check_confirmation():
                            # Carry out instruction
                            self.mapper.carry_instruction()

                # Show the prediction on the frame
                # cv2.putText(framergb, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

                # Emit and update gesture prediction text in GUI
                # Look at the object name: label_handGesture_prediction
                self.GesturePredictionUpdate.emit(class_name)

                # Convert to QtFormat
                frame = cv2.flip(frame, 1) # Flip frame horizontally
                ConvertToQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                ScaledFrame = ConvertToQtFormat.scaled(self.scaled_size, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(ScaledFrame)

    def stop(self):
        self.ThreadActive = False
        self.quit()
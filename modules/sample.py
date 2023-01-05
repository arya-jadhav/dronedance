import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from instruction import Instruction
from tensorflow.python.keras.models import load_model


# Configure MediaPipe for Hand Gesture detection
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Load gesture recogniser model from TensorFlow
model = load_model('modules\model\gesture_classifier.hdf5')

# Load class names
f = open('modules\model\gesture.names', 'r')
classNames = f.read().split('\n')
f.close()

# Initialize the webcam for Hand Gesture Recognition Python project
vid = cv2.VideoCapture(0)
instruct = Instruction()

def pre_process_landmark(landmark_list):
    # Convert to relative coordinates
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]

        landmark_list[index][0] = landmark_list[index][0] - base_x
        landmark_list[index][1] = landmark_list[index][1] - base_y

    # Convert to 1D array
    landmark_list = np.reshape(landmark_list, -1)

    # Normalization
    max_value = max(list(map(abs, landmark_list)))

    def normalize_(n):
        return n / max_value

    landmark_list = list(map(normalize_, landmark_list))

    return landmark_list

while True:
    # Read each frame from the webcam
    _, frame = vid.read()
    width, height, c = frame.shape

    # Make frame not writeable to improve performance
    frame.flags.writeable = False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(frame)

    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # Multiply width, height with normalised results from lm
                lmx = min(int(lm.x * width), width - 1)
                lmy = min(int(lm.y * height), height - 1)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Preprocess the landmarks and predict gesture
            prediction = model.predict([pre_process_landmark(landmarks)])
            classID = np.argmax(prediction)
            className = classNames[classID]

            # Obtain and identify instruction
            instruct.append_prediction(className)
            gesture = instruct.identify_gesture()
            if gesture != "" and gesture != "okay":
                instruct.set_instruction_gesture(gesture)
                instruct.identify_instruction(gesture)
            elif gesture == "okay":
                # Carry out instruction
                instruct.carry_instruction()


    # show the prediction on the frame
    frame = cv2.flip(frame, 1) # Flip frame horizontally
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("Output", frame) 

    # Press 'q' to stop the program
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
vid.release()
cv2.destroyAllWindows()


import collections
from collections import Counter
from PyQt5.QtCore import *
# from modules.TelloMaster import tello

class Instruction:
    # Emitter signals for GUI
    class Emitter(QObject):
        GestureCapturedAndInstructionToBeExecutedLabelUpdate = pyqtSignal(dict)
        SendNotification = pyqtSignal(dict)
        def __init__(self):
            super(Instruction.Emitter, self).__init__()

    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.prediction_list = collections.deque(maxlen=25)
        self.instruction_gesture = ""
        self.confirmation_gesture = False

        # Initialize Emitter and dictionary
        self.emitter = Instruction.Emitter()
        self.gesture_signal = {
        'do_reset': False,
        'gesture_captured': None,
        'instruction_to_be_executed': None
        }
        self.notification_signal = {
                'display': 'standard',
                'title': '',
                'message': ''
        }

    def gesture_present(self):
        return (self.instruction_gesture != "")
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] # the element with the most frequency

    def identify_gesture(self):
        if len(self.prediction_list) == 25:
            gesture = self.most_freq(self.prediction_list)
            self.prediction_list.clear()
            if gesture != "okay":
                self.instruction_gesture = gesture
            return gesture

    def identify_instruction(self, gesture):
        if gesture != None:
            if gesture == "one":
                print("landing instruction")
                self.update_gui(self.instruction_gesture, drone_instruction='Landing', do_reset=False)
            elif gesture == "two":
                print("take off instruction")
            elif gesture == "three":
                print("three instruction")
            elif gesture == "fist":
                print("fist instruction")
            elif gesture == "thumbs up":
                print("thumbs up instruction")
            elif gesture == "thumbs down":
                print("thumbs down instruction")
            elif gesture == "stop":
                print("stop instruction")
            elif gesture == "rock":
                print("rock instruction")
            elif gesture == "finger gun":
                print("finger gun instruction")
            elif gesture == "okay":
                self.confirmation_gesture = True
                return
            print("okay to confirm")

            self.confirmation_gesture = False

    def set_instruction_gesture(self, gesture):
        self.instruction_gesture = gesture

    def append_prediction(self, element):
        self.prediction_list.append(element)

    def carry_instruction(self):
        self.confirmation_gesture = False
        if self.gesture_present():
            # Carry out instruction based on hand gesture
            if self.instruction_gesture == "one":
                self.one_instruction()   
            elif self.instruction_gesture == "two":
                self.two_instruction()
            elif self.instruction_gesture == "three":
                self.three_instruction()
            elif self.instruction_gesture == "fist":
                self.fist_instruction() 
            elif self.instruction_gesture == "thumbs up":
                self.thumbs_up_instruction()
            elif self.instruction_gesture == "thumbs down":
                self.thumbs_down_instruction()
            elif self.instruction_gesture == "stop":
                self.stop_instruction()
            elif self.instruction_gesture == "rock":
                self.rock_instruction()
            elif self.instruction_gesture == "finger gun":
                self.finger_gun_instruction()
            else:
                print("invalid gesture")
            self.instruction_gesture = ""
        else:
            print("no instruction given")
    
    def check_confirmation(self):
        return self.confirmation_gesture

    def one_instruction(self):
        print("one instruction received")
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Successfully executed \'Landing\' instruction.')

    def two_instruction(self):
        print("two instruction received")

    def three_instruction(self):
        print("three instruction received")

    def okay_instruction(self):
        print("okay instruction received")

    def fist_instruction(self):
        print("fist instruction received")

    def thumbs_up_instruction(self):
        print("thumbs up instruction received")

    def thumbs_down_instruction(self):
        print("thumbs down instruction received")

    def stop_instruction(self):
        print("stop instruction received")

    def rock_instruction(self):
        print("rock instruction received")

    def finger_gun_instruction(self):
        print("finger gun instruction received")

    def update_gui(self, gesture_name, drone_instruction=None, do_reset=False):
        if do_reset:
            self.gesture_signal['do_reset'] = do_reset
            self.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.emit(self.gesture_signal)

            # Update dict to intial values
            self.gesture_signal = {
            'do_reset': False,
            'gesture_captured': None,
            'instruction_to_be_executed': None
            }
        else:
            self.gesture_signal['gesture_captured'] = gesture_name
            self.gesture_signal['instruction_to_be_executed'] = drone_instruction
            self.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.emit(self.gesture_signal)

    def send_notification(self, display='standard', title='', message=''):
        self.notification_signal = {
                'display': display,
                'title': title,
                'message': message
        }
        self.emitter.SendNotification.emit(self.notification_signal)
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
        self.predictionLst = collections.deque(maxlen=10)
        self.current_gesture = ""

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

    def is_gesture(self):
        return (self.current_gesture != "")
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] #the element with the most frequency

    def identify_instruction(self):
        if len(self.predictionLst) > 7:
            self.current_gesture = self.most_freq(self.predictionLst)
            self.predictionLst.clear()
            return True

    def append_prediction(self, element):
        self.predictionLst.append(element)

    def carry_instruction(self):
        if self.is_gesture():
            # Carry out instruction based on hand gesture     
            if self.current_gesture == "two":
                self.two_instruction()
            elif self.current_gesture == "thumbs up":
                self.thumbs_up_instruction()
            elif self.current_gesture == "stop":
                self.stop_instruction()
            else:
                print("invalid gesture")
                self.update_gui(self.current_gesture, do_reset=True)
            
            self.current_gesture = ""

    def one_instruction(self):
        print("one instruction received")
        #drone instruction

    def two_instruction(self):
        print("two instruction received")
        self.update_gui(self.current_gesture, drone_instruction='Take off', do_reset=False)

    def three_instruction(self):
        print("three instruction received")
        #drone instruction

    def okay_instruction(self):
        print("okay instruction received")
        #drone instruction

    def fist_instruction(self):
        print("fist instruction received")
        #drone instruction

    def thumbs_up_instruction(self):
        print("thumbs up instruction received")
        self.update_gui(self.current_gesture, drone_instruction='Do a flip', do_reset=False)
        self.send_notification(display='success', title='Success!', message='Successfully executed \'Do a flip\' instruction.')

    def thumbs_down_instruction(self):
        print("thumbs down instruction received")
        #drone instruction

    def stop_instruction(self):
        print("stop instruction received")
        self.update_gui(self.current_gesture, drone_instruction='Land', do_reset=False)

    def rock_instruction(self):
        print("rock instruction received")
        #drone instruction

    def finger_gun_instruction(self):
        print("finger gun instruction received")
        #drone instruction

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
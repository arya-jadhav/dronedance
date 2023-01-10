import collections
from collections import Counter
from PyQt5.QtCore import *
from modules.mapper.basic_commands import DroneSwarm
# from modules.TelloMaster import tello

class Instruction:
    # Emitter signals for GUI
    class Emitter(QObject):
        GestureCapturedAndInstructionToBeExecutedLabelUpdate = pyqtSignal(dict)
        SendNotification = pyqtSignal(dict)
        PreviousInstructionToDronesLabelUpdate = pyqtSignal(str)
        def __init__(self):
            super(Instruction.Emitter, self).__init__()

    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.prediction_list = collections.deque(maxlen=25)
        self.instruction_gesture = ""
        self.confirmation_gesture = False
        self.drone_swarm = DroneSwarm()
        self.drone_swarm.initialize_drones()

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

        # Gesture to Instruction dictionary
        self.gesture_to_instruction = {
            'one': 'Take Off',
            'two': 'Fan Formation',
            'three' : 'Dance Formation',
            "fist" : 'Vertical Formation',
            "thumbs up" : 'Ice Cream Formation',
            "thumbs down" : 'Diamond Formation',
            "stop": 'Landing',
            "rock" : 'Ice Cream Instruction',
            "finger gun": 'Dance Instruction',
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
        instruction_identified = False
        if gesture is not None and self.gesture_present():
            if gesture == "one":
                instruction_identified = True
            elif gesture == "two":
               instruction_identified = True
            elif gesture == "three":
                instruction_identified = True
            elif gesture == "fist":
                instruction_identified = True
            elif gesture == "thumbs up":
                instruction_identified = True
            elif gesture == "thumbs down":
                instruction_identified = True
            elif gesture == "stop":
                instruction_identified = True
            elif gesture == "rock":
                instruction_identified = True
            elif gesture == "finger gun":
                instruction_identified = True
            elif gesture == "okay":
                self.okay_instruction()
                return
            else:
                self.update_gui(self.instruction_gesture, drone_instruction='Invalid Gesture', do_reset=False)
                self.send_notification(display='error', title='Invalid Gesture', message='Gesture predicted by the gesture classifier is an invalid gesture.')
                return

            if instruction_identified:
                self.update_gui(self.instruction_gesture, drone_instruction=self.gesture_to_instruction[gesture], do_reset=False)
                self.send_notification(display='information', title='Confirmation', message='Show the \'okay\' gesture to start executing the instruction or show a different gesture to change the instruction.')
                instruction_identified = False
                
            self.confirmation_gesture = False

    def set_instruction_gesture(self, gesture):
        self.instruction_gesture = gesture

    def append_prediction(self, element):
        self.prediction_list.append(element)

    def carry_instruction(self):
        # Reset confirmation gesture
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
                self.send_notification(display='error', title='Invalid Gesture', message='Unable to carry out instruction due to invalid gesture. Please try again.')
            
            # Update display for Prvious Drone Instruction in GUI
            self.update_previous_drone_instruction(prev_instruction=self.gesture_to_instruction[self.instruction_gesture])
            # Reset instruction gesture
            self.instruction_gesture = ""

    def check_confirmation(self):
        return self.confirmation_gesture        

    def one_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("take off instruction received")
        # Drone take off instruction
        self.drone_swarm.takeoff_drones()

    def two_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("fan formation instruction received")
        # Drone fan formation instruction
   
    def three_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("dance formation instruction received")
        # Drone dance formation instruction

    def okay_instruction(self):
        self.confirmation_gesture = True

    def fist_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("vertical formation instruction received")
        # Drone vertical formation instruction

    def thumbs_up_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("ice cream formation instruction received")
        # Drone ice cream formation instruction

    def thumbs_down_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("diamond formation instruction received")
        # Drone diamond formation instruction

    def stop_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("landing instruction received")
        # Drone land instruction
        self.drone_swarm.land_drones()

    def rock_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("ice cream instruction received")
        # Drone ice cream instruction

    def finger_gun_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='information', title='Executing drone instructions...', message='')
        print("dance instruction received")
        # Drone dance instruction

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
        
    def update_previous_drone_instruction(self, prev_instruction):
        self.emitter.PreviousInstructionToDronesLabelUpdate.emit(prev_instruction)

    def send_notification(self, display='standard', title='', message=''):
        self.notification_signal = {
                'display': display,
                'title': title,
                'message': message
        }
        self.emitter.SendNotification.emit(self.notification_signal)

    def close_socket(self):
        self.drone_swarm.end()
import collections
from collections import Counter
from PyQt5.QtCore import *
from ..formation import DroneSwarm

# NOTE: All code that allows the drones to execute drone instructions are COMMENTED OUT

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
        self.prediction_list = collections.deque(maxlen=20)
        self.instruction_gesture = "" # Current gesture captured
        self.confirmation_gesture = False # Check for confirmation gesture 
        self.drone_swarm = DroneSwarm() # Drone swarm instructions
        self.drone_swarm.initialize_drones() # Connect to drones and have them ready to accept instructions

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
            'two': 'Triangle Formation',
            'three' : 'Dance Formation',
            "fist" : 'Vertical Formation',
            "thumbs up" : 'Ice Cream Formation',
            "thumbs down" : 'Diamond Formation',
            "stop": 'Landing',
            "rock" : 'Ice Cream Instruction',
            "finger gun": 'Dance Instruction',
        }

    # Check if current gesture captured exists
    def gesture_present(self):
        return (self.instruction_gesture != "")
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] # the element with the most frequency

    # Identify the user's gesture
    def identify_gesture(self):
        if len(self.prediction_list) == 20: # Avoids capturing incorrect gesture
            gesture = self.most_freq(self.prediction_list)
            self.prediction_list.clear()
            if gesture != "okay": # Not confirmation gesture
                self.instruction_gesture = gesture
            return gesture

    # Identify the instruction associated with the gesture
    def identify_instruction(self, gesture):
        instruction_identified = False
        if gesture is not None and self.gesture_present():
            # Valid instruction gestures
            if (gesture == "one" or 
                gesture == "two" or 
                gesture == "three" or 
                gesture == "fist" or 
                gesture == "thumbs up" or 
                gesture == "thumbs down" or 
                gesture == "stop" or 
                gesture == "rock" or 
                gesture == "finger gun"):
                instruction_identified = True
            elif gesture == "okay": #confirmation gesture
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

    # Setter for current instruction gesture captured
    def set_instruction_gesture(self, gesture):
        self.instruction_gesture = gesture

    # Append predictions into deque
    def append_prediction(self, element):
        self.prediction_list.append(element)

    # Execute instruction
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

    # Check if confirmation gesture given
    def check_confirmation(self):
        return self.confirmation_gesture        

    # Instruction for one hand gesture
    def one_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("take off instruction received")
        # Drone take off instruction
        # self.drone_swarm.takeoff_drones()

    # Instruction for two hand gesture
    def two_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("triangle formation instruction received")
        # Drone triangle formation instruction
        # self.drone_swarm.triangle()
   
    # Instruction for three hand gesture
    def three_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("dance formation instruction received")
        # Drone dance formation instruction

    # Confirmation Gesture
    def okay_instruction(self):
        self.confirmation_gesture = True

    # Instruction for fist hand gesture
    def fist_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("vertical formation instruction received")
        # Drone vertical formation instruction

    # Instruction for thumbs up hand gesture
    def thumbs_up_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("ice cream formation instruction received")
        # Drone ice cream formation instruction

    # Instruction for thumbs down hand gesture
    def thumbs_down_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("diamond formation instruction received")
        # Drone diamond formation instruction

    # Instruction for stop hand gesture
    def stop_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("landing instruction received")
        # Drone land instruction
        # self.drone_swarm.land_drones()

    # Instruction for rock hand gesture
    def rock_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("ice cream instruction received")
        # Drone ice cream instruction
        # self.drone_swarm.initialize_drones()

    # Instruction for finger gun hand gesture
    def finger_gun_instruction(self):
        self.update_gui(self.instruction_gesture, drone_instruction=None, do_reset=True)
        self.send_notification(display='success', title='Success!', message='Executing {}.'.format(self.gesture_to_instruction[self.instruction_gesture]))
        print("dance instruction received")
        # Drone dance instruction
        # self.drone_swarm.dance()

##### GUI SIGNAL EMITTERS #####

    # Update GUI to show the capture gesture and corresponding instruction by emitting a signal to main.py
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

    # Sending notification to GUI by emitting a signal to main.py
    def send_notification(self, display='standard', title='', message=''):
        self.notification_signal = {
                'display': display,
                'title': title,
                'message': message
        }
        self.emitter.SendNotification.emit(self.notification_signal)

##### Close socket of drone (From the Drone Formation module) #####

    def close_socket(self):
        self.drone_swarm.end()
import collections
from collections import Counter
from formation.test.basic_commands import DroneSwarm

class Instruction:
    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.prediction_list = collections.deque(maxlen=25)
        self.instruction_gesture = "" # Current gesture captured
        self.confirmation_gesture = False # Check for confirmation gesture 
        self.drone_swarm = DroneSwarm() # Drone swarm instructions
        self.drone_swarm.initialize_drones() # Connect to drones and have them ready to accept instructions

        # Gesture to Instruction dictionary
        self.gesture_to_instruction = {
            'one': 'Take Off',
            'two': 'Triangle Formation',
            'three' : 'Dance Formation',
            "fist" : 'Vertical Formation',
            "thumbs up" : 'Ice Cream Formation',
            "thumbs down" : 'Diamond Formation Formation',
            "stop": 'Landing',
            "rock" : 'Ice Cream Instruction',
            "finger gun": 'Dance Instruction',
        }

    def gesture_present(self):
        return self.instruction_gesture != ""
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] #the element with the most frequency

    def identify_gesture(self):
        if len(self.prediction_list) == 25:
            gesture = self.most_freq(self.prediction_list)
            self.prediction_list.clear()
            if gesture != "okay":
                self.instruction_gesture = gesture
            return gesture

    def identify_instruction(self, gesture):
        if gesture is not None and self.gesture_present():
            if gesture == "one":
                print("take off instruction")
            elif gesture == "two":
                print("triangle formation instruction")
            elif gesture == "three":
                print("dance formation instruction")
            elif gesture == "fist":
                print("vertical formation instruction")
            elif gesture == "thumbs up":
                print("ice cream formation instruction")
            elif gesture == "thumbs down":
                print("diamond formation instruction")
            elif gesture == "stop":
                print("landing instruction")
            elif gesture == "rock":
                print("ice cream instruction")
            elif gesture == "finger gun":
                print("dance instruction")
            elif gesture == "okay":
                self.okay_instruction()
                return
            else:
                print("invalid instruction")
                return
            print("okay to confirm")

            self.confirmation_gesture = False

    def set_instruction_gesture(self, gesture):
        self.instruction_gesture = gesture

    def append_prediction(self, element):
        self.prediction_list.append(element)

    def carry_instruction(self):
        # Reset confirmation gesture
        self.confirmation_gesture = False
        print("executing carry instruction")
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
        print("take off instruction received")
        # Drone take off instruction
        self.drone_swarm.takeoff_drones()

    def two_instruction(self):
        print("triangle formation instruction received")
        # Drone triangle formation instruction
   
    def three_instruction(self):
        print("dance formation instruction received")
        # Drone dance formation instruction

    def okay_instruction(self):
        self.confirmation_gesture = True

    def fist_instruction(self):
        print("vertical formation instruction received")
        # Drone vertical formation instruction

    def thumbs_up_instruction(self):
        print("ice cream formation instruction received")
        # Drone ice cream formation instruction

    def thumbs_down_instruction(self):
        print("diamond formation instruction received")
        # Drone diamond formation instruction


    def stop_instruction(self):
        print("landing instruction received")
        # Drone land instruction
        self.drone_swarm.land_drones()
        

    def rock_instruction(self):
        print("ice cream instruction received")
        # Drone ice cream instruction


    def finger_gun_instruction(self):
        print("dance instruction received")
        # Drone dance instruction

    
    def close_socket(self):
        self.drone_swarm.end()
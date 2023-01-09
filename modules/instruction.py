import collections
from collections import Counter
from TelloMaster.tello import *

class Instruction:
    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=25)
        self.instructionGesture = ""
        self.confirmationGesture = False

    def gesture_present(self):
        return self.instructionGesture != ""
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] #the element with the most frequency

    def identify_gesture(self):
        if len(self.predictionLst) == 25:
            gesture = self.most_freq(self.predictionLst)
            self.predictionLst.clear()
            if gesture != "okay":
                self.instructionGesture = gesture
            return gesture

    def identify_instruction(self, gesture):
        if gesture is not None and self.gesture_present():
            if gesture == "one":
                print("take off instruction")
            elif gesture == "two":
                print("fan formation instruction")
            elif gesture == "three":
                print("dance formation instruction")
            elif gesture == "fist":
                print("vertical formation instruction")
            elif gesture == "thumbs up":
                print("ice cream formation instruction")
            elif gesture == "thumbs down":
                print("diamond formation instruction")
            elif gesture == "stop":
                print("land instruction")
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

            self.confirmationGesture = False


    def set_instruction_gesture(self, gesture):
        self.instructionGesture = gesture


    def append_prediction(self, element):
        self.predictionLst.append(element)


    def carry_instruction(self):
        #reset confirmation gesture
        self.confirmationGesture = False
        if self.gesture_present():
            # Carry out instruction based on hand gesture
            if self.instructionGesture == "one":
                self.one_instruction()   
            elif self.instructionGesture == "two":
                self.two_instruction()
            elif self.instructionGesture == "three":
                self.three_instruction()
            elif self.instructionGesture == "fist":
                self.fist_instruction() 
            elif self.instructionGesture == "thumbs up":
                self.thumbs_up_instruction()
            elif self.instructionGesture == "thumbs down":
                self.thumbs_down_instruction()
            elif self.instructionGesture == "stop":
                self.stop_instruction()
            elif self.instructionGesture == "rock":
                self.rock_instruction()
            elif self.instructionGesture == "finger gun":
                self.finger_gun_instruction()
            else:
                print("invalid gesture")
            self.instructionGesture = ""
            
        else:
            print("no instruction given")


    def check_confirmation(self):
        return self.confirmationGesture        

    def one_instruction(self):
        print("take off instruction received")
        #drone instruction


    def two_instruction(self):
        print("fan formation instruction received")
        #drone instruction
   

    def three_instruction(self):
        print("dance formation instruction received")
        #drone instruction


    def okay_instruction(self):
        self.confirmationGesture = True


    def fist_instruction(self):
        print("vertical formation instruction received")
        #drone instruction


    def thumbs_up_instruction(self):
        print("ice cream formation instruction received")
        #drone instruction


    def thumbs_down_instruction(self):
        print("diamond formation instruction received")
        #drone instruction


    def stop_instruction(self):
        print("land instruction received")
        #drone instruction


    def rock_instruction(self):
        print("ice cream instruction received")
        #drone instruction


    def finger_gun_instruction(self):
        print("dance instruction received")
        #drone instruction
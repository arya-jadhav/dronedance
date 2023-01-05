import collections
from collections import Counter
from TelloMaster.tello import *

class Instruction:
    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=25)
        self.instructionGesture = ""
        #self.confirmationGesture = False

    def gesture_present(self):
        return (self.instructionGesture != "")
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] #the element with the most frequency

    def identify_gesture(self):
        if len(self.predictionLst) == 25:
            gesture = self.most_freq(self.predictionLst)
            self.predictionLst.clear()
            return gesture
        else:
            return ""

    def identify_instruction(self, gesture):
        if gesture == "one":
            print("landing instruction")
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
        print("okay to confirm")


    def set_instruction_gesture(self, gesture):
        self.instructionGesture = gesture


    def append_prediction(self, element):
        self.predictionLst.append(element)


    def carry_instruction(self):
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
            #print("okay instruction received")
            

    def one_instruction(self):
        print("one instruction received")
        #drone instruction
        # land()


    def two_instruction(self):
        print("two instruction received")
        #drone instruction
        # start()
        # takeoff()
        

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
        #drone instruction


    def thumbs_down_instruction(self):
        print("thumbs down instruction received")
        #drone instruction


    def stop_instruction(self):
        print("stop instruction received")
        #drone instruction


    def rock_instruction(self):
        print("rock instruction received")
        #drone instruction


    def finger_gun_instruction(self):
        print("finger gun instruction received")
        #drone instruction
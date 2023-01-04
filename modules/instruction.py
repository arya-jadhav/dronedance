import collections
from collections import Counter
from TelloMaster import *

class Instruction:
    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=10)
        self.currentGesture = ""

    def current_gesture(self):
        return (self.currentGesture != "")
    
    # Approach 3 from: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    def most_freq(self, lst):
        occur_count = Counter(lst)
        return occur_count.most_common(1)[0][0] #the element with the most frequency

    def identify_instruction(self):
        if len(self.predictionLst) > 7:
            self.currentGesture = self.most_freq(self.predictionLst)
            self.predictionLst.clear()
            return True


    def append_prediction(self, element):
        self.predictionLst.append(element)


    def carry_instruction(self):
        if self.current_gesture():
            # Carry out instruction based on hand gesture     
            if self.currentGesture == "two":
                self.two_instruction()
                
            elif self.currentGesture == "thumbs up":
                self.thumbs_up_instruction()
                
            elif self.currentGesture == "stop":
                self.stop_instruction()

            else:
                print("invalid gesture")
            
            self.currentGesture = ""


    def one_instruction(self):
        print("one instruction received")
        #drone instruction


    def two_instruction(self):
        print("two instruction received")
        #drone instruction
        # start()
        # takeoff()
        # land()


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
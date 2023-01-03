import collections
from collections import Counter

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
            if self.currentGesture == "peace":
                self.peace_instruction()
                
            elif self.currentGesture == "thumbs up":
                self.thumbs_up_instruction()
                
            elif self.currentGesture == "live long":
                self.live_long_instruction()
            else:
                print("invalid gesture")
            
            self.currentGesture = ""

    def peace_instruction(self):
        print("peace instruction received")
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

    def live_long_instruction(self):
        print("live long instruction received")
        #drone instruction

    def call_me_instruction(self):
        print("call me instruction received")
        #drone instruction

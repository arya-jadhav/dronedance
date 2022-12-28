import collections
from collections import Counter

class Instruction:
    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=10)
        self.comboGesture = collections.deque(maxlen=2)
        self.currentGesture = ""

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
        # Carry out instruction based on hand gesture     
        if self.currentGesture == "peace":
            print("peace instruction received")
            
        if self.currentGesture == "thumbs up":
            print("thumbs up instruction received")
            
        if self.currentGesture == "live long":
            print("reset instruction received")
            self.comboGesture.clear()
import collections
from collections import Counter

class Instruction:
    combo1 = collections.deque(["thumbs down", "okay"], maxlen=2)
    combo2 = collections.deque(["fist", "stop"], maxlen=2)

    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=10)
        self.comboGesture = collections.deque(maxlen=2)
        self.currentGesture = ""

    def current_gesture(self):
        return self.currentGesture != ""
    
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
            if not self.combo():
                # Carry out instruction based on hand gesture     
                if self.currentGesture == "peace":
                    print("peace instruction received")
                    
                elif self.currentGesture == "thumbs up":
                    print("thumbs up instruction received")
                    
                elif self.currentGesture == "live long":
                    print("reset instruction received")
                    self.comboGesture.clear()
                else:
                    if self.currentGesture not in self.comboGesture:
                        self.comboGesture.append(self.currentGesture)
            else:
                if self.currentGesture == "peace" or self.currentGesture == "thumbs up":
                    pass
                elif self.currentGesture == "live long":
                    print("reset instruction received")
                    self.comboGesture.clear()
                else:
                    if self.currentGesture not in self.comboGesture:
                        self.comboGesture.append(self.currentGesture)
            
            self.currentGesture = ""


    def check_combo(self):
        if len(self.comboGesture) == 2:
            print(self.comboGesture)
            if self.comboGesture == self.combo1:
                print("thumbs down and okay combo received")
                
            elif self.comboGesture == self.combo2:
                print("fist and stop gesture received")
                
            else:
                print("invalid combo")
            
            self.comboGesture.clear()

    def combo(self):
        return len(self.comboGesture) > 0


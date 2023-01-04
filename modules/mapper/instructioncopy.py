import collections
from collections import Counter
from PyQt5.QtCore import *

class Instruction(QObject):
    combo1 = collections.deque(["thumbs down", "okay"], maxlen=2)
    combo2 = collections.deque(["fist", "stop"], maxlen=2)

    # Emitter signals for GUI
    class Emitter(QObject):
        GestureCapturedAndInstructionToBeExecutedLabelUpdate = pyqtSignal(dict)
        def __init__(self):
            super(Instruction.Emitter, self).__init__()

    def __init__(self):
        # Initialize a double-ended queue to save in predictions
        self.predictionLst = collections.deque(maxlen=10)
        self.comboGesture = collections.deque(maxlen=2)
        self.currentGesture = ""

        # Initialize Emitter and dictionary
        self.emitter = Instruction.Emitter()
        self.gestureSignal = {
            "gesture1": None,
            "gesture2": None,
            "do_reset": False,
        }

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
                    self.updateGUI(self.currentGesture, do_reset=False)     
                elif self.currentGesture == "thumbs down":
                    print("thumbs down instruction received")
                    self.updateGUI(self.currentGesture, do_reset=False)
                elif self.currentGesture == "okay":
                    print("okay instruction received")
                    self.updateGUI(self.currentGesture, do_reset=False)           
                elif self.currentGesture == "live long":
                    print("reset instruction received")
                    self.updateGUI(self.currentGesture, do_reset=True)
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
            # Clear current gesture         
            self.currentGesture = ""
            
    def combo(self):
        return len(self.comboGesture) > 0

    def check_combo(self):
        if len(self.comboGesture) == 2:
            print(self.comboGesture)
            if self.comboGesture == self.combo1:
                print("thumbs down and okay combo received")        
            elif self.comboGesture == self.combo2:
                print("fist and stop gesture received")
            else:
                print("invalid combo")
            
            # Reset the gestures
            self.updateGUI(self.currentGesture, do_reset=True)
    
    def updateGUI(self, gesture_name, do_reset):
        if do_reset:
            self.gestureSignal['do_reset'] = do_reset
            self.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.emit(self.gestureSignal)
            self.comboGesture.clear()

            # Update dict to intial values
            self.gestureSignal = {
            "gesture1": None,
            "gesture2": None,
            "do_reset": False,
        }
        else:
            if self.gestureSignal['gesture1'] is None:
                self.gestureSignal['gesture1'] = gesture_name
            else:
                self.gestureSignal['gesture2'] = gesture_name
            self.emitter.GestureCapturedAndInstructionToBeExecutedLabelUpdate.emit(self.gestureSignal)


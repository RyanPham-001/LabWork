import sys
import os
from pathlib import *

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
from RunningFiles.Solution import Solution

class OutputSolution(Solution):
    def __init__ (self,conc = 0, formula = "", final_volume = 0):
        super().__init__(conc,formula)
        self.___final_volume = final_volume

    def getVolume (self):
        return self.___final_volume

    def setVolume (self, volume):
        self.___final_volume = volume

    def __str__ (self):
        temp = ("%s %s uL" % (super().__str__(), str(self.___final_volume)))
        # temp = (super().__str__()) + " " + str(self.___final_volume)
        return temp

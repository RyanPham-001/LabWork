import sys
import os
from pathlib import *

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))

from RunningFiles.NoneError import NoneError
from RunningFiles.Solution import Solution
from RunningFiles.StockSolutionList import StockSolutionList
from RunningFiles.OutputSolution import OutputSolution

class CreatingSolutions:

    def __init__(self):
        self.___target_conc = 0
        self.___target_compound = ""
        self.___message = ""
        self.___SolutionList = StockSolutionList()
        self.___SolutionList.collectSolution("StockSolution.txt")
        self.___OutputSolutions = StockSolutionList()

        #how to keep the composition togeter? use dictionary or tuple?

    def getFinalVolume (self):
        return self.___final_volume

    def set_final_volume (self, final_volume):
        self.___final_volume = final_volume

    def setTargetConc(self,target):
        self.___target_conc = target

    def setTargetCompound(self,target):
        self.___target_compound = target

    def getTargetConc(self):
        return self.___target_conc

    def getTargetCompound(self):
        return self.___target_compound

    def makeSolution(self, file_name):
        with open(file_name,"r") as file:
            for line in file:
                final_volume = 0
                try:
                    num,form = line.split()[:2]
                    num = int(num)
                    self.C1V1equalsC2V2(num,form,final_volume)

                except(ValueError):
                    try:
                        final_volume = int(line)

                    except(ValueError):
                        #Finds the delimter "\n"
                        continue

    def C1V1equalsC2V2(self,conc,formula,volume):
        indexOf = self.___SolutionList.indexOf(formula)

        if (indexOf == -1):
            self.___message += "Stock Solution was not found in the list"
            return
        #Target
        C1 = conc
        V1 = volume
        #Stock
        C2 = self.___SolutionList.concentrationAtIndex(indexOf)
        V2 = C1 * V1 / C2

        tempSolution = OutputSolution(conc,formula,V2)
        self.___OutputSolutions.add(tempSolution)
        return V2
        #rename stocksolutionlist with solutionlist


def test():
    test = Solution(400,"NaCl")
    print(test.get_concentration())
    print(test)

    test.set_compound_formula("KCl")
    test.set_concentration(300)
    print(test)

    test1 = CreatingSolutions()
    test1.makeSolution("CreateSolutions.txt")

    tess = OutputSolution(400,"BeCl2",30)
    print(tess)





if (__name__ == '__main__'):
    test()

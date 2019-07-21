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
        self.___final_volume = 0
        self.___check_first = False
        self.___check_last = False
        self.___StockSolutionList = StockSolutionList()
        self.___StockSolutionList.collectSolution("StockSolution.txt")
        self.___Solutions = []

        #how to keep the composition togeter? use dictionary or tuple?

    def getFinalVolume (self):
        return self.___final_volume

    def getStockSolutionList(self):
        return self.___StockSolutionList

    def makeSolution(self, file_name):
        with open(file_name,"r") as file:
            #if (error for have not able to split in two)
                #final_volume = line
            temp_solution = OutputSolution()
            for line in file:
                try:
                    num,form = line.split()[:2]
                    temp_solution.C1V1equalsC2V2(self.getStockSolutionList(),num,form)
                except(ValueError):
                    # if (type(line) is int):
                    try:
                        temp_solution = OutputSolution(int(line))
                    except(ValueError):
                        #Finds the delimter "\n"
                        continue
                    # temp_solution.set_final_volume(line)
#try int(line)
#except (whatever it is)
#make new OutputSOlution



def test():
    test = Solution(400,"NaCl")
    print(test.get_concentration())
    print(test)

    test.set_compound_formula("KCl")
    test.set_concentration(300)
    print(test)

    test1 = CreatingSolutions()
    test1.makeSolution("CreateSolutions.txt")
    print(test1.getStockSolutionList())

if (__name__ == '__main__'):
    test()

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

    def C1V1equalsC2V2(self,conc,formula,volume):
        indexOf = self.___SolutionList.indexOf(formula)

        if (indexOf == -1):
            print("Stock Solution was not found in the list")
            # self.___message +=
            return -1
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

    def makeSolution(self, file_name):
        countVolume = 0
        workingTest = True

        with open("OutputSolutions.txt","w") as output:
            output.write("Follow the determined values\n")

            with open(file_name,"r") as file:
                final_volume = 0
                workingTest = False
                for line in file:
                    try:
                        num,form = line.split()[:2]
                        num = int(num)
                        check = self.C1V1equalsC2V2(num,form,final_volume)
                        print(workingTest)
                        if (check == -1):
                            output.write("Stock Solution for %s not found, unable to calculate\n" % form)
                            workingTest = True

                        else:
                            output.write("Use %s mL of %s to make %s mM of %s\n" % (check,form,num,form))
                            countVolume += check

                    except(ValueError):
                        try:
                            final_volume = int(line)
                            # print(workingTest)
                            # if (workingTest):
                            #     output.write("Fill remaining volume with %s mL of solvent\n\n" % (final_volume - countVolume))
                            workingTest = True
                            countVolume = 0

                            output.write("Final Volume is %s mL\n" % (final_volume))

                        except(ValueError):
                            #Finds the delimter "\n"
                            if (workingTest):
                                output.write("Fill remaining volume with %s mL of solvent\n\n" % (final_volume - countVolume))
                            continue

def test():
    # test = Solution(400,"NaCl")
    # print(test.get_concentration())
    # print(test)
    #
    # test.set_compound_formula("KCl")
    # test.set_concentration(300)
    # print(test)
    #
    test1 = CreatingSolutions()
    test1.makeSolution("CreateSolutions.txt")
    #
    # tess = OutputSolution(400,"BeCl2",30)
    # test1.makeSolution("CreateSolutions.txt")
    # print(tess)





if (__name__ == '__main__'):
    test()

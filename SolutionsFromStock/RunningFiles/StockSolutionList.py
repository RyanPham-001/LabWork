import sys
import os
from pathlib import *

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
# sys.path.append(os.path.dirname(Path(__file__).resolve().parent.parent))

from RunningFiles.NoneError import NoneError
from RunningFiles.Solution import Solution

class StockSolutionList:
    def __init__ (self):
        self.___location = 0
        self.___size = 0
        self.___List= []
        self.___found = False

    def add (self, Solution):
        self.___List.append(Solution)
        self.___size += 1

    def remove (self, Solution):
        if (self.isEmpty()):
            raise NoneError()

        if (self.contains(Solution)):
            for i in range(0,self.getSize()):
                if (Solution == self.___List[i].get_compound_formula()):
                    del(self.___List[i])
                    self.___size -= 1
                    return True
        return False

    def indexOf(self,Solution):
        if (self.isEmpty()):
            raise NoneError()

        for i in range(0,self.getSize()):
            if (Solution == self.___List[i].get_compound_formula()):
                return i
            return -1

    def contains(self, element):
        if (self.isEmpty()):
            raise NoneError()

        for i in range(0,self.getSize()):
            if (element == self.___List[i].get_compound_formula()):
                return True
        return False


        #initialize found to false
        #binary search
        #if found
            #remove from list
            #update size
            #resort list
        #else
            #print that it is not found in list

    def getSize(self):
        return self.___size

    def isEmpty(self):
        return (self.getSize() == 0)

    def __str__ (self):
        temp = ""
        temp = "List of Solutions\n\n"

        for i in range(0,len(self.___List) ):
            temp += str(self.___List[i])
            temp += "\n"

        return temp


    def collectSolution(self,file_name):
        with open(file_name,"r") as file:
            for line in file:
                try:
                    num,form = line.split()[:2]
                    num = int(num)
                    solution = Solution(num,form)
                    self.add(solution)
                except(ValueError):
                    print("Check that the .txt file is formatted correctly")
                # try:
                #     if (type(int(num)) == int):
                #         solution = Solution(num,form)
                #         self.add(solution)
                # except ValueError:
                #     continue

    def updateList(self,file_name):
        with open(file_name, "w") as file:
            for line in range(0,self.getSize()):
                file.write("%s %s\n" % (self.___List[line].get_concentration(), self.___List[line].get_compound_formula()))

        #rewrites the .txt file to update what has been added/removed

def main ():
    print("A free trial as you will")
    test = StockSolutionList()

    test.collectSolution("StockSolution.txt")
    print(test)

    sol = Solution(400, "NaCl")
    test.add(sol)
    print(test)
    print(test.contains("NaCl"))
    print("Changing NaCl to KCl")
    sol.set_compound_formula("KCl")
    print(test)

    print(test.contains("KCl"))

    test.updateList("StockSolutionNew.txt")


if (__name__ == "__main__"):
    main()

from Solution import Solution
from SolutionList import SolutionList

class CreatingSolutions:

    def __init__(self,final_volume):
        self.___final_volume = 0
        self.___check_first = False
        self.___check_last = False
        self.___StockSolutionList = SolutionList()
        #how to keep the composition togeter? use dictionary or tuple?

    def getFinalVolume (self):
        return self.___final_volume

    def makeSolution(self,file_name):
        pass

    def C1V1equalsC2V2(self, final_volume):
        pass

#rrrr

def main():
    test = Solution(400,"NaCl")
    print(test.get_concentration())
    print(test)

    test.set_compound_formula("KCl")
    test.set_concentration(300)
    print(test)

if (__name__ == '__main__'):
    main()

from Solution import Solution

class SolutionList:

    def __init__ (self):
        self.___location = 0
        self.___size = 0
        self.___List= []
        self.___found = False

    def add (self, Solution):
        self.___List.append(Solution)
        self.___size += 1

    def remove (self, Solution):
        pass

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

    #Returns the
    def __str__ (self):
        temp = ""
        temp = "List of Solutions\n\n"

        for i in range(0,len(self.___List) ):
            temp += str(self.___List[i])
            temp += "\n"

        return temp

    def readTxT(self,file_name,num_start):
        with open("StockSolution.txt","r") as file:
            while(num_start >= 0):
                temp = file.readline()
                num_start -= 1

            for line in file:
                num,form = line.split()[:2]

                try:
                    if (type(int(num)) == int):
                        solution = Solution(num,form)
                        self.add(solution)
                except ValueError:
                    continue




    def updateList(self):
        pass
        #rewrites the .txt file to update what has been added/removed

def main ():
    print("A free trial as you will")
    test = SolutionList()
    sol = Solution(400, "NaCl")
    test.add(sol)
    print(test)

    print("Changing NaCl to KCl")
    sol.set_compound_formula("KCl")
    print(test)

    test.readTxT("StockSolution.txt",2)
    print(test)

if (__name__ == "__main__"):
    main()

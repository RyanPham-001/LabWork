class OutputSolution:
    def __init__ (self,final_volume = 0):
        self.___final_volume = final_volume
        self.___final_result = ()
        self.___target_conc = 0
        self.___target_compound = ""
        self.___message = ""

    def set_final_volume (self, final_volume):
        self.___final_volume = final_volume

    def get_final_volume(self):
        return self.___final_volume

    def setTargetConc(self,target):
        self.___target_conc = target

    def setTargetCompound(self,target):
        self.___target_compound = target

    def getTargetConc(self):
        return self.___target_conc

    def getTargetCompound(self):
        return self.___target_compound

    def C1V1equalsC2V2(self,StockList,conc,formula):
        if (StockList.indexOf() == -1):
            self.message += "Stock Solution was not found in the list"

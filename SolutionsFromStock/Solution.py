class Solution:

    def __init__(self, concentration = 0, compound_formula = ""):
        self.__concentration = concentration
        self.__compound_formula = compound_formula

    #Returns the concentration of the solution
    def get_concentration (self):
        
        return(self.__concentration)

    #Returns the chemicalforumla of the solution
    def get_compound_formula(self):
        return(self.__compound_formula)

    #Changes the concentration of the solution to new_conc
    def set_concentration (self, new_conc):
        self.__concentration = new_conc

    #Changes the chemicalformula of the solution to new_formula
    def set_compound_formula(self, new_formula):
        self.__compound_formula = new_formula

    def __str__ (self):
        return("%s mM %s" % (self.get_concentration(), self.get_compound_formula()))

    if (__name__ == "__main__"):
        print("This is the class file for the object 'Solution object'")

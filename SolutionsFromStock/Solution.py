class Solution:

    def __init__(self, concentration = 0, compound_formula = ""):
        self.concentration = concentration
        self.compound_formula = compound_formula

    def get_concentration (self):
        return(self.concentration)

    def get_compound_formula(self):
        return(self.compound_formula)

    def set_concentration (self, new_conc):
        self.concentration = new_conc


    def __str__ (self):
        return("Solution: %s mM %s" % (self.get_concentration(), self.get_compound_formula()))

    if (__name__ == "__main__"):
        print("This is the class file for the object 'Solution object'")

import unittest
import sys
import os
from pathlib import *

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
from RunningFiles.Solution import Solution
from RunningFiles.OutputSolution import OutputSolution

class TestOutputSolution(unittest.TestCase):
    def setUp (self):
        self.test = OutputSolution()
        self.test2 = OutputSolution(400, "MgCl2",50)

    def test_blankOutputSolution(self):
        self.assertEqual(self.test.get_concentration(),0,"Conc should be 0")
        self.assertEqual(self.test.get_compound_formula(),"","Formula should be \"\"")
        self.assertEqual(self.test.getVolume(), 0, "Final V should be 0")

    def test_changeBlankOutputSolutionConc(self):
        self.assertEqual(self.test.get_concentration(),0,"Should be 0")
        self.test.set_concentration(5)
        self.assertEqual(self.test.get_concentration(),5,"Should be 5")

    def test_changeBlankOutputSolutionFormula(self):
        self.assertEqual(self.test.get_compound_formula(),"","Should be \"\"")
        self.test.set_compound_formula("CH3COOH")
        self.assertEqual(self.test.get_compound_formula(),"CH3COOH","Should be CH3COOH")

    def test_changeBlankOutputSolutionFinalV(self):
        self.assertEqual(self.test.getVolume(),0,"Should be 0")
        self.test.setVolume(5)
        self.assertEqual(self.test.getVolume(),5,"Should be 5")

    def test_changeOutputSolutionConc(self):
        self.assertEqual(self.test2.get_concentration(),400,"Should be 400")
        self.test2.set_concentration(5)
        self.assertEqual(self.test2.get_concentration(),5,"Should be 5")

    def test_changeOutputSolutionCompoundget_compound_formula(self):
        self.assertEqual(self.test2.get_compound_formula(),"MgCl2","Should be MgCl2")
        self.test2.set_compound_formula("PO4")
        self.assertEqual(self.test2.get_compound_formula(),"PO4","Should be PO4")

    def test_changeOutputSolutionFinalV(self):
        self.assertEqual(self.test2.getVolume(),50,"Should be 50")
        self.test2.setVolume(5)
        self.assertEqual(self.test2.getVolume(),5,"Should be 5")

    def test_changeOutputSolutionConcandFormula(self):
        self.assertEqual(self.test2.get_concentration(),400,"Should be 400")
        self.assertEqual(self.test2.getVolume(),50,"Should be 50")
        self.assertEqual(self.test2.get_compound_formula(),"MgCl2","Should be MgCl2")
        self.test2.set_concentration(500)
        self.test2.set_compound_formula("KCl")
        self.test2.setVolume(25)
        self.assertEqual(self.test2.get_concentration(),500,"Should be 500")
        self.assertEqual(self.test2.get_compound_formula(),"KCl","Should be KCl")
        self.assertEqual(self.test2.getVolume(),25,"Should be 25")
if __name__ == "__main__":
    unittest.main()

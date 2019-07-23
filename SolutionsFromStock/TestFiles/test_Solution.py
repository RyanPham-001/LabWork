import unittest
import sys
import os
from pathlib import *
#Just want to import Path, but on MacOS does not work

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))

from RunningFiles.Solution import Solution

class TestSolution(unittest.TestCase):
    def setUp (self):
        self.test = Solution()
        self.test2 = Solution(400, "MgCl2")

    def test_blankSolution(self):
        self.assertEqual(self.test.get_concentration(),0,"Should be 0")
        self.assertEqual(self.test.get_compound_formula(),"","Should be \"\"")

    def test_changeBlankSolutionConc(self):
        self.assertEqual(self.test.get_concentration(),0,"Should be 0")
        self.test.set_concentration(5)
        self.assertEqual(self.test.get_concentration(),5,"Should be 5")

    def test_changeBlankSolutionFormula(self):
        self.assertEqual(self.test.get_compound_formula(),"","Should be \"\"")
        self.test.set_compound_formula("CH3COOH")
        self.assertEqual(self.test.get_compound_formula(),"CH3COOH","Should be CH3COOH")

    def test_changeSolutionConc(self):
        self.assertEqual(self.test2.get_concentration(),400,"Should be 400")
        self.test2.set_concentration(5)
        self.assertEqual(self.test2.get_concentration(),5,"Should be 5")

    def test_changeSolutionCompoundget_compound_formula(self):
        self.assertEqual(self.test2.get_compound_formula(),"MgCl2","Should be MgCl2")
        self.test2.set_compound_formula("PO4")
        self.assertEqual(self.test2.get_compound_formula(),"PO4","Should be PO4")

    def test_changeSolutionConcandFormula(self):
        self.assertEqual(self.test2.get_concentration(),400,"Should be 400")
        self.assertEqual(self.test2.get_compound_formula(),"MgCl2","Should be MgCl2")
        self.test2.set_concentration(500)
        self.test2.set_compound_formula("KCl")
        self.assertEqual(self.test2.get_concentration(),500,"Should be 500")
        self.assertEqual(self.test2.get_compound_formula(),"KCl","Should be KCl")


if __name__ == "__main__":
    unittest.main()

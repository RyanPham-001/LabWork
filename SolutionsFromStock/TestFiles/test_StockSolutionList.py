import unittest
import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
print(sys.path)

from RunningFiles.NoneError import NoneError
from RunningFiles.Solution import Solution
from RunningFiles.StockSolutionList import StockSolutionList
from RunningFiles.CreatingSolutions import CreatingSolutions

class TestStockSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def setUp(self):
        self.testList = StockSolutionList()

    def tearDown(self):
        pass

    def test_add_single_solution(self):
        sol = Solution(450, "NaCl")

        self.assertTrue(self.testList.isEmpty(),"List should be empty initially")

        self.testList.add(sol)
        self.assertFalse(self.testList.isEmpty(),"List was expected to not be empty")
        self.assertEqual(self.testList.getSize(),1,"List expected to have a size of 1")

    def test_empty_contains(self):
        with self.assertRaises(NoneError):
            self.testList.contains("KCl")

if (__name__ == "__main__"):
    unittest.main()

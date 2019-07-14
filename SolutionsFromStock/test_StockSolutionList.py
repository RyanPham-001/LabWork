import unittest
from StockSolutionList import StockSolutionList
from CreatingSolutions import CreatingSolutions
from Solution import Solution
from NoneError import NoneError

#Find out a way to import multiple files without all of these lines

class TestStockSolution(unittest.TestCase):
    def setUp(self):
        self.testList = StockSolutionList()

    def tearDown(self):
        pass

    def test_add_single_solution(self):
        pass

    def test_empty_contains(self):
        with self.assertRaises(NoneError):
            self.testList.contains("KCl")

if (__name__ == "__main__"):
    unittest.main()

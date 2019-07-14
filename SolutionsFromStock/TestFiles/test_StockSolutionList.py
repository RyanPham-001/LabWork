import unittest
from SolutionsFromStock.StockSolutionList import StockSolutionList
from CreatingSolutions import CreatingSolutions
from Solution import Solution
from NoneError import NoneError

#Find out a way to import multiple files without all of these lines

class TestStockSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

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

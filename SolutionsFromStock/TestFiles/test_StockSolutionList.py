import unittest
import sys
import os


from pathlib import Path
# print(Path(__file__).resolve())

# print (y)
#
# print(sys.path)
# x = Path(__file__).resolve().parent.parent
# print(x)
# sys.path.insert(0,x)
#
# os.chdir(x)
# print(sys.path)
# os.chdir(y)
sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
print(sys.path)
from RunningFiles.CreatingSolutions import CreatingSolutions
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path)
#
# os.getcwd()
from RunningFiles.Solution import Solution
from RunningFiles.StockSolutionList import StockSolutionList
from RunningFiles.NoneError import NoneError
# from StockSolutionList import StockSolutionList
# from CreatingSolutions import CreatingSolutions
# from Solution import Solution
# from NoneError import NoneError
#
#Find out a way to import multiple files without all of these lines

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

import unittest
import sys
import os
from pathlib import *
#Just want to import Path, but on MacOS does not work

sys.path.append(os.path.dirname(Path(__file__).resolve().parent))

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

    def test_is_empty(self):
        self.assertTrue(self.testList.isEmpty())

    def test_add_single_solution(self):
        sol = Solution(450, "NaCl")
        self.assertTrue(self.testList.isEmpty(),"List should be empty initially")

        self.testList.add(sol)
        self.assertFalse(self.testList.isEmpty(),"List was expected to not be empty")
        self.assertEqual(self.testList.getSize(),1,"List expected to have a size of 1")

    def test_add_file(self):
        self.assertTrue(self.testList.isEmpty(),"List should be empty")
        self.testList.collectSolution("test_StockSolution.txt")
        self.assertEqual(self.testList.getSize(),3,"List is expected to have 3 items")

    def test_remove_empty_list(self):
        with self.assertRaises(NoneError):
            self.testList.remove("NaCl")

    def test_remove_last_solution(self):
        sol = Solution(450,"NaCl")
        self.testList.add(sol)
        self.assertTrue(self.testList.contains("NaCl"), "List should have NaCl in it")
        self.assertTrue(self.testList.remove("NaCl"),"Should have been able to remove the NaCl")
        with self.assertRaises(NoneError):
            self.testList.contains("NaCl")

    def test_remove(self):
        self.testList.collectSolution("test_StockSolution.txt")
        self.assertEqual(self.testList.getSize(),3,"Size should now be 3")
        self.assertTrue(self.testList.remove("NaCl"),"Should have been able to remove the NaCl")
        self.assertFalse(self.testList.contains("NaCl"),"Should not have NaCl in the list")
        self.assertEqual(self.testList.getSize(),2,"Size should now be 2")

    def test_empty_contains(self):
        with self.assertRaises(NoneError):
            self.testList.contains("KCl")

    def test_indexOfEmpty(self):
        with self.assertRaises(NoneError):
            self.testList.indexOf("AgCl")

    def test_indexOfInList(self):
        self.testList.collectSolution("test_StockSolution.txt")
        self.assertEqual(self.testList.indexOf("NaCl"),0,"Should find NaCl in position 0")

    def test_indexOfNotInList(self):
        self.testList.collectSolution("test_StockSolution.txt")
        self.assertEqual(self.testList.indexOf("NH3"),-1,"Should not be in list")

    def test_concAtIndex(self):
        with self.assertRaises(NoneError):
            self.testList.concentrationAtIndex(2)

    def test_concAtIndex(self):
        self.testList.collectSolution("test_StockSolution.txt")
        self.assertEqual(self.testList.concentrationAtIndex(2),1000,"Should be 1000 in position 2")

    def test_concAtIndexOutOfBounds(self):
        with self.assertRaises(IndexError):
            self.testList.collectSolution("test_StockSolution.txt")
            self.testList.concentrationAtIndex(3)

if (__name__ == "__main__"):
    unittest.main()

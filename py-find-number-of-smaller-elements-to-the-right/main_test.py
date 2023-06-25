import unittest
import main

class TestFindNumbersOfSmallerElementsToTheRight(unittest.TestCase):

    def setUp(self):
        self.find = main.FindNumbersOfSmallerElementsToTheRight
        self.list1 = [3, 4, 9, 6, 1]
        self.list_return = [1, 1, 2, 1, 0]

    def test_smaller_counts_in_naive_way(self):
        result = self.find.smaller_counts_in_naive_way(self.list1)
        self.assertEqual(result, self.list_return)

    def test_smaller_counts(self):
        result = self.find.smaller_counts(self.list1)
        self.assertEqual(result, self.list_return)
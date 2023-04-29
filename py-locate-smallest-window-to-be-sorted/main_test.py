import unittest
import main

class TestLocateSmallestWindowToBeSorted(unittest.TestCase):

    def setUp(self):
        self.Locate = main.LocateSmallestWindowToBeSorted()

    def test_nlogn_ordered_array(self):
        array = [1,2,3,4,5,6]
        left_result = None
        right_result = None

        left, right = self.Locate.window_nlogn(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_n_ordered_array(self):
        array = [1,2,3,4,5,6]
        left_result = None
        right_result = None

        left, right = self.Locate.window_n(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_nlogn_empty_array(self):
        array = []
        left_result = None
        right_result = None

        left, right = self.Locate.window_nlogn(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_n_empty_array(self):
        array = []
        left_result = None
        right_result = None

        left, right = self.Locate.window_n(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_nlogn_array_1(self):
        array = [3, 7, 5, 6, 9]
        left_result = 1
        right_result = 3

        left, right = self.Locate.window_nlogn(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_n_array_1(self):
        array = [3, 7, 5, 6, 9]
        left_result = 1
        right_result = 3

        left, right = self.Locate.window_n(array)

        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_nlogn_array_2(self):
        array = [9, 7, 5, 6, 3]
        left_result = 0
        right_result = 4

        left, right = self.Locate.window_nlogn(array)
        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_n_array_2(self):
        array = [9, 7, 5, 6, 3]
        left_result = 0
        right_result = 4

        left, right = self.Locate.window_n(array)
        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_nlogn_array_3(self):
        array = [3, 4, 6, 5, 7, 9]

        left_result = 2
        right_result = 3

        left, right = self.Locate.window_nlogn(array)
        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)

    def test_n_array_3(self):
        array = [3, 4, 6, 5, 7, 9]

        left_result = 2
        right_result = 3

        left, right = self.Locate.window_nlogn(array)
        self.assertEqual(right, right_result)
        self.assertEqual(left, left_result)
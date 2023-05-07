import unittest
import main

class TestCalculateMaxSubarraySum(unittest.TestCase):
    
    def setUp(self) -> None:
        self.empty_array = []
        self.default_array = [34, -50, 42, 14, -5, 86]
        self.default_array_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.CalculateMaxSubArraySum = main.CalculateMaxSubArraySum()
        return super().setUp()
    
    def test_an_empty_array_sum_max_subarray_n3(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n3(self.empty_array)
        self.assertEqual(0, sum)

    def test_an_empty_array_sum_max_subarray_n1(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n(self.empty_array)
        self.assertEqual(0, sum)

    def test_an_empty_array_sum_max_subarray(self):
        sum = self.CalculateMaxSubArraySum.max_subarray_sum(self.empty_array)
        self.assertEqual(0, sum)

    def test_array_sum_max_subarray_n3(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n3(self.default_array)
        self.assertEqual(137, sum)

    def test_an_array_sum_max_subarray_n1(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n(self.default_array)
        self.assertEqual(137, sum)
    
    def test_an_array_sum_max_subarray(self):
        sum = self.CalculateMaxSubArraySum.max_subarray_sum(self.default_array)
        self.assertEqual(137, sum)

    def test_array_1_sum_max_subarray_n3(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n3(self.default_array_1)
        self.assertEqual(6, sum)

    def test_array_1_sum_max_subarray_n1(self):
        sum = self.CalculateMaxSubArraySum.sum_max_subarray_n(self.default_array_1)
        self.assertEqual(6, sum)

    def test_array_1_sum_max_subarray(self):
        sum = self.CalculateMaxSubArraySum.max_subarray_sum(self.default_array_1)
        self.assertEqual(6, sum)



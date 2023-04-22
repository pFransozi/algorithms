import unittest
import main

class TestsGetProductOfAllOtherElements(unittest.TestCase):
    
    def setUp(self):
        self.GetProductOfAllOtherElements = main.GetProductOfAllOtherElements()

    def test_an_empty_array(self):
        result = self.GetProductOfAllOtherElements.compute_product_array([])
        self.assertEqual([], result, "Not equal.")

    def test_an_array_with_one_element(self):
        result = self.GetProductOfAllOtherElements.compute_product_array([7])
        self.assertEqual([7], result, "Not equal.")

    def test_an_array_with_two_elements(self):
        result = self.GetProductOfAllOtherElements.compute_product_array([7, 5])
        self.assertEqual([5, 7], result, "Not equal.")

    def test_an_defined_array_a(self):
        result = self.GetProductOfAllOtherElements.compute_product_array([3, 2, 1])
        self.assertEqual([2, 3, 6], result, "Not Equal.")

    def test_an_defined_array_b(self):
        result = self.GetProductOfAllOtherElements.compute_product_array([1, 2, 3, 4, 5])
        self.assertEqual([120, 60, 40, 30, 24], result, "Not equal.")
import unittest

from .product_array_except_self import productExceptSelf as product_except_self

class TestProductExceptSelf(unittest.TestCase):
    
    def test_example_case(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    
    def test_single_element(self):
        self.assertEqual(product_except_self([1]), [1])
    
    def test_two_elements(self):
        self.assertEqual(product_except_self([1, 2]), [2, 1])
    
    def test_contains_zero(self):
        self.assertEqual(product_except_self([1, 2, 3, 0]), [0, 0, 0, 6])
    
    def test_multiple_zeros(self):
        self.assertEqual(product_except_self([1, 0, 3, 0]), [0, 0, 0, 0])
    
    def test_all_ones(self):
        self.assertEqual(product_except_self([1, 1, 1, 1]), [1, 1, 1, 1])
    
    def test_mixed_numbers(self):
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
    
    def test_negative_numbers(self):
        self.assertEqual(product_except_self([-1, -2, -3, -4]), [-24, -12, -8, -6])
    
    def test_large_numbers(self):
        self.assertEqual(product_except_self([1000, 2000, 3000, 4000]), [24000000000, 12000000000, 8000000000, 6000000000])
    
    def test_repeated_numbers(self):
        self.assertEqual(product_except_self([2, 2, 2, 2]), [8, 8, 8, 8])

if __name__ == '__main__':
    unittest.main()
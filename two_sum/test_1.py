import unittest
from .two_sum import two_sum
class TestTwoSum(unittest.TestCase):
    
    def test_example_case(self):
        self.assertEqual(sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])
    
    def test_single_pair(self):
        self.assertEqual(sorted(two_sum([1, 2, 3], 4)), [0, 2])
    
    def test_negative_numbers(self):
        self.assertEqual(sorted(two_sum([-1, -2, -3, -4, -5], -8)), [2, 4])
    
    def test_mixed_numbers(self):
        self.assertEqual(sorted(two_sum([1, -2, 3, 4, 5], 3)), [1, 4])
    
    def test_large_numbers(self):
        self.assertEqual(sorted(two_sum([1000000, 2000000, 3000000, 4000000], 7000000)), [2, 3])
    
    def test_zero(self):
        self.assertEqual(sorted(two_sum([0, 4, 3, 0], 0)), [0, 3])
    
    def test_duplicate_elements(self):
        self.assertEqual(sorted(two_sum([3, 3], 6)), [0, 1])
    
    def test_minimum_input_size(self):
        self.assertEqual(sorted(two_sum([1, 2], 3)), [0, 1])
    
    def test_unsorted_array(self):
        self.assertEqual(sorted(two_sum([4, 3, 5, 1], 6)), [2, 3])

if __name__ == '__main__':
    unittest.main()
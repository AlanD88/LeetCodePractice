import unittest
from .top_k_frequent_elements import topKFrequent as top_k_frequent

class TestTopKFrequent(unittest.TestCase):
    
    def test_example_case(self):
        self.assertCountEqual(
            top_k_frequent([1,1,1,2,2,3], 2),
            [1, 2]
        )
    
    def test_single_element(self):
        self.assertEqual(
            top_k_frequent([1], 1),
            [1]
        )
    
    def test_all_same_frequency(self):
        self.assertCountEqual(
            top_k_frequent([1,2,3,4,5,6], 3),
            [1, 2, 3]
        )
    
    def test_k_equals_length(self):
        self.assertCountEqual(
            top_k_frequent([1,2,3,4,5,6], 6),
            [1, 2, 3, 4, 5, 6]
        )
    
    def test_k_greater_than_unique_elements(self):
        self.assertCountEqual(
            top_k_frequent([1, 1, 2, 2, 3, 3, 4, 4], 5),
            [1, 2, 3, 4]
        )
    
    def test_negative_numbers(self):
        self.assertCountEqual(
            top_k_frequent([-1, -1, -2, -2, -3], 2),
            [-1, -2]
        )
    
    def test_mixed_numbers(self):
        self.assertCountEqual(
            top_k_frequent([1, -1, 2, -1, -2, -2, -2, 3], 3),
            [-2, -1, 1]
        )
    
    def test_large_list(self):
        nums = [i for i in range(1000)] * 2 + [i for i in range(500)]
        self.assertCountEqual(
            top_k_frequent(nums, 5),
            [0, 1, 2, 3, 4]
        )

if __name__ == '__main__':
    unittest.main()
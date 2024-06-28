import unittest
from .contains_duplicates import contains_duplicate

class TestContainsDuplicate(unittest.TestCase):
    
    def test_no_duplicates(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4, 5]))
    
    def test_with_duplicates(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
    
    def test_empty_list(self):
        self.assertFalse(contains_duplicate([]))
    
    def test_single_element(self):
        self.assertFalse(contains_duplicate([10]))
    
    def test_large_list_with_no_duplicates(self):
        self.assertFalse(contains_duplicate(list(range(100000))))
    
    def test_large_list_with_duplicates(self):
        self.assertTrue(contains_duplicate(list(range(100000)) + [0]))
    
    def test_all_duplicates(self):
        self.assertTrue(contains_duplicate([2, 2, 2, 2, 2]))
    
    def test_negative_numbers(self):
        self.assertTrue(contains_duplicate([-1, -2, -3, -1]))
    
    def test_mixed_numbers(self):
        self.assertTrue(contains_duplicate([0, 1, -1, 2, -2, 0]))

if __name__ == '__main__':
    unittest.main()
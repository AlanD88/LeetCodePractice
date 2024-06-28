import unittest
from .group_anagrams import groupAnagrams as group_anagrams
class TestGroupAnagrams(unittest.TestCase):
    
    def test_example_case(self):
        self.assertEqual(
            sorted([sorted(group) for group in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])]),
            sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        )
    
    def test_empty_string(self):
        self.assertEqual(
            group_anagrams([""]),
            [[""]]
        )
    
    def test_single_character_strings(self):
        self.assertEqual(
            sorted([sorted(group) for group in group_anagrams(["a", "b", "c", "a"])]),
            sorted([["a", "a"], ["b"], ["c"]])
        )
    
    def test_no_anagrams(self):
        self.assertEqual(
            sorted([sorted(group) for group in group_anagrams(["abc", "def", "ghi"])]),
            sorted([["abc"], ["def"], ["ghi"]])
        )
    
    def test_all_anagrams(self):
        self.assertEqual(
            group_anagrams(["abc", "cba", "bca", "cab", "bac"]),
            [["abc", "cba", "bca", "cab", "bac"]]
        )
    
    def test_mixed_length_strings(self):
        self.assertEqual(
            sorted([sorted(group) for group in group_anagrams(["a", "ab", "ba", "abc", "cab"])]),
            sorted([["a"], ["ab", "ba"], ["abc", "cab"]])
        )
    
    def test_empty_list(self):
        self.assertEqual(
            group_anagrams([]),
            []
        )

if __name__ == '__main__':
    unittest.main()
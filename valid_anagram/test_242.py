import unittest
from .valid_anagram import is_anagram

class TestIsAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
    
    def test_not_anagrams(self):
        self.assertFalse(is_anagram("rat", "car"))
    
    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
    
    def test_different_lengths(self):
        self.assertFalse(is_anagram("a", "ab"))
    
    def test_same_characters_different_frequencies(self):
        self.assertFalse(is_anagram("aabbcc", "aabbc"))
    
    def test_case_sensitivity(self):
        self.assertFalse(is_anagram("anagram", "Nagaram"))
    
    def test_unicode_characters(self):
        self.assertTrue(is_anagram("你好", "好你"))
    
    def test_special_characters(self):
        self.assertTrue(is_anagram("a!n@a#g$r%a^m", "m^a!g@a#r%a$n"))
    
    def test_numbers_and_letters(self):
        self.assertTrue(is_anagram("123abc", "cba321"))

if __name__ == '__main__':
    unittest.main()
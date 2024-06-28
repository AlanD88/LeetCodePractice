# 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

## Description
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

```
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
```

## Solution

```python
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
```

## Explanation

By Counting the number of elements in string, we determine if the strings contain exactly the same amount of characters within each other.

## Analyze Complexity

```
Time O(n)
    Time complexity of counting the String with a single pass.  O(n)

Space O(1)
    The table size at most will be 26 long.  One element per alphabet character, which means it will always be a constant size.

```
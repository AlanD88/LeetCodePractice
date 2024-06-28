# 49. Group Anagrams

https://leetcode.com/problems/group-anagrams/description/

## Description

```
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


```
## Solution
```python
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            hmap[tuple(count)].append(word)

        return hmap.values()
```

## Explanation
Using an list of character counts of the entire alphabet we can build a unique tuple of all counts of
all letters in the alphabet as our key.  By subtracting ord(X) with ord('a') we get a value between 0-25 which we can increment in our tuple key

```plaintext
{
    (0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ["note", "tone"],
    (1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0): ["affection", "caffeino"]
}
```

## Analyze Complexity
```
Time Complexity: O(NK)
    For each Word N and each character K in each word.

Space Complexity: O(NK)
    Hashmap N and each list of K groups.
```
# 217. Contains Duplicates
https://leetcode.com/problems/contains-duplicate/description/

## Description
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```
Example 1:

  Input: nums = [1,2,3,1]
  Output: true

Example 2:

  Input: nums = [1,2,3,4]
  Output: false

Example 3:

  Input: nums = [1,1,1,3,3,4,3,2,4,2]
  Output: true
```

## Solution

```python
def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
```

## Explanation

The problem is solved by using a simple `set` data type.  Sets are a built-in data type that is used to store unordered **unique** collections of elements.

By comparing the length of the original nums list with the length of the set of the nums list we can see if any elements were removed from the list indicating that there were duplicates in the original list and return True/False based on this indication.

## Analyze Complexity


```
Time: O(n)
  Time complexity of converting a list to a set runs O(n) time

Space: O(1)
  No additional data structures were used to store data.
```


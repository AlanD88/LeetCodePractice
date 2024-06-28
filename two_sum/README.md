# 1. Two Sum
https://leetcode.com/problems/two-sum/description/

## Description

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

```

## Solution

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    hmap = {}
    for idx, num in enumerate(nums):
        if hmap.get(target-num) is not None:
            return [hmap.get(target-num), idx]
        hmap[num] = idx
```

## Explanation
Iterate through a hashmap tracking the number with the index value.  If target minus the current index value exists in the hashmap then you have the unique solution.

## Analyze Complexity

```
Time Complexity: O(n)
    Single pass through nums list for O(n) times

Space Complexity: O(n)
    Store hash container that fills with atmost N-1 elements in the worst case where the solution is
    at the end of the list.
```
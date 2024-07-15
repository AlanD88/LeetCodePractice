# 238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/description/

## Description

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


## Solution
```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```

## Explanation

To solve this problem we can use a combination of prefix-sum and postfix sum.

We first initialize a results array to match the length of nums array and set each index to 1.

We then proceed to calculate the prefix value for each position.

Initializing the `prefix` variable to 1 as the prefix of the 0th index value is 1 by default.  we then proceed to set each prefix value in the results index array and then finding the next prefix by `prefix = prefix * nums[i]`

Example first pass

```python
nums = [1,2,3,4]
prefix = 1
for num in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
```

This gives us a results array of `[1,1,2,6]`
```
Explanation:
prefix = 1
  res[0] = prefix = 1
prefix = 1 * 1  = 1
  res[1] = prefix = 1
prefix = 1 * 2 = 2
  res[2] = prefix = 2
prefix = 2 * 3 = 6
  res[3] = prefix = 6
```

Then we calculate the postfix values by iterating in reverse over the original nums array
```python
for i in range(len(nums)-1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
```

Starting from the original results array
```
res = [1,1,2,6]
postfix = 1
  res[3] = 6 * 1 = 6
postfix = 1 * 4
  res[2] = 2 * 4 = 8
postfix = 4 * 3 = 12
  res[1] = 1 * 12 = 12
postfix = 12 * 2 = 24
  res[0] = 1 * 24 = 24

```
## Analyze Complexity

```
Time Complexity: O(n)
  We iterate over the nums array twice giving us O(2n) -> O(n)

Space Complexity: O(1)
  We create one array container to hold the results, but the problem statement states that the output
  array does not count towards space complexity so O(1)
```
# 347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

## Description
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



## Solution

```python
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)

    freq = [[] for _ in range(len(nums)+1)]
    for v,c in count.items():
        freq[c].append(v)

    res = []
    for i in range(len(freq)-1, 0, -1):
        if len(freq) == 0:
            continue
        res.extend(freq[i])
        if len(res) >= k:
            break
    return res[:k]
```
## Explanation

First gain a count of frequency of all elements in the original list.  This is done in O(n) Time

Next build a freq grouped list and populate each index based on the total count of that character.
If nums list is 

[0,1,1,1,3,3,2,4,3]

we'ed have counts of :
```
{
    0: 1,
    1: 3,
    2: 1,
    3: 3,
    4: 1
}
```
Populating the frequency list would give us a list looking:
[[],[0,2,4],[],[1,3],[],[],[],[],[]]

We then build a results list iterating over the freq list backwards.  Due to most frequent occuring later in the list and we'd obviously want to iterate over that way first.  We ignore empty lists and populate a results list based on values found.  If the length of the results list is >= k our target break and return the result list sliced up to k values res[:k]  This ensure any subarray group that might have pushed us over k isn't included and since we don't care about the order of frequencys that are equal we can safely trim off without being pedantic over the results list.

## Analyze Complexity

```
Time Complexity: O(4n) -> O(n)

Space Complexity: O(2n) -> O(n)

```
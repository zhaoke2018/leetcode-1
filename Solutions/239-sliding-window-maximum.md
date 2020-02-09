- [Intro](#intro)
- [Topics](#topics)
- [Queue Monotonous](#queue-monotonous)
- [DP](#dp)
- [Brute Force](#brute-force)

## Intro

- https://leetcode.com/problems/sliding-window-maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
Follow up:
Could you solve it in linear time?

## Topics

- `Heap`
- `Queue - Monotonous`
- `Sliding Window`


## Queue Monotonous

- https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/





## DP

...



## Brute Force

- 时间复杂度：O(Nk)。其中 N 为数组中元素个数。
- 空间复杂度：O(N−k+1)，用于输出数组。


```py
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        
        return [max(nums[i:i + k]) for i in range(n - k + 1)]
```


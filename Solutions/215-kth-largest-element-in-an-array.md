- [Intro](#intro)
- [Topics](#topics)
- [Sort](#sort)
- [Heap](#heap)

## Intro

- https://leetcode.com/problems/kth-largest-element-in-an-array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


## Topics

- `Divide and Conquer`
- `Heap`



## Sort

- 最佳解法
- 最佳时间复杂度为 nlog(n)



```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
```

## Heap
```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return heapq.heappop()
```




- [Intro](#intro)
- [Topics](#topics)
- [Heap](#heap)
- [Brute Force](#brute-force)

## Intro

- https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

## Topics

- `Binary Search`
- `Heap`



## Heap

- [python要点] 注意使用 list comprehension 压平二维数组的时候, 要先处理二维.


```py
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # flaten 2d list
        matrix = [i for level in matrix for i in level]
        # build heap
        return heapq.nsmallest(k, matrix)[-1]
```


## Brute Force

- 不能一行行遍历, 因为行与行之间不是有序的.
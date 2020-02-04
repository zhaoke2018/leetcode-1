- [Intro](#intro)

## Intro

- https://leetcode.com/problems/range-sum-query-mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.
Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

- https://leetcode.com/problems/range-sum-query-mutable/ binaryIndexedTree / segmentTree
  - 给定一个数组,但是中间会对数组进行更新操作,所以就不能用dp了.mutable就需要segment tree之类的来辅助了.
  - [segmentTree] 虽然update某个元素,其他未update的部分sum还是可以复用的嘛
  - https://leetcode.com/problems/range-sum-query-mutable/solution/



## Topics

- `Binary Indexed Tree`
- `Segment Tree`


## xx
- https://leetcode.com/problems/range-sum-query-mutable/ binaryIndexedTree / segmentTree
  - 给定一个数组,但是中间会对数组进行更新操作,所以就不能用dp了.mutable就需要segment tree之类的来辅助了.
  - [segmentTree] 虽然update某个元素,其他未update的部分sum还是可以复用的嘛
  - https://leetcode.com/problems/range-sum-query-mutable/solution/

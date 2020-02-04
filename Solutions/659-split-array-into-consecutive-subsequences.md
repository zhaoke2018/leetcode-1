- [Intro](#intro)

## Intro

- https://leetcode.com/problems/split-array-into-consecutive-subsequences

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
 
Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5


Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5


Example 3:

Input: [1,2,3,4,4,5]
Output: False

 
Constraints:

1 <= nums.length <= 10000

 


### Leetcode- 659. Split Array into Consecutive Subsequences

- 如果可以将序列划分为「至少3个连续递增子序列」就返回 True https://leetcode.com/problems/split-array-into-consecutive-subsequences/
  - 贪心去找就行. 所有序列都要满足3位, 满足了之后进入待增长状态, 表示还可以继续接纳新的连续数字.

```py
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
```





## Topics

- `Heap`
- `Greedy`



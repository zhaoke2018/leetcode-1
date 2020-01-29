

### Leetcode- 659. Split Array into Consecutive Subsequences

- 如果可以将序列划分为「至少3个连续递增子序列」就返回 True https://leetcode.com/problems/split-array-into-consecutive-subsequences/
  - 贪心去找就行. 所有序列都要满足3位, 满足了之后进入待增长状态, 表示还可以继续接纳新的连续数字.

```py
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
```




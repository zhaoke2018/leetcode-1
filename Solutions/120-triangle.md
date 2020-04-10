- [Intro](#intro)
- [Topics](#topics)
- [DP - Bottom up](#dp---bottom-up)
- [DP - Top down](#dp---top-down)

## Intro

- https://leetcode.com/problems/triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


## Topics

- `Array`
- `Dynamic Programming`


## DP - Bottom up

- 感觉这道题可以让我弄懂 01背包 的 bottom-up 原因.
- 贪心肯定不靠谱, 因为最佳路线很可能一开始被埋没. 
- 如果要保证全局最优, 那么必然要记录所有内容.

- [秘诀] 这个题目为什么要条件反射 bottom-up 呢? 因为收敛的永远是最好的. 哈哈哈

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 倒过来, 都不用新建额外的空间了.
        for row in range(len(triangle)-2, -1, -1):
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])
        
        return triangle[0][0]
```


## DP - Top down

- 需要维护一个庞大的二维数组

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
```
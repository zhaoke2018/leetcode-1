- [Intro](#intro)
- [思路对比](#%e6%80%9d%e8%b7%af%e5%af%b9%e6%af%94)
- [DP By John](#dp-by-john)
- [BFS By John](#bfs-by-john)

## Intro

- https://leetcode.com/problems/perfect-squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.



## Topics

- `Math`
- `Dynamic Programming`
- `Breadth-first Search`


## 思路对比


- Perfect Square 最少需要几个平方数,使得和为n? 
  - 不能使用最大的平方数辗转相减, 比如12=4+4+4, 而不是12=9+1+1+1, 而是要把所有的可能的平方数都检查一遍.
  - BFS 可以使用 recursion 或者 队列.


- Python 知识点
1.  如何实现 `j=0; j*j<i; j++`


- [] DP 与 DFS 哪个解法更好?
- 对比一下复杂度就可以了.





## DP By John

```py
# Time Complexity: O(n*n^1/2)
# Space Complexity: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        # 先将平方数存起来
        sq_num = [i*i for i in range(1, n//2+1)] # 警告! 这里必须使用根号, 不然会超时
        dp = [n for i in range(n+1)] # 设为 int_max 也可以
        dp[0] = 0
        
        for i in range(1, n+1): # 计算每一个数需要多少步
            for j in sq_num: # 所有可能的平方数都检查一下, 以防止 12 = 4+4+4 的情况被 9 覆盖

                if i >= j:
                    dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1]
```


## BFS By John



```py
class Solution:
    def numSquares(self, n: int) -> int:
        
        def bfs(n, step):
            if n == 0:
                return step
            print('step', step)
            for sqn in sqns:
                if n >= sqn:
                    bfs(n-sqn, step+1)


        sqns = [i*i for i in range(1, n//2+1)]
        # print(sqns)
        return bfs(n, 0)

```
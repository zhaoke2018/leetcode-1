- [Intro](#intro)

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


## DP

```py
from typing import List

# class Solution:
#     def numSquares(self, n: int) -> int:
        
#         def bfs(n, step):
#             if n == 0:
#                 return step
#             print('step', step)
#             for sqn in sqns:
#                 if n >= sqn:
#                     bfs(n-sqn, step+1)


#         sqns = [i*i for i in range(1, n//2+1)]
#         # print(sqns)
#         return bfs(n, 0)

class Solution:
    def numSquares(self, n: int) -> int:
        # 先将平方数存起来
        sq_num = [i*i for i in range(1, n//2+1)] 
        dp = [n for i in range(n+1)] # 设为 int_max 也可以
        dp[0] = 0
        
        for i in range(1, n+1): # 计算每一个数需要多少步
            for j in sq_num: # 所有可能的平方数都检查一下, 以防止 12 = 4+4+4 的情况被 9 覆盖

                if i >= j:
                    dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1]

sol = Solution().numSquares(13)
print(sol)
```
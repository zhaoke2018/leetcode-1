- [Intro](#intro)
- [DP](#dp)
- [Search with memo](#search-with-memo)


## Intro

- https://leetcode.com/problems/integer-break/



## DP

```py
class Solution:
    def integerBreak(self, n: int) -> int:
        # 暴力: 将所有拆分形式都遍历一次.
        # 回溯: 自顶向下, 不断拆分.
        # DP: 自底向上, 不断计算
        product = [0] * (n+1) # product[i] 表示 i 对应的最大拆分乘积
        product[1] = 1
        
        for i in range(2, n+1):
            for ka in range(1, i):
                product[i] = max(ka*(i-ka), ka*product[i-ka], product[i])
        return product[n]
```


## Search with memo

- 与普通 recursion 一样, 只不过在最开始做一下 “缓存访问” 就行了.

```py
class Solution:
    def integerBreak(self, n: int) -> int:
        def bfs(m):
            if m == 1:
                return 1
            if memo[m] != -1:
                return memo[m]

            for i in range(1, m):
                memo[m] = max(i*(m-i), i*bfs(m-i), memo[m])

            return memo[m]

        memo = [-1] * (n+1)
        memo[1] = 1
        
        return bfs(n)
```
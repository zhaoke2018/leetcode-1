- [Coin Change](#coin-change)
- [Coin Change 2](#coin-change-2)

## Coin Change


```py
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)] # 最多n个硬币, 初始化n+1就很安全
        dp[0] = 0
        print(dp)

        for i in range(amount+1):
            for coin in coins:
                if i>=coin: # i 是要找零的钱数
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        print(dp)
        res = dp[-1] if dp[-1] <= amount else -1
        return res


sol = Solution().coinChange([1, 2, 5], 11)
print(sol)
```



## Coin Change 2

- 为什么要把 coin 的循环放在外面呢?
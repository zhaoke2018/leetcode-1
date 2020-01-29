




- https://leetcode.com/problems/coin-change-2/
- 为什么要把 coin 的循环放在外面呢?



```py
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1 #???
        
        
        for coin in coins:
            for i in range(1, len(dp)): # 外层循环放所有的coin=1
                if i >= coin:
                    dp[i] += dp[i-coin] #???
                    
        return dp[-1]
```
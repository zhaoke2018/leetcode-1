- [Intro](#intro)

## Intro

- https://leetcode.com/problems/coin-change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.




## Topics

- `Dynamic Programming`


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




## coin change xxxx


- 用最少硬币数找零 https://leetcode.com/problems/coin-change/
- [Greedy] 从面额大的开始找,用小面额补足. 但是 12 = 4+4+4 这种就可能被忽略
  - https://www.youtube.com/watch?v=9dZzyl7dCuw
- [DP] 如果最小的硬币是1,就可以用贪心算法;如果是最小是2,但是要找11块,那就只能用动态规划了.
  - [技巧] 最多找零n个硬币, 那么初始化n+1就很安全; 使用 int_max 会在累加的时候溢出.
  - [陷阱] 如果要拆分的是2, 而最小金额是5, 那么就无法找零. 并且初始化DP也是个问题.
    - 其实如果 i 找不到, 那么 dp[i] 就会保持初始值.
- https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/


```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)] # 最多n个硬币, 初始化n+1就很安全
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i>=coin: # i 是要找零的钱数
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        res = dp[-1] if dp[-1] <= amount else -1
        return res
```





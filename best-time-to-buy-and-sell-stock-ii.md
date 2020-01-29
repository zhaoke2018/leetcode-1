
- 可多次交易同一支股票,但是必须卖完之后再买 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ greedy/easy
  - `Greedy` 只要第二天价格比第一天高,就进行买卖


```py
def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0
    for i in range(1, len(prices)):
        maxProfit += prices[i] - prices[i-1] if prices[i]>prices[i-1] else 0
    return maxProfit
```


- 给定数组 price, 最多交易一次 https://leetcode.com/problems/best-time-to-buy-and-sell-stock
  - `DP` 循环找到最低价, 同时求出最大profit
    - 通用收获: 求最值,循环中不断max.
    - 也许是一种新类型 DP?
  - `brute force` 找到price[j]-price[i]的最大值,j>i.


```py
def tradeStock(prices):
  int max_profit=0, min_buy=INT_MAX
  for i in prices:
    min_buy = min(min_buy, prices[i]) # 先 确定历史最低价
    max_profit = max(max_profit, prices[i]-min_buy) # 再 用当前价格-历史最低价,作为利润
  return max_profit
```

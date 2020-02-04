- [Intro](#intro)
- [DP](#dp)

## Intro

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


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



## Topics

- `Array`
- `Dynamic Programming`


## DP
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

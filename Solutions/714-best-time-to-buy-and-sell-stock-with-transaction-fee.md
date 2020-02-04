- [Intro](#intro)

## Intro

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.
Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.



Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee dp/greedy/medium


- http://bangbingsyb.blogspot.com/2014/11/leetcode-best-time-to-buy-and-sell.html


```py
def maxProfit(self, prices: List[int], fee: int) -> int:
    maxProfit = 0
    for i in range(len(prices)):
        maxProfit = prices[i] - prices[i-1] - 2 if prices[i]>prices[i-1]+2 else 0
    return maxProfit
```



- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee dp/greedy/medium


- http://bangbingsyb.blogspot.com/2014/11/leetcode-best-time-to-buy-and-sell.html


```py
def maxProfit(self, prices: List[int], fee: int) -> int:
    maxProfit = 0
    for i in range(len(prices)):
        maxProfit = prices[i] - prices[i-1] - 2 if prices[i]>prices[i-1]+2 else 0
    return maxProfit
```



## Topics

- `Array`
- `Dynamic Programming`
- `Greedy`





- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee dp/greedy/medium


- http://bangbingsyb.blogspot.com/2014/11/leetcode-best-time-to-buy-and-sell.html


```py
def maxProfit(self, prices: List[int], fee: int) -> int:
    maxProfit = 0
    for i in range(len(prices)):
        maxProfit = prices[i] - prices[i-1] - 2 if prices[i]>prices[i-1]+2 else 0
    return maxProfit
```


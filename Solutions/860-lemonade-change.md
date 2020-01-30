- [Intro](#intro)

## Intro

- https://leetcode.com/problems/lemonade-change

At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
Note that you don't have any change in hand at first.
Return true if and only if you can provide every customer with correct change.
 

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.


Example 2:

Input: [5,5,10]
Output: true


Example 3:

Input: [10,10]
Output: false


Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

 
Note:

0 <= bills.length <= 10000
bills[i] will be either 5, 10, or 20.







- 在自己没有任何钱的情况下, 检测是否能给每个顾客找钱. https://leetcode.com/problems/lemonade-change/
  - 基本没涉及什么算法知识, 没啥价值


考点
1. Greedy: 由于本题分类少, 所以基本上翻译题意就行了.
  - 优化: 20 不需要记录.


```py
def lemonadeChange(self, bills: List[int]) -> bool:
    changes = dict() # 20, 10, 5 的个数
    changes['5'] = 0
    changes['10'] = 0
    changes['20'] = 0

    for i in bills:
        if i == 5:
            changes['5'] += 1
        if i == 10:
            changes['10'] += 1
            if changes['5'] > 0:
                changes['5'] -= 1
            else:
                return False
        if i == 20:
            changes['20'] += 1
            if changes['10'] > 0 and changes['5'] > 0:
                changes['10'] -= 1
                changes['5'] -= 1
            elif changes['5'] >= 3:
                changes['5'] -= 3
            else:
                return False
    return True
```




```py
class Solution(object):
    def minSwapsCouples(self, row):
        N = len(row)
        d = [0] * N
        
        def find(a):
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]
    
        def union(a,b):
            d[find(a)] = find(b)
        
        # Initialize DS
        for i in xrange(0, N, 2):
            d[i] = d[i+1] = i
        
        # Union find
        for i in xrange(0, N, 2):    
            union(row[i], row[i+1])
        
        # Total sets - available sets
        return (N//2) - sum([1 for i in xrange(0, N, 2) if i == d[i] == d[i+1]])
```







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





- [Intro](#intro)

## Intro

- https://leetcode.com/problems/4sum-ii

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

 


```py
from typing import List
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter([a+b for a in A for b in B])
        return sum([AB[-c-d] for c in C for d in D])

sol = Solution().fourSumCount([ 1, 2], [-2,-1], [-1, 2], [ 0, 2])

print(sol)

```




- 返回sum为0的组合有几种 https://leetcode.com/problems/4sum-ii
- [思路] 本题并不要求列出所有tuple，只求个数而已，因此实现起来很简单。首先dict算出AB各种组合之和的次数。然后计算CD之和相反数即可。
- [巧妙] 相反数的神奇特性。
- [Python] collections.counter 就是一个 hash dict 而已



```py
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter([a+b for a in A for b in B])
        return sum([AB[-c-d] for c in C for d in D])
```





```py
def nSum_brute(sum, arr, n):
  for i in arr: # 从arr开始找n个数
    sum_res = sum-i
    arr_res = arr.remove(i)
    if sum_res == 0:
      return True
    elif sum_res < 0:
      return False
    else:
      return nSum_brute(sum_res, arr_res, n-1)
```




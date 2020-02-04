- [Intro](#intro)

## Intro

- https://leetcode.com/problems/daily-temperatures


Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].



- https://leetcode.com/problems/daily-temperatures/



## Topics

- `Hash Table`
- `Stack`


## 我写的

- nexti 应该从 i+1 开始, 那么 step 就得从 1 开始, 但是找不到更高温的时候, step=0
- 始终各种矛盾

```py
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for i in range(len(T))]
        print(T)
        for i in range(len(T)):
            nexti = i
            step = 0
            print('---', nexti, step)
            still_colder = T[i] >= T[nexti]
            while still_colder and nexti < len(T)-1:
                # if i!=nexti:
                #     continue # dead loop
                print('nexti', nexti)
                nexti += 1
                step += 1
            
            # if nexti == len(T)-1 and T[i] >= T[nexti]: # 找不到, 置为0
            #     res[i] = 0
            # else:
            #     res[i] = step
            res[i] = step
        
        return res

sol = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(sol)
```


## 标准答案

- 不知道是怎么想出来的.

```py
class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] # [hot, cold] indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]: # 把 T[i] 
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
```
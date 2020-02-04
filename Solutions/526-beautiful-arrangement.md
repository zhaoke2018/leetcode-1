- [Intro](#intro)

## Intro

- https://leetcode.com/problems/beautiful-arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.

 
Now given N, how many beautiful arrangements can you construct?
Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

 
Note:

N is a positive integer and will not exceed 15.

 



## Topics

- `Backtracking`


## 基本信息

- https://leetcode.com/problems/beautiful-arrangement/
- 经典 bfs/ dfs 套路
  - 一个参数发射, 一个参数接收. 接收完成就是一个阶段性成果了.





## 我自己的尝试

```py
class Solution:
    def countArrangement(self, N: int) -> int:
        # num[i] 与 i 可以整除, one way or another
        # 判断
        def dfs(nums, sres):
            if len(sres) == N:
                print('阶段性结果', sres)
                self.ans += 1
            for i in range(len(nums)):
                ith = len(sres)
                print('i+1', i+1, 'ith+1', ith+1, 'calcul', (i+1) % (ith+1))
                if (i+1) % (ith+1) == 0 or (ith+1) % (i+1) == 0:
                    dfs(nums[i+1:], sres+[nums[i]])
        
        if N == 0:
            return 0
        nums = [i+1 for i in range(N)]
        self.ans = 0
        dfs(nums, [])
        return self.ans
```


## 标准答案




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


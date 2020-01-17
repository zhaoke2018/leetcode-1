- [我自己写的答案](#%e6%88%91%e8%87%aa%e5%b7%b1%e5%86%99%e7%9a%84%e7%ad%94%e6%a1%88)
- [参考答案](#%e5%8f%82%e8%80%83%e7%ad%94%e6%a1%88)


## 我自己写的答案

- 是否通过?






```py
from typing import List
"""
知识点
1. 本题重点在于如何记录中间过程. 一维数组就可以记录所有内容了.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, res, [])
        return res
    
    # nums: 代表每行的位置 [2, 1, 3]
    def dfs(self, nums, nth, res, cur_res):
        if nth == len(nums): # 到这一步, 所有行都放好了Queen, 虽然nth是从0开始的,但是要到计算到n-1, 因此到n再结束没毛病
            res.append(cur_res)
            print('本次递归结束\n', cur_res)
            print('-----------------总结果\n', res)
            return
        for i in range(len(nums)): # 每行从左到右所有位置都试一下
            nums[nth] = i
            if self.valid(nth, nums):
                new_line = i*'.' + 'Q' + (len(nums)-1-i)*'.'
                print('new line', new_line)
                # cur_res.append(new_line)
                # new_line = "."*len(nums)
                # cur_res += [new_line[:i]+"Q"+new_line[i+1:]] # + / append 效果一样

                self.dfs(nums, nth+1, res, cur_res+[new_line]) # 计算下一行

    def valid(self, nth, nums):
        for i in range(nth):
            diagnal_attack = abs(nums[nth]-nums[i]) == abs(nth-i)
            vertical_attack = nums[nth] == nums[i]
            if diagnal_attack or vertical_attack:
                return False
        return True


sol = Solution().solveNQueens(4) 
# print(sol)
```


## 参考答案

```py

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    
    # nums: 一维数组, 表示 Queen 在每行的位置
    # index: 当前处理的行
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)): # 对于每行, 不断试探应该放在哪里
            nums[index] = i 
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # 在 nth 行是否能放 Queen
    def valid(self, nums, n):
        for i in range(n): # 检查前n行数据
            diagnal_attack = abs(nums[i]-nums[n]) == n-i
            vertical_attack = nums[i] == nums[n]
            if diagnal_attack or vertical_attack:
                return False
        return True


sol = Solution().solveNQueens(4)
print(sol)
```
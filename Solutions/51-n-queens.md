- [Intro](#intro)
- [Topics](#topics)
- [Backtracking](#backtracking)
  - [to debug](#to-debug)
  - [简单版](#%e7%ae%80%e5%8d%95%e7%89%88)

## Intro

- https://leetcode.com/problems/n-queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.










## Topics

- `Backtracking`



## Backtracking

```py
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

### to debug

- 是否通过?


- [重点] 本题重点在于如何记录中间过程. 一维数组就可以记录所有内容了.

```py
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
```

### 简单版

```py
class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```

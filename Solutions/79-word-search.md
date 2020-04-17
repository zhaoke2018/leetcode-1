- [Intro](#intro)
- [Topics](#topics)
- [Backtracking](#backtracking)

## Intro

- https://leetcode.com/problems/word-search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.






## Topics

- `Array`
- `Backtracking`


## Backtracking

- https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
- 直接去找就行了，不需要建立树
- 我怎么感觉更像是 DFS 呢?

- [WHY] 为什么需要把 `board[x][y]` 变回原来的值呢? 
  - 因为传入来的是数组, call by reference, 所以如果不变回去的话, 之后别的路径找到这个元素, 就会出错.
- [WHY] 以下两段代码不是基本一模一样吗? 怎么第一份就提交超时了!
  - 主要还是 up / down / left / right 那个地方有问题, 第一份代码中, 上下左右都会先计算完, 而 caikehe 的代码, 只要第一个方向满足条件就不再计算递归其他方向. 这样一来, 当整个 board 都是 'a' 的时候, 优势就很明显了.




```py
# 超时代码
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_ in range(len(board)):
            for letter_ in range(len(board[0])):
                if self.findNext(board, word, row_, letter_):
                    return True
        return False
        
    def findNext(self, board, word, x, y):
        # print('next step: ', word, x, y)
        if not word:
            # print('找到啦!')
            return True
        
        # 统一判断终止条件
        if x < 0 or y < 0 or x > len(board)-1 or y > len(board[0])-1 or board[x][y] != word[0]:
            return False
        
        tmp = board[x][y]
        board[x][y] = '#'

        down = self.findNext(board, word[1:], x+1, y)
        up = self.findNext(board, word[1:], x-1, y)
        right = self.findNext(board, word[1:], x, y+1)
        left = self.findNext(board, word[1:], x, y-1)
        
        board[x][y] = tmp # 为什么要还原呢? 有何意义?
        return down or up or right or left

```




```py
# caikehe
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
```







- [Intro](#intro)
- [Topics](#topics)
- [Backtacking by John](#backtacking-by-john)
- [Backtracking by Leetcode](#backtracking-by-leetcode)




## Intro

- https://leetcode.com/problems/sudoku-solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

A sudoku puzzle...

...and its solution numbers marked in red.
Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.







## Topics

- `Hash Table`
- `Backtracking`


## Backtacking by John


- [WHY] 递归的时候，先修改数组再递归 vs 在参数中递归，差别在哪里呢？
- [WHY] 主函数里, 最后那两个 return 是解题的关键, 但是我还是不懂他们的必要性.

- 参考自 https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
  - 我之前自己写的已经很接近这个解法了！还是直接看最高票的解答最高效啊！
  - 与其想出知识，不如快速学习经验。与其慢慢debug，不如直接对比最优解。在“发现问题”和“解决问题”两方面都要快，缺一不可。
  - Debug 过程可以提升代码分析能力, leetcode有很多标准答案对比, 工作中可没有对比, 只能自己根据代码分析.



```py
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):

                if board[i][j] == '.': # 找到一个空, 开始填!
                    for num in range(1, 10):
                        if self.valid(board, str(num), i, j): # 对于第一个".", 除去肯定不valid的, 其余所有的数都试一下.
                            board[i][j] = str(num)
                            if self.solveSudoku(board): # 这样可以防止 invalid 的时候修改 board
                                return True
                            else:
                                board[i][j] = '.'
                    
                    # 对于某个格子, 所有的数字都不合法, 这种情况会出现吗?
                    return False # 没有这句话, 棋盘只会改一部分
        
        # 棋盘遍历完成之后, 所有格子都应该填满了, 此时是否返回很重要吗?
        return True # 没有这句话, 棋盘不会改

    def valid(self, board: List[List[str]], num: str, i: int, j: int) -> bool:
        for row in range(9):
            if i != row and num == board[row][j]: # 同列, 对比不同行
                return False
        for col in range(9):
            if j != col and num == board[i][col]: # 同行 对比不同列
                return False
        
        row_sec = i//3 # 012 / 345 / 678
        col_sec = j//3
        for row in range(row_sec*3, row_sec*3+3): # [2, 4]
            for col in range(col_sec*3, col_sec*3+3):
                if i!=row and j!=col and board[row][col] == num:
                    return False
        return True
```





## Backtracking by Leetcode

- 好难看懂...

```py
from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion to continue to place numbers till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        print()
        sudoku_solved = False
        backtrack()

boardd = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


Solution().solveSudoku(boardd)

print(boardd)
```















- [基本情况](#%e5%9f%ba%e6%9c%ac%e6%83%85%e5%86%b5)
- [Backtacking by me](#backtacking-by-me)
- [Backtracking by Leetcode](#backtracking-by-leetcode)
- [忘记这个是干嘛的](#%e5%bf%98%e8%ae%b0%e8%bf%99%e4%b8%aa%e6%98%af%e5%b9%b2%e5%98%9b%e7%9a%84)
- [Sudoku Java](#sudoku-java)



## 基本情况

- 填完一个Sudoku https://leetcode.com/problems/sudoku-solver/






## Backtacking by me

TODO
- 递归的时候，先修改数组再递归 vs 在参数中递归，差别在哪里呢？

- 参考自 https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
  - 我之前的解法已经很接近了！看来还是直接看最高票的解答最高效啊！
  - 与其想出知识，不如快速学习经验。与其慢慢debug，不如直接对比最优解。在“发现问题”和“解决问题”两方面都要快，缺一不可。


```py
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solver(board)

    def solver(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        
                        if self.valid(board, str(num), i, j): # 对于第一个".", 除去肯定不valid的, 其余所有的数都试一下.
                            board[i][j] = str(num)

                            if self.solver(board): # 这样可以防止 invalid 的时候修改 board
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

## 忘记这个是干嘛的


- Debug 过程可以提升代码分析能力, leetcode有很多标准答案对比, 工作中可没有对比, 只能自己根据代码分析.



```py
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solver(board)

    def solver(self, board: List[List[str]]) -> None:

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        
                        # print(i, j, board[i][j])

                        if self.valid(board, str(num), i, j): # 对于第一个".", 除去肯定不valid的, 其余所有的数都试一下.
                            # print('location ', i, j, 'new number', board[i][j])
                            board[i][j] = str(num)
                            self.solver(board)
                        # else: # 这条路走不通: 剪枝
                        #     continue
                        
                        
        
    def valid(self, board: List[List[str]], num: str, i: int, j: int) -> bool:
        for row in range(9):
            # print('same col', board[i][j], board[row][j])
            if i != row and board[i][j] == board[row][j]: # 同列, 对比不同行
                return False
        for col in range(9):
            # print('same row', board[i][j], board[i][col])
            if j != col and board[i][j] == board[i][col]: # 同行 对比不同列
                return False
        
        row_sec = i//3 # 012 / 345 / 678
        col_sec = j//3
        # print(row_sec, col_sec)
        for row in range(row_sec*3, row_sec*3+3): # [2, 4]
            for col in range(col_sec*3, col_sec*3+3):
                # print('same sec', row, col, board[row][col])
                if i!=row and j!=col and board[row][col] == board[i][j]:
                    return False
        return True

boardd = [
  ["5","3","4",".","7",".",".",".","."],
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

# sol = Solution().valid(boardd, 0, 2)
# print(sol)



```


## Sudoku Java


```java
public class Solution {
    public void solveSudoku(char[][] board) {
        if(board == null || board.length == 0)
            return;
        solve(board);
    }
    
    public boolean solve(char[][] board){
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == '.'){
                    for(char c = '1'; c <= '9'; c++){//trial. Try 1 through 9
                        if(isValid(board, i, j, c)){
                            board[i][j] = c; //Put c for this cell
                            
                            if(solve(board))
                                return true; //If it's the solution return true
                            else
                                board[i][j] = '.'; //Otherwise go back
                        }
                    }
                    
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, int row, int col, char c){
        for(int i = 0; i < 9; i++) {
            if(board[i][col] != '.' && board[i][col] == c) return false; //check row
            if(board[row][i] != '.' && board[row][i] == c) return false; //check column
            if(board[3 * (row / 3) + i / 3][ 3 * (col / 3) + i % 3] != '.' && 
board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false; //check 3*3 block
        }
        return true;
    }
}
```


















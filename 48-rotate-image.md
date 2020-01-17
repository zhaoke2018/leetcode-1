







- https://leetcode.com/problems/rotate-image/

考点
- [坐标操作] 代入一个实例即可.
- 只需变换一半坐标即可.


```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mlen = len(matrix)
        
        # 沿 \ 对折
        for x in range(mlen):
            for y in range(mlen):
                if x > y: # 这样就可以保证只执行一般
                    matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        # 沿 | 对折
        for row in range(mlen):
            for col in range(mlen//2):
                matrix[row][col], matrix[row][mlen-col-1] = matrix[row][mlen-col-1], matrix[row][col]
```
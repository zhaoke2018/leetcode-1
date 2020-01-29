




## Intro


- https://leetcode.com/problems/rotate-image/

考点
- [坐标操作] 代入一个实例即可.
- 只需变换一半坐标即可.


https://leetcode.com/problems/rotate-image/discuss/18965/Comprehensible-python-solution

- [思路] 这个解法真的很难想到，即使看答案之后，还要自己举例来验证。求数学证明出处。


举例
原始数组
123
456
789

2 loops 实现对角线对折
147
258
369

Reverse 实现水平翻转
741
852
963



## Array Maniplation By John

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
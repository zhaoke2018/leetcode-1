- [Intro](#intro)

## Intro

- https://leetcode.com/problems/rotate-image

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]






## Intro xx


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
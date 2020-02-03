- [Intro](#intro)
- [xxx](#xxx)

## Intro

- https://leetcode.com/problems/01-matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
 
Example 1: 

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2: 

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

 
Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

## xxx

- [思路] 遵循标准流程, 将所有的0入队, 作为初始条件. 然后层次遍历, 依次得出距离. 由于图会产生交错, 因此一定要记得用 visited 记录.



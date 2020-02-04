- [Intro](#intro)
- [xxx](#xxx)

## Intro

- https://leetcode.com/problems/rotting-oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
 

Example 1:


Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4


Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.


Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

 
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.




## Topics

- `Breadth-first Search`


## xxx

- 模板不熟悉就比较头大，不过跟之前那个01 matrix差不多。
- 将所有2元素的坐标入队，然后出队的时候将周围的坐标都变成2，直到下标out bound，最后问一下整个2d数组，还有1吗？



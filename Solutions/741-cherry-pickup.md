- [Intro](#intro)

## Intro

- https://leetcode.com/problems/cherry-pickup

In a N x N grid representing a field of cherries, each cell is one of three possible integers.
 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

 
Your task is to collect maximum number of cherries possible by following the rules below:
 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

 
 
Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

 
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

 




- 左上角到右下角,然后再回来,求可摘到最多的樱桃数. 
  - https://leetcode.com/problems/cherry-pickup/
  - 贪心做出来的就是单程,不是全程最优.
  - 每个格子都有值,0=可通过,1=有樱桃(摘了就置0),-1=不可通过.
  - 本题难点在于需要返回,想起来有点麻烦,但是将其展开成两面来看待就简单了,

```py
class Solution(object):
    def cherryPickup(self, grid):
        row, column = len(grid), len(grid[0])
        for i in xrange(row)
```

```js
/**
 * @param {number[][]} grid
 * @return {number}
 */
var cherryPickup = function(grid) {
    var maxY = grid.length;
    var maxX = grid[0].length;
    var memo = {};
    function dp(yPersonA, xPersonA, xPersonB) {
        //work out corrosponding Y variable for personB. (works since personA and personB have made the same number of moves)
        var yPersonB = yPersonA + xPersonA - xPersonB;

        //key for the current state
        var memoKey = yPersonA + "_" + xPersonA + "_" + xPersonB;

        //work out if we are out of bounds
        var overTheEdge = maxY == yPersonA || maxY == yPersonB || maxX == xPersonA || maxX == xPersonB; //we are actually over the edge HERE!!
        if (overTheEdge) {
            return -999999;
        }

        var personAHitAThorn = grid[yPersonA][xPersonA] == -1;
        var personBHitAThorn = grid[yPersonB][xPersonB] == -1;
        if (personAHitAThorn || personBHitAThorn) {
            //impossible move, either over the edge or directly on a thorn
            return -999999;
        } else if (yPersonA == maxY - 1 && xPersonA == maxX - 1) {
            //reached the target finally
            return grid[yPersonA][xPersonA];
        } else if (memo[memoKey] !== undefined) {
            //already visited
            return memo[memoKey];
        } else {

            var personAHasCherry = grid[yPersonA][xPersonA] === 1;
            var personBHasCherry =
                yPersonB !== yPersonA && xPersonB !== xPersonA && //if personA didn't take it first!
                grid[yPersonB][xPersonB] === 1;

            var cherriesCollectedByBothPeopleThisTurn =
                (personAHasCherry ? 1 : 0) +
                (personBHasCherry ? 1 : 0);

            //both people make all possible single moves they can make (down and right)
            //personB by definition will likely always be on a different path than personA since:
            //   *   it will generate more COMBINED cherries (see above cherriesCollectedByBothPeopleThisTurn)
            var maxCherriesCollectedByBothPeopleForRemainingTurns = Math.max(
                Math.max(
                    dp(yPersonA, xPersonA + 1, xPersonB + 1), //personA right personB right
                    dp(yPersonA + 1, xPersonA, xPersonB + 1)), //personA down personB right
                Math.max(
                    dp(yPersonA, xPersonA + 1, xPersonB), //personA right personB down
                    dp(yPersonA + 1, xPersonA, xPersonB)) //personA down personB down
                );

            var cherriesCollectedRecursive = cherriesCollectedByBothPeopleThisTurn + maxCherriesCollectedByBothPeopleForRemainingTurns;
            memo[memoKey] = cherriesCollectedRecursive;
            return cherriesCollectedRecursive;
        }
    }

    return Math.max(0, dp(0, 0, 0));
}
```


## Topics

- `Dynamic Programming`



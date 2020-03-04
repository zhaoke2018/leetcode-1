- [Intro](#intro)
- [Topics](#topics)
- [Top Down](#top-down)
  - [Recurssion?](#recurssion)

## Intro

- https://leetcode.com/problems/reaching-points

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True


Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].



## Topics

- `Math` use remainder


## Top Down


- 貌似从终点入手比较好做, 但是不理解为什么..
- 这么写可以看懂, 但是如何理解呢?
- 由于本题对时间要求很高, 逐步累加会超时. 因此可以采用 **取余** 的方法快速缩小到一个快速计算的范围.

```py
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        # reached right edge, and check if move up will meet
        moveUp = sx == tx and sy <= ty and (ty - sy) % sx == 0

        # reached up edge, then check if move right will meet
        moveRight = sy == ty and sx <= tx and (tx - sx) % sy == 0

        return  moveUp or moveRight
```

### Recurssion?

- 如果要递归的话, 怎么写?




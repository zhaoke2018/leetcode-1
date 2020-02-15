- [Intro](#intro)
- [Topics](#topics)
- [Greedy](#greedy)

## Intro

- https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.
Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

 


## Topics

- `Greedy`


## Greedy

- [解释] 见注释

```py
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float('-inf') # 在循环中, end 表示 max(之前节点的终点)
        res = 0
        for ball in sorted(points, key=lambda x: x[1]): # 默认 升序
            # 所以当 “节点的起点” 比 “max(之前节点的终点)” 小, 说明这两个区间有重叠!
            if ball[0] > end: # if 当前坐标起点 > end
                res += 1
                end = ball[1] # end = 当前坐标终点
        return res
```
- [Intro](#intro)
- [Topics](#topics)
- [JJJ](#jjj)

## Intro

- https://leetcode.com/problems/the-skyline-problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
    
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]



## Topics

- `Divide and Conquer`
- `Heap`
- `Binary Indexed Tree`
- `Segment Tree`
- `Line Sweep`

- `Multiple Methods`


## JJJ

- 这篇好像讲得不错 http://wlcoding.blogspot.com/2015/05/the-skyline-problem.html
- https://www.educative.io/edpresso/the-skyline-problem-in-cpp
- https://medium.com/@dimko1/the-skyline-problem-c999466b7778

```py
# TODO 优化 拐点只会发生在房子的两端
def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    xs = max([bld[1] for bld in buildings]) + 2 # 表示 last Index 需要+1, 展示 last Index 的变化 也需要+1

    skyline_height = [0 for i in range(xs)] # 每个坐标都有一个 max height
    res = []

    # 更新天际线
    for bid in range(len(buildings)):
        for xx in range(buildings[bid][0], buildings[bid][1]+1): # xx 表示当前建筑的横坐标范围
            if buildings[bid][2] > skyline_height[xx]:
                skyline_height[xx] = buildings[bid][2]
    
    # 计算转折点
    for i in range(xs):
        if skyline_height[i] > skyline_height[i-1]:
            res.append([i, skyline_height[i]])
        elif skyline_height[i] < skyline_height[i-1]:
            res.append([i-1, skyline_height[i]])

    return res

# failed at case: [[0,2147483647,2147483647]] Memory Limit Exceeded
```
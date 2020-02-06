- [Intro](#intro)
- [Topics](#topics)
- [BFS](#bfs)

## Intro

- https://leetcode.com/problems/cut-off-trees-for-golf-event

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.

 
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6

 
Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1

 
Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

 
Hint: size of the given matrix will not exceed 50x50.




## Topics

- `Breadth-first Search`
- `A*`
- `Hadlock`


## BFS


- 在一片 2d 森林中从矮到高砍树. 如果能一直砍完所有的树, 则返回一共要走多少步; 如果不能, 就返回-1. 砍完数, 原数字变为1, 0是不可以走的地方.
  - 解法 https://leetcode.com/articles/cutoff-trees-for-golf-event/


```py
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        steps = 0 # 当前走了多少步
        area = len(forest) * len(forest[0]) # 森林面积

        # 如果出现了路分叉, 选择数字较小的那条路即可.
        Q = collections.deque([forest[0][0]])
        while Q:
            curr = Q.popleft()
            find_next_smallest_spot = "TODO"
            if find_next_smallest_spot:
                steps += 1
                Q.append()
                forest[current_spot] = 1
            else: # 找不到, 到绝路了
                return steps if forest_doesnot_have_number_above_1 else -1

```



- [Intro](#intro)

## Intro

- https://leetcode.com/problems/maximum-depth-of-n-ary-tree

Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
 
Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

 
Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].




- 这道题 BFS / DFS 都能解,不算是 DFS 的典型题.
- 我想象的 DFS,应该是一路到底,然后记录长度.这里感觉是多路齐下, 更像是 BFS.

```py
def maxDepth_DFS(self, root):
    if root is None: return 0
    if root.children is None or root.children == []:
        return 1
    return max(map(self.maxDepth, root.children)) + 1 # 每个子节点递归到底,不断比较出最大的一个
```




## Topics

- `Tree`
- `Depth-first Search`
- `Breadth-first Search`



- [Intro](#intro)
- [Topics](#topics)
- [Recursion - Medium](#recursion---medium)

## Intro

- https://leetcode.com/problems/minimum-depth-of-binary-tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.



## Topics

- `Tree`
- `Depth-first Search`
- `Breadth-first Search`
- `Recursion - Medium`

## Recursion - Medium

- [思路] 最小深度，层次遍历过程中，遇到某个节点没有子节点，就可以返回当前层数了。
- [陷阱] 一柱擎天的树, 最小深度是那根柱的高度, 而不是1. 左右节点都没有, 才算终止!

```py
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def bfs(root, depth):

            if not root:
                return depth
            
            if not root.left: # 没有左树, 那么就看右树
                return bfs(root.right, depth+1)
            if not root.right:
                return bfs(root.left, depth+1)

            return min(bfs(root.left, depth+1), bfs(root.right, depth+1)) # 左右都有, 就都考虑

        return bfs(root, 0)
```


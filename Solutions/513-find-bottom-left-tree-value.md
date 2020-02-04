- [Intro](#intro)

## Intro

- https://leetcode.com/problems/find-bottom-left-tree-value


Given a binary tree, find the leftmost value in the last row of the tree. 

Example 1:

Input:

    2
   / \
  1   3

Output:
1

  Example 2: 

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note:
You may assume the tree (i.e., the given root node) is not NULL.



- https://leetcode.com/problems/find-bottom-left-tree-value/


- [基础思路] 层次遍历，返回最后一层的第一个元素即可
- [简易思路] 直接把所有的节点依次 **从右向左** 加入队列, 并过滤所有空节点, 这样最后一个节点就是题目要找的节点了.






```py
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        for node in queue: # 遍历过程中queue慢慢变长, for 可以保证不会重复遍历
            queue += filter(None, [node.right, node.left])

        return node.val # 最后一个处理的节点肯定就是最左边的嘛
```








## Topics

- `Tree`
- `Depth-first Search`
- `Breadth-first Search`



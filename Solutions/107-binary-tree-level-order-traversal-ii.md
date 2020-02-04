- [Intro](#intro)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/binary-tree-level-order-traversal-ii

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]




## Topics

- `Tree`
- `Breadth-first Search`


## Iteration By John

- 这太简单了！直接层次遍历就行了，最后reversed一下即可。
- [Intro](#intro)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]



## Iteration By John


- 在标准流程上, 加一个 level 记录当前层, 然后对奇数层记性 reverse 一下即可.
- 本题直接AC!

```py
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return None
    Q = collections.deque([root])
    res = []
    level = 0
    while Q:
        leng = len(Q)
        cur_level = []
        level += 1
        for i in range(leng):
            popi = Q.popleft()
            cur_level.append(popi.val)

            if popi.left: Q.append(popi.left) # BFS 核心
            if popi.right: Q.append(popi.right)
        
        if level % 2 == 0:
            res.append(reversed(cur_level))
        else:
            res.append(cur_level)
    return res         
```

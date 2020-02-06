- [Intro](#intro)
- [Topics](#topics)
- [BFS - Iteration](#bfs---iteration)
  - [一段错误的代码](#%e4%b8%80%e6%ae%b5%e9%94%99%e8%af%af%e7%9a%84%e4%bb%a3%e7%a0%81)

## Intro

- https://leetcode.com/problems/cousins-in-binary-tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
 
Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false


Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true


Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.





## Topics

- `Tree`
- `Breadth-first Search` 直接遍历整个树, 对于每个节点, 将其 父亲节点 和 深度信息 保存起来. 
  - [优化] 找到两个节点就可以结束了, 没必要遍历整棵树.



## BFS - Iteration



- faster than 99.90%

```py
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        def bfs(root, depth, father=None):
            if root:
                depthd[root.val] = depth
                parentd[root.val] = father
                if root.left:
                    bfs(root.left, depth+1, root)
                if root.right:
                    bfs(root.right, depth+1, root)
            
        bfs(root, 1)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]
```






### 一段错误的代码



- [WHY] My code runs perfectly locally, but got this error when I submit.

> Runtime Error Message: Line 29: KeyError: 1
> Last executed input:
> [1,null,2,3,null,null,4,null,5]
> 1
> 3


```py
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        Q = collections.deque([root])
        depth = 0
        
        while Q:
            level_len = len(Q)
            depth += 1
            for i in range(level_len):
                q = Q.popleft()
                if q.left:
                    depthd[q.left.val] = depth
                    parentd[q.left.val] = q
                    Q.append(q.left)
                if q.right:
                    depthd[q.right.val] = depth
                    parentd[q.right.val] = q
                    Q.append(q.right)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]
```



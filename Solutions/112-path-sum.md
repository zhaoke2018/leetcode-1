- [Intro](#intro)
- [Topics](#topics)
- [DFS Recursion](#dfs-recursion)
- [DFS Iteration](#dfs-iteration)
- [BFS Iteration](#bfs-iteration)

## Intro

- https://leetcode.com/problems/path-sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.




## Topics

- `Tree`
- `Depth-first Search`



- [Hash] ?



## DFS Recursion

- faster than 80%



```py
class Solution:
    def hasPathSum(self, root: TreeNode, sumi: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sumi-root.val == 0:
            return True
        
        # 智慧之处, left or right 有一个成功都行!
        return self.hasPathSum(root.left, sumi-root.val) or self.hasPathSum(root.right, sumi-root.val)
```


- [WHY] 为什么这种写法不行呢? 容易在遍历完第一个叶子的时候就过早返回. 怎么改呢?


```py
class Solution:
    def hasPathSum(self, root: TreeNode, sumi: int) -> bool:
        def dfs(node, yushu): # yushu: 余数
            if not node or yushu < 0:
                return False # 其他路径说不定还有解! 不要太早否定
            
            if yushu - node.val == 0:
                return True
            return dfs(node.left, yushu - node.val) or dfs(node.right, yushu - node.val)
            
        dfs(root, sumi)
```

## DFS Iteration

```py
class Solution:
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False
```




## BFS Iteration


```py
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False


```









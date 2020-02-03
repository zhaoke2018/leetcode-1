- [Intro](#intro)
- [Recursion By John](#recursion-by-john)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/symmetric-tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 
Note:
Bonus points if you could solve it both recursively and iteratively.



## Recursion By John


- 检测一棵树是否对称 https://leetcode.com/problems/symmetric-tree/
- [注意] 主树对称, 而不是子树对称! 所以必须考虑3代才行!
  - 两个点无法保证对称, 因为两点无法确定一个平面.

```py
def isSymmetric(self, root: TreeNode) -> bool:
    def helper(t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return t1.val == t2.val and helper(t1.left, t2.right) and helper(t1.right, t2.left) # 注意这里递归下去的参数!
    return helper(root, root) # 根结点入队两次
```
## Iteration By John

```py
# Iterative with queue
def isSymmetric(self, root: TreeNode) -> bool:
    stack = deque([root, root]) # 新建队列的方式
    while len(stack) > 0:
        t1, t2 = stack.popleft(), stack.popleft()
        if t1 == None and t2 == None: continue
        if t1 == None or t2 == None: return False
        if t1.val != t2.val: return False

        stack.append(t1.left) # 一定要注意顺序! 镜像
        stack.append(t2.right)
        stack.append(t1.right)
        stack.append(t2.left)
    return True
```


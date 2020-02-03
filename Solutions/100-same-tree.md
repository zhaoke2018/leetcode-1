- [Intro](#intro)
- [思路对比](#%e6%80%9d%e8%b7%af%e5%af%b9%e6%af%94)
- [Recursion By John](#recursion-by-john)
- [Iteration By John](#iteration-by-john)

## Intro

- https://leetcode.com/problems/same-tree

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

## 思路对比

- [思路] 递归判断两个树是否每层都相等.
- [代码技巧] 用一个易懂的变量来表示一段复杂的逻辑.

## Recursion By John

```py
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    trees_compare_finished = not p and not q # 两个树都不存在, 说明比完了
    trees_not_same = (not p or not q) or (p.val != q.val) # 一树不存在 or 两值不相等, 肯定不相等

    if trees_compare_finished:
        return True
    if trees_not_same: 
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```



## Iteration By John

```py
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    def check(p, q):
        trees_compare_finished = not p and not q # 两个树都不存在, 说明比完了
        trees_not_same = (not p or not q) or (p.val != q.val) # 一树不存在 or 两值不相等, 肯定不相等
        
        if trees_compare_finished: # Why 最后反正要返回 True, 为什么这里还要这一轮呢? 去掉又会报错
            return True
        if trees_not_same:
            return False
        return True
    
    deq = deque([(p, q),])
    while deq: # 树型递归好像都需要弄一个队列哦!
        p, q = deq.popleft()
        if not check(p, q):
            return False
        
        if p:
            deq.append((p.left, q.left)) # Why 居然不是镜面形式加入的.
            deq.append((p.right, q.right))
                
    return True
```
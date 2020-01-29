- [Intro](#intro)
- [Iteration by leetcode](#iteration-by-leetcode)
- [Recursion by leetcode](#recursion-by-leetcode)
- [recursion by me](#recursion-by-me)
- [Inorder](#inorder)

TODO
- 哪种方法比较好?




## Intro

- 验证一个 BST 是否合法 https://leetcode.com/problems/validate-binary-search-tree/


```
[10,5,15,null,null,6,20]
           10
        /     \
       5       15
     /   \    /  \
  null  null 6    20
```


https://leetcode.com/problems/validate-binary-search-tree/solution/
解法很多，但是可以归类一下。
思想上，分为 inorder 和。。。
实现上，iteration 和 recursion



## Iteration by leetcode

```py


```



## Recursion by leetcode

```py
class Solution:
    def isValidBST(self, root):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
```


## recursion by me


TODO
- 这个解答与下面的那个错误的根本区别是什么?
  - 错误解答中, 没有把界限代入到递归函数中

```py
# 递归的时候, 保证里面所有的元素都大于之前的元素
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root, min_=float('-inf'), max_=float('inf')):
            if not root:
                return True
            
            if root.val > max_ or root.val < min_: # 保证本代在限定范围内
                return False
            
            if not traverse(root.left, min_, root.val):
                return False
            if not traverse(root.right, root.val, max_):
                return False
            return True

        return traverse(root)
```


- 错误原因: 没有保证子节点的所有内容都小于 root.

```py
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_res = True
        right_res = True
        
        
        # 当前只保证两层内顺序正确, 实际上要保证所有的子节点都正确
        if root.left:
            left_res = root.left.val < root.val and self.isValidBST(root.left)
        if root.right:
            right_res = root.right.val > root.val and self.isValidBST(root.right)
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        return left_res and right_res
```



## Inorder


```py


```



















- [Intro](#intro)
- [思路对比](#%e6%80%9d%e8%b7%af%e5%af%b9%e6%af%94)
- [Compare_While_Traversal By Leetcode](#comparewhiletraversal-by-leetcode)
  - [Compare_While_Traversal By John](#comparewhiletraversal-by-john)

## Intro

- https://leetcode.com/problems/subtree-of-another-tree


Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:

Given tree s:

        3
        / \
      4   5
      / \
    1   2

Given tree t:

      4 
      / \
    1   2

Return true, because t has the same structure and node values with a subtree of s.


Example 2:

Given tree s:

        3
        / \
      4   5
      / \
    1   2
        /
      0

Given tree t:

      4
      / \
    1   2

Return false.


## 思路对比

- [Compare_While_Traversal] 一边遍历一边对比. 如果大树很大, 小树很小, 那这种方法就会比较高效.
- [Compare_After_Traversal] 两棵树遍历完之后, 直接对比遍历结果即可.
  - [WHY] 单独的一个 preorder 并不能确定一棵树!!!为什么不会报错???

      1
     / \
    2   3
preorder: [1,2,3]

        1
       /
      2
     /
    3
preorder: [1,2,3]




## Compare_While_Traversal By Leetcode


```py
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(s, t):
            if not s and not t: # 都不存在, 表示比完了. 成功的结果优先返回
                return True
            if not s or not t: # 经过上面的过滤, 那么此时肯定是一棵树不存在, 另一棵树存在的情况
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
        def traverse(s, t):
            return s and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))
        return traverse(s, t)
```





### Compare_While_Traversal By John

- 本解法仅留作纪念, 跟上面的思路一样, 但是写得很繁琐.

- [WHY] 比完一层就直接返回结果了
- [WHY] 不知道为什么, compare() 的返回值没有返回到 traverse() 里
  - 打印 root.val 的值, 就知道问题在哪了, 其实是 递归的traverse() 没有返回



```py
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # s is bigger
        
        # traverse big tree
        def traverse(root):
            if root:
                rrr = compare(root, t)
                # print('rrr', rrr, root.val)
                if rrr:
                    # print("2. 求求你 返回吧!!!!!!!!!!!!!!!")
                    return True
                else:
                    if traverse(root.left):
                        return True # 4
                    if traverse(root.right):
                        return True
            else:
                if not t:
                    return True
                else:
                    # print('会进入这里????', root, t)
                    return False
        
        # 左右子树都相等, 才能 return True
        def compare(a, b):
            if not a and not b: # 两者都比完了
                # print('1. 某树比完了 True')
                return True
            if (not a and b) or (a and not b) or (a.val != b.val):
                # print('会进入这里? 11')
                return False
            # print('0. 本次对比', a.val, b.val)
            # 如果两树都存在并且相等, 则继续比
            return compare(a.left, b.left) and compare(a.right, b.right)
        
        
        res = traverse(s)
        # print('3. 先检查以下结果', res)
        return res
```


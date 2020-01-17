- [Intro](#intro)
- [Traverse By John](#traverse-by-john)
- [Traverse By Leetcode](#traverse-by-leetcode)
- [Preorder By John](#preorder-by-john)




## Intro

- 

## Traverse By John



- 以下代码的问题
- 比完一层就直接返回结果了
- 不知道为什么, compare() 的返回值没有返回到 traverse() 里
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


## Traverse By Leetcode


```py
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
        def traverse(s, t):
            return s and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))
        return traverse(s, t)
```

## Preorder By John




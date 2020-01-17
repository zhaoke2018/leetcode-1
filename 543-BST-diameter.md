- [基本信息](#%e5%9f%ba%e6%9c%ac%e4%bf%a1%e6%81%af)
- [第一次尝试](#%e7%ac%ac%e4%b8%80%e6%ac%a1%e5%b0%9d%e8%af%95)
- [标准答案](#%e6%a0%87%e5%87%86%e7%ad%94%e6%a1%88)
- [参考标准答案后](#%e5%8f%82%e8%80%83%e6%a0%87%e5%87%86%e7%ad%94%e6%a1%88%e5%90%8e)



## 基本信息

- 计算二叉树的直径, 其实就是从一个节点到另一个节点的最长距离, 但是这个距离不是节点的数量, 而是节点之间的边的数量. https://leetcode.com/problems/diameter-of-binary-tree/
- [陷阱] 对于没有右子树的二叉树, 宽度可能不经过 root 节点.
  - 因此, 不能最后计算 宽度, 而是需要在递归过程中计算最大宽度.




```
tree1 = [1, 2, null, 3, 4, 5, null, null, 6, null, null, null, 7] # diameter 应该是6, 但是标准答案计算的是5
# 其实没有错, diameter 指的是 边的长度.
        1
       / 
      2
     / \
    3   4
   /     \
  5       6
           \
            7
```


## 第一次尝试

```py
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs_depth(root): # 计算深度的经典代码, 居然会报错
            if not root:
                return 0
            print(root.val)
            
            return max(dfs_depth(root.left), dfs_depth(root.right)) + 1
   
        return dfs_depth(root.left) + dfs_depth(root.right)
```







## 标准答案

```py
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1 # 本函数计算节点的深度(因为递归的时候没有算root, 所以最后+1)

        depth(root)
        return self.ans - 1
```


## 参考标准答案后

```py

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs_depth(root):
            if not root:
                return 0
            print(root.val)
            L = dfs_depth(root.left) 
            R = dfs_depth(root.right)
            # ans 每次更新, 获取所有节点的长度, 包括 root
            # 因为 最大长度 可能不在 根节点 出现, 因此需要在递归过程中计算
            self.ans = max(L+R+1, self.ans) # 去掉这句话, 整个函数就是计算树深度的
            return max(L, R) + 1
        
        if not root:
            return 0
        
        self.ans = 1 # 为什么初始化为1呢? 方便最后 -1
        dfs_depth(root)
        
        return self.ans - 1
```














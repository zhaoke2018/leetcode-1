- [Intro](#intro)

## Intro

- https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.
 
Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

 
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.




- https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/477048/JavaC%2B%2BPython-1-Line-Recursive-Solution

- 把 父系 信息都记录下来, 不就很清晰了吗!

```py
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
    
        def dfs(node: TreeNode, pa: int, gpa: int): # 注意: pa 和 gpa 都用 int
            if not node:
                return 0
            # 这句话涵盖 递归和返回的作用
            return dfs(node.left, node.val, pa) + dfs(node.right, node.val, pa) + (node.val if gpa % 2==0 else 0)
        
        return dfs(root, 1, 1)
```


- 将递归拆开写, 容易理解一点

```py
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            res += node.val # 需要一个全局变量
            dfs(node.left, node, pa)
            dfs(node.right, node, pa)
        dfs(root, 1, 1)

```


## 

```py
# John 实现的, 时间复杂度较高; 但没有使用额外的变量
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getgson(root):
            sumi = 0
            if root.left:
                if root.left.left:
                    sumi += root.left.left.val
                if root.left.right:
                    sumi += root.left.right.val
            if root.right:
                if root.right.left:
                    sumi += root.right.left.val
                if root.right.right:
                    sumi += root.right.right.val
            return sumi
        
        res = 0
        Q = collections.deque([root])
        while Q:
            q = Q.popleft()
            if q:
                if q.val % 2 == 0:
                    ss = getgson(q)
                    print('even', q.val, ss)
                    res += ss

                Q.append(q.left)
                Q.append(q.right)
        return res
```# DFS-Java
```Java
class Solution {
    int count = 0;
    public int sumEvenGrandparent(TreeNode root) {
        dfs(root, null, null);
        return count;
    }
    
    private void dfs(TreeNode cur, TreeNode pa, TreeNode gpa) {
        if (cur == null) return;
        if (gpa != null && gpa.val % 2 == 0) count+=cur.val;
        dfs(cur.left, cur, pa);
        dfs(cur.right, cur,pa);
    }
}
```

# BFS-Java
```Java
class Solution {
    public int sumEvenGrandparent(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int count = 0;
        while(!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node.val % 2 == 0 && node.left != null) {
                if (node.left.left != null) count+= node.left.left.val;
                if (node.left.right != null) count+= node.left.right.val;
                
            }
            if (node.val % 2 == 0 && node.right != null) {
                if (node.right.left != null) count+= node.right.left.val;
                if (node.right.right != null) count+= node.right.right.val;
            }
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        return count;
    }
}
```

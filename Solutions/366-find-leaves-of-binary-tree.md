- [Intro](#intro)
- [DFS](#dfs)

## Intro

- https://leetcode.com/problems/find-leaves-of-binary-tree


Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:
```
Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 ```

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:
```
          1
         / 
        2          
``` 

2. Now removing the leaf [2] would result in this tree:
```
          1          
``` 

3. Now removing the leaf [1] would result in the empty tree:
```
          []         
```

## DFS


```Java
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> ans = new ArrayList();
        if (root == null) return ans;
        List<Integer> cur;
        while (root != null) {
            cur = new ArrayList();
            root = dfs(root, cur);
            ans.add(cur);
        }
        return ans;
    }
    
    private TreeNode dfs(TreeNode root, List<Integer> cur) {
        if (root.left == null && root.right == null) {
            cur.add(root.val);
            return null;
        }
        if (root.left != null) root.left = dfs(root.left, cur);
        if (root.right != null) root.right = dfs(root.right, cur);
        return root;
    }
}
```

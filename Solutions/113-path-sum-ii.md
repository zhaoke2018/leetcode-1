- [Intro](#intro)

## Intro

- https://leetcode.com/problems/path-sum-ii

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]




# DFS-Java
```Java
class Solution {
    int sum;
    List<List<Integer>> res = new ArrayList();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        
        this.sum = sum;
        dfs(root, 0, new ArrayList<Integer>());
        return res;
    }
    private void dfs(TreeNode root, int cur, ArrayList<Integer> temp) {
        if (root == null) return;
        temp.add(root.val);
        if (root.left == null && root.right == null && cur +root.val == sum) {
            res.add(new ArrayList<Integer>(temp));
            
        }
        if (root.left != null) dfs(root.left, cur + root.val, temp);
        if (root.right != null) dfs(root.right, cur + root.val, temp);
        temp.remove(temp.size() - 1);
    }
}
```


## Topics

- `Tree`
- `Depth-first Search`



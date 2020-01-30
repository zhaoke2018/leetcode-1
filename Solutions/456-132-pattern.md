- [Intro](#intro)

## Intro

- https://leetcode.com/problems/132-pattern


Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such
that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

# DFS-Java
```Java
class Solution {
    int level = 0;
    int leftMost;
    public int findBottomLeftValue(TreeNode root) {
        if (root.left == null && root.right == null) return root.val;
        dfs(root, level);
        return leftMost;
    }
    
    private void dfs(TreeNode root, int curLevel) {
        if (curLevel > level) {
            level = curLevel;
            leftMost = root.val;
        }
        
        if (root.left != null) dfs(root.left, curLevel + 1);
        if (root.right != null) dfs(root.right, curLevel + 1);
    }
}
```
# BFS-Java
```Java
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        int leftMost = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()) {
            int size = q.size();
            leftMost = q.peek().val;
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
        }
        return leftMost;
    }
}
```

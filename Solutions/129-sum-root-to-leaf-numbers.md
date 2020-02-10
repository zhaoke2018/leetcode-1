- [Intro](#intro)

## Intro

- https://leetcode.com/problems/sum-root-to-leaf-numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.
Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


## Topics

- `Tree`
- `Depth-first Search`

## DFS
### 自己写的
```java
class Solution {
    int sum;
    public int sumNumbers(TreeNode root) {
        sum = 0;
        dfs(root, 0);
        return sum;
    }
    private void dfs(TreeNode root, int cur) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            cur = cur * 10 + root.val;
            sum += cur;
        }
        dfs(root.left, cur * 10 + root.val);
        dfs(root.right, cur * 10 + root.val);
    }
}
```
### 更简洁的
```java
class Solution {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }
    private int dfs(TreeNode root, int cur) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return cur * 10 + root.val;
        return dfs(root.left, cur * 10 + root.val) + dfs(root.right, cur * 10 + root.val);
    }
}
```


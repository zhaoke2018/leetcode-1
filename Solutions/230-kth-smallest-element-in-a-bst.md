- [Intro](#intro)
- [Topics](#topics)
- [Inorder - Recursion](#inorder---recursion)
- [Iteration - Hard](#iteration---hard)

## Intro

- https://leetcode.com/problems/kth-smallest-element-in-a-bst

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?




## Topics

- `Binary Search`
- `Tree`
- `Iteration - Hard`
- `Inorder - Recursion`


## Inorder - Recursion


- BST 的 inorder traversal 就是一个 sorted array, 所以本题考的就是 inorder traversal!

```py
def kthSmallest(self, root: TreeNode, k: int) -> int:
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    return inorder(root)[k-1]
```


## Iteration - Hard

- 本题也可以一边遍历一边找元素
- Faster than 99%
- 这里解法很多, 也可以看一下 https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python)%3A-Binary-Search-in-order-iterative-and-recursive

```py
class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while True:
            # enstack all root, and process left!
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```












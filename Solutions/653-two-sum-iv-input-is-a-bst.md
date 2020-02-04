- [Intro](#intro)

## Intro

- https://leetcode.com/problems/two-sum-iv-input-is-a-bst

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

 
Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

 

- https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ tree/easy
  - input一个binary search tree和一个val,若树中有两个元素加起来==val,则返回true,否则返回false.
  - [Hash] 跟最普通的 2 sum 一样, 区别在于, 遍历的是BST, 而不是一个数组.

```py
def findTarget(self, root: TreeNode, k: int) -> bool:
    cache = set()
    qu = [root] # 使用 queue 实现 BFS
    while qu: # 遍历所有数据
        cv = qu.pop()
        if k-cv.val in cache:
            return True
        else:
            cache.add(cv.val)
            
            if cv.left: qu.append(cv.left)
            if cv.right: qu.append(cv.right)
    return False
```




https://leetcode.com/submissions/detail/267496631/

- [思路] 借此机会回顾一下基础的 2 sum：我们可以先将所有元素都入set；也可以一次遍历，如果余数在set就直接返回！如果余数不在，就把原数入set。









- https://leetcode.com/problems/two-sum-iv-input-is-a-bst/ tree/easy
  - input一个binary search tree和一个val,若树中有两个元素加起来==val,则返回true,否则返回false.
  - [Hash] 跟最普通的 2 sum 一样, 区别在于, 遍历的是BST, 而不是一个数组.

```py
def findTarget(self, root: TreeNode, k: int) -> bool:
    cache = set()
    qu = [root] # 使用 queue 实现 BFS
    while qu: # 遍历所有数据
        cv = qu.pop()
        if k-cv.val in cache:
            return True
        else:
            cache.add(cv.val)
            
            if cv.left: qu.append(cv.left)
            if cv.right: qu.append(cv.right)
    return False
```





## Topics

- `Tree`



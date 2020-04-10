- [Intro](#intro)
- [Topics](#topics)
- [DFS](#dfs)
- [BFS](#bfs)
- [Other](#other)

## Intro

- https://leetcode.com/problems/populating-next-right-pointers-in-each-node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 
Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 
Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

 
Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000



## Topics

- `Tree`
- `Depth-first Search`


## DFS

- [小技巧] 搭好的桥(next), 可以立马就用上噢!
- [空间复杂度] O(1) 不需要用任何额外空间, 连管理递归的空间都不需要.

```py
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return

        if root.left and root.right:
            root.left.next = root.right # 树内相连
            if root.next:
                root.right.next = root.next.left # 树外相连
            else:
                root.next = None
                
        self.connect(root.left)
        self.connect(root.right)

        return root # 递归完, 返回!
```

## BFS

- BFS遍历, 然后同一层的往右指一下即可.
- 但是每次要取出两个节点才行, 这样有点不太方便.
- [报错!] Time Limit Exceeded
  - [WHY] 很奇怪, 下次再弄吧.


```py
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        Q = collections.deque([root])
        while Q:
            level = len(Q)
            for i in range(level-1):
                if not pre:
                    pre = Q.popleft()
                    if pre:
                        Q.append(pre.left)
                        Q.append(pre.right)
                cur = Q.popleft()
                if not cur: # 弹不出了, 那就到了最右了
                    pre.next = None
                    break
                else:
                    pre.next = cur
                    Q.append(cur.left)
                    Q.append(cur.right)
        return root
```

## Other

- 这个答案, 还有下面的回复都挺有参考价值的! https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space

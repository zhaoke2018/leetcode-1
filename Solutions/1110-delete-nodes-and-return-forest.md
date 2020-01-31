- [Intro](#intro)
- [Top-Down](#top-down)

## Intro

- https://leetcode.com/problems/delete-nodes-and-return-forest

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.
 
Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

 
Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.




## Top-Down

- [未解之谜]为什么第一个程序里面, 删除节点没有效果, 但是第二个程序就有效呢?


```py
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        Q = collections.deque([(root, False)])

        while Q:
            node, hasPa = Q.popleft()
            if node:
                if node.val in to_delete:
                    Q.append((node.left, False))
                    Q.append((node.right, False))
                    node = None # key
                else:
                    if not hasPa:
                        result.append(node)

                    Q.append((node.left, True))
                    Q.append((node.right, True))
        return result
```
Output: [[1,2,3,4,5,6,7],[6],[7]]
Expected: [[1,2,null,4],[6],[7]]


```py
# accepted
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = collections.deque([(root, False)])
        res = []
        
        while queue:
            node, hasParent = queue.popleft()
            # new Root found
            if not hasParent and node.val not in to_delete:
                res.append(node)
                
            hasParent = not node.val in to_delete

            if node.left: 
                queue.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None # key
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None
            
        return res
```









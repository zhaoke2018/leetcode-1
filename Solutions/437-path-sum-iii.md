- [Intro](#intro)

## Intro

- https://leetcode.com/problems/path-sum-iii

You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

- [Intro](#intro)
- [ACed Recursion by someone](#aced-recursion-by-someone)
- [Recursion minus By John](#recursion-minus-by-john)
- [Recursion Collect by John](#recursion-collect-by-john)




## Intro

- https://leetcode.com/problems/path-sum-iii/
- [陷阱] 路径有可能数字相同, 因此不能去重

[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
[[5, 4, 11, 2], [5, 8, 4, 5]]

          5
      /          \
     4            8
   /    \        /  \
  11   null    13    4
 / \            /    \
7  2           5      1


[1,-2,-3,1,3,-2,null,-1]

   1
 /  \
-2   -3
/\    /\
1 3  -2
/
-1


[1,-2,-3,5,3,-6,null,-7]
   1
 /  \
-2   -3
/\    /\
5 3  -6
/
-7


## Topics

- `Tree`


## ACed Recursion by someone

```py
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return 
        # dfs break down 
        self.test(node, target) # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        # test break down
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
```


## Recursion minus By John



- [Recursion思路] 每个节点都可能是起点, 每个节点也可能是终点!
- [错误原因] 叶子(3) 的每一个祖先, 都会导致(3) 开张一次. 因为每次验证的时候都会导致新开张.
  - [解决办法] 把验证和递归两个函数分开.
- 全是负数的没法通过, 有正有负的估计也没法



```py
class Solution:
    def pathSum(self, root: TreeNode, sumi: int) -> int:
        # store all path 
        def bt(node, stage):
            if not node:
                # TODO 无子节点已经处理过了, 怎么还会走这里呢?
                # print('这句应该只有[]才会用到 gabage path', stage) # 按理说, 只有遍历到叶子, 才会走这个逻辑
                return

            # TODO 为什么结尾的3会计算两次呢?
            if sum(stage)+node.val == sumi:
                stage.append(node.val)
                # print('结束2 - Found path at node!!!:', node.val, stage)
                res.append(stage)
                return
            
            if not node.left and not node.right:
                stage.append(node.val)
                print('结束1 - 没有子节点', stage) # 没错!
                return

            # 开张啦!
            bt(node.left, stage+[node.val])
            bt(node.right, stage+[node.val])
            
            # 给所有节点一个开张的机会
            bt(node.left, [])
            bt(node.right, [])

        res = []
        bt(root, [])
        print(res)
        return len(res)
```


## Recursion Collect by John

- 这段代码好像跟上面重复了... 暂时保留...


- 将所有情况都列出来.
- 如果 某叶子==和, 会计算两次
  - 如果把 garbage path 重复输出的问题解决了, 估计就好了

```py
class Solution:
    def pathSum(self, root: TreeNode, sumi: int) -> int:
        # store all path 
        def bt(node, stage):
            
            if not node:
                return
            print('looping node:', node.val)
            # print(stage)
            if sum(stage)+node.val == sumi:
                stage.append(node.val)
                print('Found path at node!!!:', node.val, stage)
                res.append(stage)
                return
              
            # 开张啦!
            bt(node.left, stage+[node.val])
            bt(node.right, stage+[node.val])
            
            # 给所有节点一个开张的机会
            bt(node.left, [])
            bt(node.right, [])

        res = []
        bt(root, [])
        print(res)
        return len(res)
```










                    


- [基本情况介绍](#%e5%9f%ba%e6%9c%ac%e6%83%85%e5%86%b5%e4%bb%8b%e7%bb%8d)
- [1. 提交失败](#1-%e6%8f%90%e4%ba%a4%e5%a4%b1%e8%b4%a5)
- [2. 本地验证代码](#2-%e6%9c%ac%e5%9c%b0%e9%aa%8c%e8%af%81%e4%bb%a3%e7%a0%81)
- [3. 发帖询问](#3-%e5%8f%91%e5%b8%96%e8%af%a2%e9%97%ae)
- [4. 暂时提交递归版](#4-%e6%9a%82%e6%97%b6%e6%8f%90%e4%ba%a4%e9%80%92%e5%bd%92%e7%89%88)
- [??xx](#xx)



## 基本情况介绍

- 给定一个二叉树, 判断其中的两个节点是否为 cousin 节点(父亲节点不一样, 但是深度一样) https://leetcode.com/problems/cousins-in-binary-tree/
- [BFS] 直接遍历整个树, 对于每个节点, 将其 父亲节点 和 深度信息 保存起来. 
- [优化] 找到两个节点就可以结束了, 没必要遍历整棵树.






## 1. 提交失败



## 2. 本地验证代码

TODO
- 无

```py
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        Q = collections.deque([root])
        depth = 0
        
        while Q:
            level_len = len(Q)
            depth += 1
            for i in range(level_len):
                q = Q.popleft()
                if q.left:
                    depthd[q.left.val] = depth
                    parentd[q.left.val] = q
                    Q.append(q.left)
                if q.right:
                    depthd[q.right.val] = depth
                    parentd[q.right.val] = q
                    Q.append(q.right)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        # for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        #     yield line.strip('\n')
        with open('input.txt', 'r') as f: # 改成从文件中读取输入
            for line in f.readlines():
                if not line.strip('\n'): # 加上这句话之后, 输入文件中可以加空行断开
                    continue
                print(line.strip('\n'))
                yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            line = next(lines)
            x = int(line)
            line = next(lines)
            y = int(line)
            print(root.val, x, y)
            ret = Solution().isCousins(root, x, y)

            out = ('out', ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
```


```txt
[1,2,3,null,4,null,5]
5
4

[1,2,3,4]
4
3

[1,2,3,null,4]
2
3
```



## 3. 发帖询问

TODO
- 等待别人解答


My code runs perfectly locally, but has this error when I submit 👇Any idea why?

> Runtime Error Message: Line 29: KeyError: 1
> Last executed input:
> [1,null,2,3,null,null,4,null,5]
> 1
> 3


```py
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        Q = collections.deque([root])
        depth = 0
        
        while Q:
            level_len = len(Q)
            depth += 1
            for i in range(level_len):
                q = Q.popleft()
                if q.left:
                    depthd[q.left.val] = depth
                    parentd[q.left.val] = q
                    Q.append(q.left)
                if q.right:
                    depthd[q.right.val] = depth
                    parentd[q.right.val] = q
                    Q.append(q.right)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]
```


## 4. 暂时提交递归版

TODO
- [如何实现提前结束的优化?]



- 本答案 faster than 99.90%

```py
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        def bfs(root, depth, father=None):
            if root:
                depthd[root.val] = depth
                parentd[root.val] = father
                if root.left:
                    bfs(root.left, depth+1, root)
                if root.right:
                    bfs(root.right, depth+1, root)
            
        bfs(root, 1)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]
```


## ??xx




```py
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depthd = dict()
        parentd = dict()
        
        Q = collections.deque([root])
        depth = 0
        
        while Q:
            level_len = len(Q)
            depth += 1
            for i in range(level_len):
                q = Q.popleft()
                if q.left:
                    depthd[q.left.val] = depth
                    parentd[q.left.val] = q
                    Q.append(q.left)
                if q.right:
                    depthd[q.right.val] = depth
                    parentd[q.right.val] = q
                    Q.append(q.right)
        return depthd[x] == depthd[y] and parentd[x] != parentd[y]

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        # for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        #     yield line.strip('\n')
        with open('input.txt', 'r') as f:
            for line in f.readlines():
                if not line.strip('\n'):
                    continue
                print(line.strip('\n'))
                yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            line = next(lines)
            x = int(line)
            line = next(lines)
            y = int(line)
            print(root.val, x, y)
            ret = Solution().isCousins(root, x, y)

            out = ('out', ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

```


- [基本情况](#%e5%9f%ba%e6%9c%ac%e6%83%85%e5%86%b5)
- [解题](#%e8%a7%a3%e9%a2%98)
- [Python JS 的 funtional 区别](#python-js-%e7%9a%84-funtional-%e5%8c%ba%e5%88%ab)


## 基本情况

- 返回所有从 root 出发, 到 leaf 的路径 https://leetcode.com/problems/binary-tree-paths/

https://leetcode.com/problems/binary-tree-paths/submissions/1

- 阶段性结束条件：无子节点。
- 其他结束条件：当前节点不存在。这样一来，可以直接把子节点拿去递归，再判断是否存在。
- 如何打印Python中的map对象？



## 解题

```py
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node: # 节点不存在, 当然要返回
                return

            if not node.left and not node.right: # 没有孩子, 阶段性结束
                path.append(node.val)
                res.append(path)
                return
            
            dfs(node.left, path+[node.val])
            dfs(node.right, path+[node.val])
        
        res = []
        dfs(root, [])

        return map(lambda hr : "->".join(map(str, hr)), res)
```


## Python JS 的 funtional 区别

- 如果 map 需要参数, 那么就用 lambda 来帮助!
- Python 的 map 格式:  `map(func, list)`


```py
res = [[1,2,5],[1,3]]
res = map(lambda hr : "->".join(map(str, hr)), res)
```


```js
// js 写起来很顺手
big_list = [
  [1, 2, 3],
  [4, 4, 4]
]

res = big_list.map((single_list) => {
    return single_list.join('->')
})

console.log(res)
```






```py
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for i in range(len(T))]
        print(T)
        for i in range(len(T)):
            nexti = i # 1
            step = 0 # 0
            print('---', nexti, step)
            while T[i] > T[nexti] and nexti < len(T)-1:
                print('nexti', nexti)
                nexti += 1
                step += 1
                
            res[i] = step
        
        return res
```   
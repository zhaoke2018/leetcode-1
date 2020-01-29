
- https://leetcode.com/problems/validate-stack-sequences/
  - 本题体现greedy的地方在于,每执行一个a操作,就检查是否满足b条件.
  - 每次push一个pushed数据的时候,就看看stack[-1] == popped(idx++)

```py
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        idx = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        print len(stack) == 0
        return len(stack) == 0

Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
```



- [Intro](#intro)

## Intro

- https://leetcode.com/problems/validate-stack-sequences

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1


Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

 
Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.



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



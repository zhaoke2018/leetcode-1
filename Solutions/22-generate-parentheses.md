- [Intro](#intro)
- [Topics](#topics)
- [Backtracking](#backtracking)

## Intro

- https://leetcode.com/problems/generate-parentheses


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


For example, given n = 3, a solution set is:


[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


## Topics

- `String`
- `Backtracking`

## Backtracking



```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N: # 每次都先处理 left
                backtrack(S+'(', left+1, right)
            if right < left: # 但是也会有一个分支处理右边. 注意, 这里都不能返回, 一旦返回就没法处理右边了
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
```
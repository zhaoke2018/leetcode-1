- [Intro](#intro)
- [Topics](#topics)
- [Stack](#stack)

## Intro

- https://leetcode.com/problems/valid-parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true



## Topics

- `String`
- `Stack`


## Stack

- pop from empty list 会报错! 听起来像是 `stack.pop()` 本身会报错呀! 那下面的代码为什么没事?
  - 因为 `left = stack.pop() if stack else '#'` 里面的 if 先执行, 所以避免了错误.


```py
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []

        for c in s:
            print(c in pair)
            if c not in pair:
                stack.append(c)
            else:
                left = stack.pop() if stack else '#' # Here
                if left != pair[c]:
                    return False
        return not stack
```
- [Intro](#intro)

## Intro

- https://leetcode.com/problems/letter-combinations-of-a-phone-number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.







## Topics

- `String`
- `Backtracking`


## Recursion

- 每个数字发射3个字母，所有的字母都发射完了就可以阶段性返回了。



```py
# accepted
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        quick = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def bim(ditz, stage):
            if not ditz:
                if stage: # 防止空串进来扰乱市场
                    res.append(stage)
                return
            for i in quick[int(ditz[0])]:
                bim(ditz[1:], stage+i)
        res = []
        bim(digits, "")
        return res
```

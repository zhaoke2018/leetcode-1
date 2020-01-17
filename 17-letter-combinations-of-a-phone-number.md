






- https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/

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

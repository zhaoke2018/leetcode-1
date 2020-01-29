
- 检验 s1 的变种是否存在 s2 中 https://leetcode.com/problems/permutation-in-string/


```py
def checkInclusion(self, s1: str, s2: str) -> bool:
    sm = Counter(s1)
    bg = Counter(s2[:len(s1)-1])

    for i in range(len(s1), len(s2)):

```



## Hash By John


分析:
- 将所有 substring 的组合都保存下来, 然后使用 find string 的方法来做

- 使用 hashing?
  - All substring has the same length? which means we can compare the first chars first then confirm later.





```py
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # find substring's index that is concatenation of words
        res = []
        return res

res = Solution().findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"])
print(res)
```


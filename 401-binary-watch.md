


- [陷阱] 用 num 构建所有的时间.
  - 应该把所有的时间都列出来, 然后看是否满足条件.


```py
from typing import List

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == num:
                    res.append(str(h) + ':' + str(m).zfill(2))
        return res

sol = Solution().readBinaryWatch(1)
print(sol)
```
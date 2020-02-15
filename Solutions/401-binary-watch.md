- [Intro](#intro)
- [Topics](#topics)
- [Backtracking](#backtracking)

## Intro

- https://leetcode.com/problems/binary-watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
Example:
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".




## Topics

- `Backtracking`
- `Bit Manipulation`


## Backtracking

- [陷阱] 用 num 构建所有的时间.
  - 应该把所有的时间都列出来, 然后看是否满足条件.

- [] python知识点
1. count() 参数必须是字符串.
2. bin() 返回的格式是 '0b11' 其实就是字符串'11', 只是多一个二进制标记而已.


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
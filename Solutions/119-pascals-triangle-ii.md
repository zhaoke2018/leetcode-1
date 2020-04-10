- [Intro](#intro)
- [Topics](#topics)
- [Array](#array)

## Intro

- https://leetcode.com/problems/pascals-triangle-ii

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:

Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?


## Topics

- `Array`



## Array

- 太简单了, 唯一值得提的就是本题可以将 edge case 融入主流程.

```py
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        lastRow = [1]
        for row in range(rowIndex):
            thisRow = [1]
            for idx in range(row):
                if idx+1 < len(lastRow):
                    thisRow.append(lastRow[idx] + lastRow[idx+1])
            thisRow.append(1)
            lastRow = thisRow
        return lastRow
```
- [Intro](#intro)
- [Topics](#topics)
- [Array](#array)

## Intro

- https://leetcode.com/problems/pascals-triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]



## Topics

- `Array`


## Array

经验总结
1. Python 可以使用负下标的, lastRow[-1] 不会报错, 因此不能通过这样判断元素是否存在.
2. 正下标也不能用, 因为会在 if 判断的时候直接报错.
3. 最保险的方式还是使用数组长度判断.


```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        if numRows < 1:
            return []
        
        for row in range(1, numRows):
            thisRow = [1] # 开头的 1 不需要计算, 直接写上
            for idx in range(row):

                lastRow = res[row-1]

                # 取数组下标如何能够简单一点呢?
                if idx + 1 < len(lastRow): # 不能直接取下标, 不然会报错
                    thisRow.append(lastRow[idx] + lastRow[idx+1])

            thisRow.append(1) # 结尾的 1 也不需要计算, 直接写上
            res.append(thisRow)

        return res
```
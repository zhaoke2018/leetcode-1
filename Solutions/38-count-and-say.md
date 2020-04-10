- [Intro](#intro)
- [Topics](#topics)
- [Regular Expression](#regular-expression)
- [Intuitive](#intuitive)

## Intro

- https://leetcode.com/problems/count-and-say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.
Note: Each term of the sequence of integers will be represented as a string.
 
Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".



## Topics

- `String`




## Regular Expression

- [感想] 很久之前被问过这个问题, 当时很快就解出来, 而现在居然要花这么久时间.
- [WHY] 这个正则还是不太懂



```js
const countAndSay = n => {
  let next = '1'
  for (let i=2; i<=n; i++) {
    base = next
    next = compressStr(base)
  }
  return next
};

const compressStr = ss => {
  // 这个 \1* 的正则匹配, 好像是重复前一个数字的?
  return ss.match(/(\d)\1*/g).map(substr => {
    return substr.length + substr[0]
  }).join('')
}
```

- 这里有俩正则的, 区别是啥 https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions

## Intuitive

- 找重复字母的部分, 用 for 循环, 更加清晰一点.

```js
const countAndSay = n => {
  let next = '1'
  for (let i=2; i<=n; i++) {
    base = next
    next = compressStr(base)
  }
  return next
};

const compressStr = ss => {
  let compressedStr = ''
  let count = 1
  let i = 0
  for (i=1; i<ss.length; i++) {
    if (ss[i] == ss[i-1]) {
      count ++;
    } else {
      compressedStr += count + ss[i-1]
      count = 1
    }
  }
  compressedStr += count + ss[i-1]
  return compressedStr
}
```






- 以下代码有问题

```py
class Solution:
    def countAndSay(self, n: int) -> str:
        base = '1'
        
        for i in range(1, n+1):
            newb = ''
            # 统计连续的数字
            s = 0 # index of base

            while s+1 < len(base):
                count = 0
                reachEnd = s+2 == len(base)
                keepCounting = base[s+1] == base[s]
                while reachEnd or keepCounting:
                    s += 1
                    count += 1
            
                newb += str(count) + base[s]
            
            base = newb

        return newb
```
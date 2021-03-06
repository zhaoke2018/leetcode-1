- [Intro](#intro)

## Intro

- https://leetcode.com/problems/implement-strstr

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


- https://leetcode.com/problems/implement-strstr/
  - 自己想的,将不会的地方用注释写出来,真的让思路清晰很多.小学的方法很好用耶!Don't let unknown things stop you.
  - 本问题主体思路基本上是brute force,循环一遍就可以找到了.只有一些细节实现上有区别.
  - leetcode 对本题要求不高, 所以 brute force 就搞定

```py
def strStr(haystack, needle):
    longg, shortt = len(haystack), len(needle)
    for i in range(longg - shortt + 1): # 这里为什么要+1, 没有想清楚 -> 也许只能通过举例来确定吧, 当两者相等时, 还是需要遍历一次
        if haystack[i: i+shortt] == needle:
            return i
    return -1
```

## Topics

- `Two Pointers`
- `String`



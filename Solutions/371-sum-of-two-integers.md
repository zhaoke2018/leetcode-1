- [Intro](#intro)
- [Topics](#topics)
- [Bit](#bit)

## Intro

- https://leetcode.com/problems/sum-of-two-integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3


Example 2:

Input: a = -2, b = 3
Output: 1





## Topics

- `Bit Manipulation`




## Bit

- 还是不懂

```js
var getSum = function(a, b) {
  return b==0 ? a : getSum(a^b, (a&b)<<1)  
};
```
- [Intro](#intro)

## Intro

- https://leetcode.com/problems/counting-bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.



## xx

- 找1大赛。0~n转换成二进制的话,每个数里面有多少个1? https://leetcode.com/problems/counting-bits/
  - `hint` You should make use of what you have produced already.
  - `hint` Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
  - `hint` Or does the odd/even status of the number help you in calculating the number of 1s?

```csharp
vector<int> countBits(int num) {
    vector<int> f(num+1);
    for (int i=1; i<=num; i++) 
      // 难道(i&1)就是快速变成binary的神器吗?
      f[i] = f[i >> 1] + (i & 1);
    return f;
}
```

- 思路2: 掌握一个规律(公式),本题就很简单了. `dp[i] = dp[i&(i-1)] + 1`
- 来源: https://leetcode.com/problems/counting-bits/discuss/79527/Four-lines-C++-time-O(n)-space-O(n)
  - https://leetcode.com/problems/counting-bits/discuss/119131/C++-Easy-to-Understand-Solution
  - 其实,出现在dp类别下,就应该去找dp[i]与dp[i-1]之间的关系.
```csharp
vector<int> countBits(int num) {
    vector<int> ret(num+1, 0);
    for (int i = 1; i <= num; ++i)
      ret[i] = ret[i&(i-1)] + 1;
    return ret;
}
```

- [Intro](#intro)

## Intro

- https://leetcode.com/problems/ones-and-zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.
Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.
Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

 
Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

 
Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

 




- https://leetcode.com/problems/ones-and-zeroes/
  - 给m个0和n个1,以及一些字符串,求最多可以用这些01组成多少个字符串.


- 给你m个0,n个1,还有一个字符串数组.看你能拼出多少个array里面的字符串,返回总数.(这些0和1都只能用一次) https://leetcode.com/problems/ones-and-zeroes/
- 本题分析和解法见背包问题

```csharp
// 传参是不是都用指针比较好?
int findMaxForm(vector<string>& strs, int m, int n) {
    int sum = 0;
    return sum;
}
```


```py


```
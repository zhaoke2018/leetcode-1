
- https://leetcode.com/problems/palindrome-partitioning-ii/
  - 将字符串切割成回文子串,问最小切割次数是?
  - https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/
  - 感觉跟rod cutting 有点像?

```py
# st[i,j]表示区间(i,j)的回文最小切割次数
st[i][j] = st[i][mid] + st[mid][j]

# hw[i][j]: 区间是否为回文
hw[i][j] = hw[i+1][j-1] and hw[i] == hw[j]
```

 
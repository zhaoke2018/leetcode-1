- [Intro](#intro)

## Intro

- https://leetcode.com/problems/decode-ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

- 将一串数字解码为字母，1~26分别对应A~Z，求有多少种解码方式 https://leetcode.com/problems/decode-ways/
  - 主干思想解析: 大部分数字只有一种解法,那么数字变长也不会让解法变多 dp[i]=dp[i-1]; 少部分数字有两种解法 dp[i]+=dp[i-2]
  - edge case 是本题的难点, 因为超多!
    - 提前返回.
      - 0开头的不能被解码.比如0/01
      - 空字符串不能被解码
    - 第二次仅处理 10/20 这两个整十.(第一次遇整十就清零,第二次仅添加)
      - 301/403 超过20的整十不能被解码.
      - 1001 连续两个0不能被解码.
      - 110只有一种解码方式,而不是两种. **这个处理真的很巧妙!可以通过清零,抵消掉之前的**


```py
def numDecodings(s: str) -> int:
    if s[0] == '0' or s == '': # edge case: 以0开头的不能被解码 '0' or '01'
        return 0

    decodeWays = [1 for i in range(len(s)+1)] # 将 s[i-1] 和 s[i-2] 的处理结果存放在 dp[i]中, 因此必须要加长一位才能存下所有s

    for i in range(2, len(decodeWays)):
        twodigits = int(s[i-2: i]) # slice是取前不取后的!
        decodeWays[i] = decodeWays[i-1] if twodigits%10!=0 else 0 # 个位为0? 一律清空

        if twodigits >= 10 and twodigits <= 26:
            decodeWays[i] += decodeWays[i-2]
    return decodeWays[-1]
```

- ref
  - http://www.cnblogs.com/grandyang/p/4313384.html
  - http://bangbingsyb.blogspot.com/2014/11/leetcode-decode-ways.html



## Python


```py
def numDecodings(s):
    s_len = len(s)

    if s_len == 0 or s[0] == '0':
        return 0

    dp = [1 for i in xrange(s_len + 1)]
    
    for i in xrange(1, len(dp)):
        h, l = int(s[i-2]), int(s[i-1]) # 为什么s和dp需要错开一个位置
        dp[i] = dp[i-1] if l != 0 else 0 # 并不是重置机制,xxx0拆成xxx+0的时候,因为0无法解码,那整体的解码就是为0

        num2 = h * 10 + l
        if i > 1 and num2 >= 10 and num2 <= 26: # 如果两位数有解码方式
            dp[i] += dp[i-2]
    return dp[-1]


def decodeWays(s):
    dp = [1 for i in xrange(len(s) + 1)]
    for i in xrange(1, len(dp)):
        pass


print numDecodings('12121') # 8

# 有了重制机制,这些带0的都不用愁了
print numDecodings('110') # 1
print numDecodings('100') # 0
print numDecodings('101') # 1
```


## CPP by 


```csharp
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || (s.size() > 1 && s[0] == '0')) return 0;
        vector<int> dp(s.size() + 1, 0); // dp = [0, 0, 0, 0, 0]
        dp[0] = 1; // dp = [1, 0, 0, 0, 0]
        for (int i = 1; i < dp.size(); ++i) {
            cout << "current i: " << i;
            cout << " current s[i-2]: " << s[i-2] << endl;
            dp[i] = (s[i - 1] == '0') ? 0 : dp[i - 1]; // 这个重制机制也太巧妙了!!!
            // 这个if把10和20都包含了.
            if (i > 1 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
                dp[i] += dp[i - 2];
                cout << "12 accu - dp[" << i << "]:" << dp[i] << endl;
            }
        }
        return dp.back();
    }
};

/*
when i=4
s[3] = 0

*/

int main() {
    cout << Solution().numDecodings("3120");
    return 0;
}
```
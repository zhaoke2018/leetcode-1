



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
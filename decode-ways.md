
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
- [Basic](#basic)
- [Optimize](#optimize)






## Basic


- TODO 如果s与dp一一对应会如何?
- 使用 dp[i] = d[i-1] + dp[i-2] 的方式,毕竟这是dp题,这样表现出来的关系更明显
- 教训: 一定要注意代码的覆盖面,很多bug都是因为某些条件根本没考虑到.解决办法就是if的条件拆开写.压缩会失真!
- 中心思想化简: 针对s[i-1],往前看一位s[i-2],如果他们俩综合起来有两种解码方式,那么dp[i]=dp[i-1]+dp[i-2],如果只有一种解码方式,那么dp[i]=dp[i-1].
- 提醒点: 对于s[i]位的结果,其实是存在dp[i+1]的,这就是为什么dp要长一位.
- 难处: 写好if,将所有情况考虑到位
- 难点: 计算的时候,如果dp[i-1]和dp[i-2]都计算,那么就是加,如果只算一位,就是乘



```py
def decodeWaysII(s):
    M = 10**9 + 7

    if len(s) == 0 or s[0] == '0':
        return 0

    # step-1 初始化dp数组
    dp = [1 for i in xrange(len(s) + 1)] # dp[0] 一定要初始化为1,其余的随便,反正会被覆盖的
    if s[0] == '*':
        dp[1] = 9

    # step-2 迭代计算dp数组
    for i in xrange(2, len(dp)):
        # 先算最后一位
        if s[i-1] == '*':
            if s[i-2] == '*': # **
                dp[i] = dp[i-1] * 9 + dp[i-2] * 15 # 如果最后两位一起解码,则有[11,19],[21,26]一共15种
            elif s[i-2] == '0': # 0*
                dp[i] = dp[i-1] * 9
            elif s[i-2] == '1': # 1* = 9
                dp[i] = dp[i-1] * 9 + dp[i-2] * 9
            elif s[i-2] == '2': # 2* = 6
                dp[i] = dp[i-1] * 9 + dp[i-2] * 6
            else:
                dp[i] = dp[i-1] * 9
        elif s[i-1] == '0':
            if s[i-2] in ['1','2']:
                dp[i] = dp[i-2]
            elif s[i-2] == '*':
                dp[i] = dp[i-2] * 2
            else:
                return 0
        else: # 以1-9数字结尾
            if s[i-1] in ['1','2','3','4','5','6']:
                if s[i-2] == '*':
                    dp[i] = dp[i-1] + dp[i-2] * 2
                if s[i-2] in ['1', '2']:
                    dp[i] = dp[i-1] + dp[i-2]
                if s[i-2] in ['0','3','4','5','6','7','8','9']:
                    dp[i] = dp[i-1]
            if s[i-1] in ['7','8','9']:
                if s[i-2] in ['*','1']:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        dp[i] = dp[i] % M
    return dp[-1]






# print decodeWaysII('*') # 9
# print decodeWaysII('1*') # 18

# print decodeWaysII('**') # 96 = 9*9+15
# print decodeWaysII('1**') # 177
# print decodeWaysII('1*1*0') # 404
# print decodeWaysII('1*1*1') # 382
# print decodeWaysII('2*2*2') # 277
# print decodeWaysII('***') # 999


# elif 没有写对
# print decodeWaysII('10') # 1
# print decodeWaysII('10*') # 9
# print decodeWaysII('10*1') # 11


# if a and b 这种还是分两个if写比较好,不然很容易覆盖不全
# print decodeWaysII('1*') # 18
# print decodeWaysII('1*7') # 18+1 dp[3]=dp[1]+dp[2]=1+18
# print decodeWaysII('1*72') # 19
# print decodeWaysII('1*72*') # 19*9 + 19*6 = 285
# print decodeWaysII("16") # 2
# print decodeWaysII("162") # 2
# print decodeWaysII("1620") # 2
# print decodeWaysII("16205") # 2
```



## Optimize


```py


def decodeWaysII_optimize(s):
    e0, e1, e2 = 1, 0, 0
    # f0, f1, f2 # 这是用来计算临时结果的
    M = 10**9 + 7
    for c in s:
        if c == '*':
            f0 = 9 * e0 + 9 * e1 + 6 * e2
            f1 = e0
            f2 = e0
        else:
            f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
            f1 = (c == '1') * e0
            f2 = (c == '2') * e0
        e0 = f0 % M
        e1 = f1
        e2 = f2
    return e0
```
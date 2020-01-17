- [基本信息](#%e5%9f%ba%e6%9c%ac%e4%bf%a1%e6%81%af)
- [Backtracking by me](#backtracking-by-me)



## 基本信息

- https://leetcode.com/problems/word-break-ii/

- [Backtracking] 截取前i个元素, 然后看是否在 dict 里, 如果找到了, 就继续递归, 如果i=full length 的时候都没找到, 那就 return False.
- [DP] 这个暂时还没思路



## Backtracking by me



```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def bt(ress, stage): # ress 表示剩余的字符串
            # print("刚开始", ress, stage)
            if not ress: # 当发射器空了之后, 就阶段性结束
                res.append(stage)

            for i in range(len(ress)+1): # 为了 ress[:i] 能取到所有值
                if ress[:i] in wordDict:
                    # print(ress[:i], stage)
                    bt(ress[i:], stage+[ress[:i]])
        
        if not s:
            return
        res = []
        bt(s, [])
        return map(lambda li: ' '.join(li), res)

# 执行这个例子时, Time Limit Exceeded
sol = Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
```

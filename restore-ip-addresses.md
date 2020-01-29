
- 给定一串字符串, 返回所有可能的IP地址. https://leetcode.com/problems/restore-ip-addresses/
  - John思路: 最开始统计, 只有4-12个数字才能进行计算. 一开始每段都一个数, 看看数字是否能够分配完.
  - 思路: 其实就是看这个字符串有多少种合法的切分方式. 把切分方式全都列出来就行了.
  - 
  - 考点: Backtracking
  - 补充知识点: IP地址每段都是[0, 255]
  - 升华: 一是只要遇到`字符串的子序列`或`配准问题`首先考虑动态规划DP; 二是只要遇到需要`求出所有可能情况`首先考虑用递归.
  - 面试频率: 面试出现很少. 本题思想不是很普适.


```py
def restoreIpAddresses(self, s: str) -> List[str]:
    def valid_IP_part(part):
        return part>=0  and part<=255
    slen = len(s)
    if slen>12 or slen<4:
        return None
    
```



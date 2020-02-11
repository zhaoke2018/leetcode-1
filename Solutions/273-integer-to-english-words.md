- [Intro](#intro)
- [Topics](#topics)
- [Translate](#translate)

## Intro

- https://leetcode.com/problems/integer-to-english-words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"







## Topics

- `Math`
- `String - Translate`


## Translate

- [亮点] 使用字符串 split 表示数组
- [陷阱] 边界情况要小心, 比如以0结尾 / 数字0.


```py
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = "0 Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def tran(num):
            # 每三位翻译一次
            if num == 0:
                return [] # 不能直接返回 ['Zero'], 因为 1000 最后不能有东西, 所以最后处理是最好的.
            if num < 20:
                return [to19[num]]
            if num < 100:
                return [tens[num//10]] + tran(num%10)
            if num < 1000:
                return tran(num//100) + ['Hundred'] + tran(num%100)
            
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1): # 表示, 从 1 开始算下标
                if num < 1000**(p+1):
                    return tran(num//1000**p) + [w] + tran(num%1000**p)
        
        res = tran(num)
        return ' '.join(res) or 'Zero'
```


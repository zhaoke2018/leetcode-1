
- Int数字转换为罗马数字.`1<n<3999`. https://leetcode.com/problems/integer-to-roman/ Medium
  - 10以内,IV
  - 100以内,XL
  - 1000以内,CD
  - 10000以内,M
  - `solution` 从低位到高位依次取余(remainder),然后用字典翻译

```py
def intToRoman(num):
    while num > 10:
        rem = num % 10
        num = num / 10
```
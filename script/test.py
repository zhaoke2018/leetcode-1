from typing import List
import collections 

class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        zipo = zip(numerals, values)
        print(list(zipo))
        # [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), 
        # ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        res = ""
        for n, v in zip(numerals, values):
            # print('---', n, v)
            res += (num // v) * n
            num %= v 
        return res


sol = Solution().intToRoman(99)
print(sol)


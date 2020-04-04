from typing import List
# import collections
# from functools import reduce

# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         # 这个好像是一个循环构造器, Trie 是一个 dict, dict 里面的默认值是 Trie
#         Trie = lambda: collections.defaultdict(Trie) # 这里为什么要用 lambda
#         print('Trie', Trie)
#         trie = Trie()
#         END = True
#         print('dict.__getitem__', dict.__getitem__)

#         for i, word in enumerate(words):
#             reduce(dict.__getitem__, word, trie)[END] = i

#         stack = list(trie.values())
#         ans = ""
#         while stack:
#             cur = stack.pop()
#             if END in cur:
#                 word = words[cur[END]]
#                 if len(word) > len(ans) or len(word) == len(ans) and word < ans:
#                     ans = word
#                 stack.extend([cur[letter] for letter in cur if letter != END])

#         return ans


# sol = Solution().longestWord(["w","wo","wor","worl", "world"])
# print(sol)

# # https://kite.com/python/answers/how-to-create-a-trie-in-python



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        if numRows < 1:
            return []
        
        for row in range(1, numRows):
            thisRow = [1]
            for idx in range(row): # don't calculate the first row
                # TODO calculate this row numbers
                lastRow = res[row-1]
                # if row == 1: # 计算第二行
                #     print('last row', lastRow)
                #     print('second row', lastRow[idx], lastRow[idx+1]) # python 里, 数组的负下标不会越界, 正下标才会越界!

                # 取数组下标如何能够简单一点呢?
                if idx + 1 < len(lastRow): # 不能直接取下标, 不然会报错
                # if lastRow[idx] and lastRow[idx+1]:
                    thisRow.append(lastRow[idx] + lastRow[idx+1])
            
            thisRow.append(1)
            res.append(thisRow)
        
        return res

sol = Solution().generate(5)
print(sol)

'''
[
[1], row=0 不计算
[1,1], row=1 不计算
[1,2,1], row=2 
[1,3,3,1], row=3
[1,4,6,4,1] row=4
]
'''
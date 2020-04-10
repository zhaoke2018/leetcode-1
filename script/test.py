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

import collections
import heapq

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def qualify(count, ss):
            patcount = collections.Counter(ss)
            for key in count.keys():
                if patcount[key] < count[key]:
                    return False
            return True

        l, r = 0, 0
        minwin = s
        count = collections.Counter(t)

        # 扩张到count全部满足为止, 然后收缩到刚好不满足为止
        while r<len(s): # 这个条件有点不妥
            while not qualify(count, s[l:r]):
                r += 1
            while qualify(count, s[l:r]):
                l += 1
            if len(minwin) > r-l:
                minwin = s[l-1:r]
        return minwin


sol = Solution().minWindow("ADOBECODEBANC", "ABC")

print(sol)
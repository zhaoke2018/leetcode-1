







- 从大串s上找到所有p的anagram的下标 https://leetcode.com/problems/find-all-anagrams-in-a-string/
  - anagram: 字符串的同分异构体,比如acb/bca/cbc
  - `Hash` 将p的映射到一个hash_p上,然后遍历s的时候,将window的数据映射到hash_window上,检验两个hash是否相等.
    - `优化` 使用一个窗口,这样的话,每个 s_substring 都只需要更新两个元素就行了.


```py
def findAnagrams(self, s: str, p: str) -> List[int]:
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p)-1])

    for i in range(len(p)-1,len(s)):
        sCounter[s[i]] += 1   # include a new char in the window
        if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
            res.append(i-len(p)+1)   # append the starting index
        sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
        if sCounter[s[i-len(p)+1]] == 0:
            del sCounter[s[i-len(p)+1]]   # remove the count if it is 0 这样可以防止比较
    return res
```







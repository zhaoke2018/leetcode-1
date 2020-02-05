- [Intro](#intro)
- [Topics](#topics)
- [Return one sort way](#return-one-sort-way)
- [待整理](#%e5%be%85%e6%95%b4%e7%90%86)

## Intro

- https://leetcode.com/problems/pancake-sorting

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.
 
Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 


Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

 

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]



## Topics

- `Array`
- `Sort`



## Return one sort way

- 返回一种翻转排序的方式即可 https://leetcode.com/problems/pancake-sorting/

```py
# 主要思想
for i in reversed(range(len(arr))):
    max_index = find_max(arr, i+1)
    flip(arr, max_index+1)
    flip(arr, i+1)

# 思想归思想,本题只需要求出 flip 序列就行,不用真的排序
def pancakeSort(A):
    ans = []

    N = len(A)
    B = sorted(range(1, N+1), key = lambda i: -A[i-1]) # key 表示 sort by -A[i-1], 但是这里的i是什么意思?
    for i in B:
        for f in ans:
            if i <= f:
                i = f+1 - i
        ans.extend([i, N])
        N -= 1

    return ans
```



## 待整理


```py

# flip first k elements in arr
def flip(arr, k):
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    return arr

# print(flip([1,3,5,7,9], 3))

# Find index of biggest number in first k elements
def findIndexOfMaxnum(arr, k):
    if len(arr) == 0:
        return
    bar = arr[0]
    idx = 0
    for i in range(k):
        if arr[i] > bar:
            bar = arr[i]
            idx = i
    return idx
      
# print(findIndexOfMaxnum([1,3,8,5,6], 4))


def pancake_sort(arr):
    for i in reversed(range(len(arr))):
        indexOfMaxNum = findIndexOfMaxnum(arr, i+1) # first biggest in first k
        if indexOfMaxNum != i:
            flip(arr, indexOfMaxNum + 1) # to make biggest number at beginning
            flip(arr, i + 1) # to make beginning number to the end
        
    return arr

print(pancake_sort([1, 5, 4, 3, 2]))
```


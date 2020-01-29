



## 知识总结



```py
def guess(guess, range=0, key=0):
    return 1

def guessNumber(n): # n is range
    low, high = 0, n
    while low != high:
        mid = low + (high - low) / 2
        if (high-low) % 2 != 0: # 由于整除的时候会丢掉一部分精度,因此需要一个跳位机制.主要是为了处理1 1的情况.
          mid += 1
        result = guess(mid)
        # print mid
        if result == 0:
            return mid
        elif result == 1:
            low = mid
        else:
            high = mid
       
# 与其说本地是dynamic programming,倒不如说是binary search
# 无法写迭代的时候,就递归呗
# python2需要引用future division才能精确除,但是python3默认精确除了.

def getMoneyAmount(n):
    low, high = 0, n
    fine = 0
    while low != high:
        mid = low + (high - low) / 2
        if (high-low) % 2 != 0: # 由于整除的时候会丢掉一部分精度,因此需要一个跳位机制.主要是为了处理1 1的情况.
          mid += 1
        result = guess(mid)
        # print mid
        if result == 0:
            return mid
        elif result == 1:
            low = mid
        else:
            high = mid


# 由于每次猜错都要被罚款,因此猜的次数要少,那还是二分法次数最少了.
```
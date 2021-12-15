# 231. Power of Two
'''
    TOPIC: Math BIT
    THINK:check if n is power of two, n can be positive, 0, negative
    T/S:Brute force TLE O(n); bit:O(1)
    HOW:
    1     2       4         8         16 　　....

    1    10    100    1000    10000　....
    see pattern: if n is power of two, mean most siginificant is 1, others are 0s, so 
    this question is asking count number of 1.
'''
def isPowerOfTwo(n):
        count = 0
        while n > 0:
            count += (n&1)
            n >>= 1
        return count == 1
print(isPowerOfTwo(3))
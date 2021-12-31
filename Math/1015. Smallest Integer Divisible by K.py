'''
    TOPIC:find smallest n which only contains digit 1, can be divisible by k,count len of n
    STEP:MATH:pighole algorithm/抽屉原理
    原理1： 把多于n个的物体放到n个抽屉里，则至少有一个抽屉里的东西不少于两件。
    原理2：把多于mn(m乘n)+1（n不为0）个的物体放到n个抽屉里，则至少有一个抽屉里有不少于（m+1）的物体。
    1.remain must [0,k-1], so loop created, more k will stop
    2.remain=remain*10+1,see if %k, yes return;otherwise, remain%=k
    3.reversely THINK 111/3=3 % 2, 21 % 0
'''
def smallestRepunitDivByK(k):
        if k == 2 or k == 5: return -1
        remain = 0
        for i in range(1,k+1):
            remain = remain*10 + 1
            print("Test; ", remain)
            if remain % k == 0:
                return i
            remain %= k
            
        return -1
print(smallestRepunitDivByK(3))
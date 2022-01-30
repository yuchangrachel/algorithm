from operator import sub


def maxScoreIndices(nums):
        totalOnes = 0
        for i in nums:
            if i == 1:
                totalOnes += 1
    
    
        res = [0] * (len(nums)+1)
        zero = 0
        ones = 0
        for i in range(len(nums)+1):
            if i == 0:
                res[i] = totalOnes
                continue
            elif nums[i-1] == 0:
                zero += 1
            else:
                ones += 1
            
            res[i] = zero + (totalOnes - ones)

        maxi = max(res)
        result = []
        for i in range(len(res)):
            if res[i] == maxi:
                result.append(i)
        
        return result

# print(maxScoreIndices(([0,0,1,0])))

# Find Substring With Given Hash Value
# overtime
def subStrHash(s, power, modulo, k, hashValue):
    if k == len(s):
        return s

    for i in range(len(s)-k):
        temp = 0
        d = 0
        sub = ""
        for j in range(i,i+k):
            sub += s[j]
            temp += (ord(s[j]) - ord("a") + 1) * (power ** d)
            d += 1
        
        if temp > hashValue:
            temp = temp % modulo
            if i == 1:
                print(temp)

        if temp == hashValue:
            return sub
    
    return ""

'''
    Intuition
Good time to learn rolling hash.
what's hash?
The definition hash(s, p, m) in the description is the hash of string s based on p.

what's rolling hash?
The hash of substring is a sliding window.
So the basis of rolling hash is sliding window.

Explanation
Calculate the rolling hash backward.
In this process, we slide a window of size k from the end to the begin.

Firstly calculate the substring hash of the last k characters,
then we add one previous backward and drop the last characters.

Why traverse from end instead of front?
Because cur is reminder by mod m,
cur = cur * p works easier.
cur = cur / p doesn'r work easily.


Complexity
Time O(n)
Space O(1)
    '''
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord("a") + 1
        
        pk = pow(power,k, modulo)
        cur = 0
        
        for i in range(len(s)-1, -1, -1):
            cur = (cur * power + val(s[i])) % modulo
            if i + k < len(s):
                cur = (cur - val(s[i+k]) * pk) % modulo
            if cur == hashValue:
                res = i
        return s[res:res+k]
        

# print(subStrHash("xmmhdakfursinye",96,45,15,21))  #"xmmhdakfursinye"
print(subStrHash("leetcode",7, 20,2, 0))        
    
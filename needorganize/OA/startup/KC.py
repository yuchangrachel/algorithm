#Q1: LEEtcode same question Maximum shipping 
def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    match = []
    res = 0
    for i in range(len(boxes)):
        match.append([boxes[i], unitsPerBox[i]])
    match = sorted(match, key = lambda x:-x[1])

    for box, units in match:
        if truckSize > box:
            res += box * units
        else:
            res += truckSize * units
            return res
    
    return res

print(getMaxUnits([1,2,3], [3,2,1], 3))

#Q2:query index1 - endindex, search from strArr, and count the number of the string(first character and last character is vowel) within this range
#TLE
from collections import defaultdict
def hasVowels(strArr, query):
    if not strArr or len(strArr) == 0 or not query or len(query) == 0: return []
    res = [] 
    vowels = ["a", "e", "i", "o", "u"]
    
    # store acculate numbers of vowels
    count = [0] * len(strArr)
    for i in range(len(strArr)):
        if strArr[i][0] in vowels and strArr[i][-1] in vowels:
            count[i] += 1
    
    for q in query:
        arr = q.split("-")
        start = int(arr[0])-1
        
        end = int(arr[1]) 
        if end >= len(strArr):
            end = len(strArr) 
        end = end - 1
            
        count = 0 
        for i in range(start, end + 1):
            curStr = strArr[i]
            if curStr[0] in vowels and curStr[-1] in vowels:
                count +=1
        res.append(count)
    
    return res
#optimal 
from collections import defaultdict
def hasVowels(strArr, query):
    if not strArr or len(strArr) == 0 or not query or len(query) == 0: return []
    res = [] 
    vowels = ["a", "e", "i", "o", "u"]
    # check single word is meet requirement or not
    isVowels =[False] * len(strArr)
    for i in range(len(strArr)):
        if strArr[i][0] in vowels and strArr[i][-1] in vowels:
            isVowels[i] = True
            
    # store acculate numbers of vowels
    count = [0] * len(strArr)
    for i in range(len(strArr)):
        if i == 0 and strArr[i][0] in vowels and strArr[i][-1] in vowels:
            count[i] = 1
        elif i > 0 and strArr[i][0] in vowels and strArr[i][-1] in vowels:
            count[i] = count[i-1] + 1
        elif i == 0:
            count[i] = 0
        else:
            count[i] = count[i-1]
    print(count)
    
    for q in query:
        arr = q.split("-")
        start = int(arr[0])-1
        
        end = int(arr[1]) 
        if end >= len(strArr):
            end = len(strArr) 
        end = end - 1

        counter = 0
        print(start, " ", end)
        if start >= 1:           
            counter = count[end] - count[start-1] 
        else:
            counter = count[end]
            
        res.append(counter)
    
    return res
    
print(hasVowels(["yy", "u","oe"], ['1-2','2-3'])) #[1,2]
print(hasVowels(['aba', 'bcb', 'ece', 'aa', 'e'], ['1-3', '2-5', '2-2'])) #[2,3,0]
print(hasVowels(['aab', 'a', 'bcd', 'awe', 'bbbbbu'], ['2-3', '4-5'])) #[1,1]

# Q3: count the number of increasing subarray with k size
def countHighlyProfitableMonths(stockPrices, k):
    # Write your code here
    if not stockPrices or len(stockPrices) == 0: return 0
    
    res = 0
    left = 0
    while left < len(stockPrices):
        right = left + 1

        while right < len(stockPrices) and stockPrices[right]> stockPrices[right-1]:
            right += 1

        res += max(right - left - k + 1, 0)
        left = right
    return res
      

print(countHighlyProfitableMonths([5,3,5,7,8], 3)) #2 (3,5,7) (5,7,8)
print(countHighlyProfitableMonths([5,3,5,7,8], 1)) # 5
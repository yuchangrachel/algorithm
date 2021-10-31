'''
1.Meandering Array
get [first_largest, first_smallest, second_largest, second-smallest]
[-1, 1, 2, 3, -5] => [3,-5,2,-1,1]
'''
def meanderingArr(arr):
    arr = sorted(arr)
    res = [] 

    while len(arr) > 1:
        res += [arr[-1], arr[0]]
        arr = arr[1:-1]
    
    res += arr
    return res
# print(meanderingArr([-1,1,3,2,-5]))

'''
2.Circular Array
n:numbers range[1:10][means:1,2,3,4,5,6,7,8,9,10]
ends array:point jump.[1,5,10,5] start 1, end 5, start 5, end 10, start 10, end 5. start/end count twice
It's a circular array, for each pair [endNode[i],endNode[i+1]] 0 < i < m-1 we
visit all nodes from endNode[i] to endNode[i+1] by incrementing count inclusive.
If endNode[i+1] < endNode[i] it means it a circular path so we traverse so
we visit both [endNode[i], n] and [1, to endNode[i+1]]
Finally we iterate from 1 to n to find the most visited node also it needs to be smallest
 
Time Complexity O(|n|*m), Space Complexity O(|n|)
'''
def circularArray1(n, endNode): #TLE
    count = [0] * (n+1) # all numbers
    
    for i in range(len(endNode) - 1):
        start = endNode[i]
        end = endNode[i+1]
        
        if start <= end: 
            for j in range(start, end+1):
                count[j] += 1
        else: #go to second round circle
            for j in range(start, n+1):
                count[j] += 1
            for j in range(1, end+1):
                count[j] += 1
    
    resIndex = 0
    count_max = 0
    for i in range(len(count)):
        if count[i] > count_max:
            count_max = count[i]
            resIndex = i
            
    return resIndex


'''
We turn endNode into ranges keeping track of starts and ends separately.
 We can think split circular ranges into two ranges [i, j] i>j -> [i,n][1,j]
 the same way as brute force approach.

 Then we look for most deepest overlapping range. We use two pointer left and right.
When startNode[right] <= endNode[left] it implies that we hit an overlap otherwise we increment left
 The window size just grows so when startNode[right] <= endNode[left] it means that we have hit the
deepest overlap so 'mostvisted' 1. the most visited node 2. the smallest node in the most visited nodes

 Time Complexity O(m*log(m)), Space Complexity O(m)
'''
def circularArray(n, ends):
    # Write your code here
    startNode = []
    endNode = []
    
    for i in range(len(ends) - 1):
        start = ends[i]
        end = ends[i+1]
        
        startNode.append(start)
        endNode.append(end)
        
        if start > end:
            startNode.append(1)
            endNode.append(n)
    # sort startNode and endNode       
    startNode = sorted(startNode)
    endNode = sorted (endNode)
    print(startNode)
    print(endNode)
    

    count_max = 0
    left = right = 0
    while right < len(startNode):
        if startNode[right] <= endNode[left]: # !HARD TO THINK!MUST REVIEW!
            print("count most: " ,count_max)
            count_max = startNode[right]
        else:
            left +=1
        right +=1
        
    return count_max
# print(circularArray(10, [1,5,6, 10,5,7]))

'''
3.Triplets
i< j < k
n[i] + n[j] + n[k] <= t
How many combinations meet above requirements
'''
def triplets1(t, d): #TLE
    # three sum
    d = sorted(d)
    res = 0
    for i in range(len(d) - 2):
        if d[i] > t:
            return res
        for j in range(i+1, len(d) - 1):
            for k in range(j+1, len(d)):
                if d[i] + d[j] + d[k] <= t: 
                    print(d[i], " ", d[j], " ", d[k])
                    res += 1
                else:
                    break
    
    return res

def triplets(t,d):
    # three sum
    d = sorted(d)
    count = 0
    for i in range(len(d) - 2):
        if d[i] > t: return count
        target = t - d[i]
        count += binarysearch(d, target, i)
    
    return count


def binarysearch(ls, target, index):
    low = index + 1
    high = len(ls) - 1
    count = 0
    
    while low < high:
        if ls[low] + ls[high] <= target:
            # WHY HIGH - LOW? eg.[4]-[1]=>1,2,3;1,2,4;1,2,5(three possibilities). [3]-[2]=>1,3,4(one possibility)
            # (2,4) (2,3) (2,5) | (3,4)
    
            count += high - low  # !HARD TO THINK!MUST REVIEW!
            print(count, " ", high, " ", low)
            low += 1
        else:
            high -= 1
    return count

print(triplets(8,[1,2,3,4,5]))
# 1+2+3 <=8
# 1+2+4 <=8
# 1+2+5 <=8
# 1+3+4 <=8


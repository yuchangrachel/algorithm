#1588. Sum of All Odd Length Subarrays
'''
TOPIC:sum of permulate prefix sum at odd length subarray
STEP:
1.create prefix sumarray, traverse fill out
2.construct subarray, outerloop,control start of subarray;inner loop, expand valid subarray
'''
def sumOddLengthSubarrays(arr):
    prefix = [0] * (len(arr)+1)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    res = 0
    #construct odd length subarray
    for i in range(len(arr)):
        end = i
        while end < len(arr): #subarray[i...end]
            print(i, " ", end)
            if i == 0:
                res += prefix[end]
            else:
                val = prefix[end] - prefix[i-1]
                res += val
            end += 2
    return res
            
print(sumOddLengthSubarrays([1,4,2,5,3])) 
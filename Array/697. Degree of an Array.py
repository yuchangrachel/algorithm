'''
    TOPIC:find shortest length of subarray cover elements has highest frequency, if same highest freq, choose one of them which let res shortest.
    STEP:from left find first index of high-freq char and keep find next one is last index of high-freq
    1.create left, right count map since may has many same high-freq char;left right {char:index}
'''
from collections import defaultdict
def findShortestSubArray(nums):
        left,right,count = defaultdict(int),defaultdict(int),defaultdict(int)
        for i in range(len(nums)):
            if count[nums[i]] == 0:
                #first time i met this char
                left[nums[i]] = i
            
            #keep update index until last time
            right[nums[i]] = i
            count[nums[i]] += 1
            
        maxi = max(count.values())
        res = len(nums)
        for k,v in count.items():
            if v == maxi: # highest freq
                res = min(res, right[k] - left[k] + 1)
        
        return res

print(findShortestSubArray([2,1]))
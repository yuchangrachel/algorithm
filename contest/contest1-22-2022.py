#1
def rearrangeArray(nums):
        # think corner case
        # same sign
        sameSign = True
        if nums[0] > 0: #positive
            # see rest of them
            for i in range(1, len(nums), 1):
                if nums[i] < 0:
                    sameSign = False
                    break
        
        if nums[0] < 0:
            for i in range(1, len(nums), 1):
                if nums[i] > 0:
                    sameSign = False
                    break
        
        if sameSign == True:
            return nums
        else:
            positive = []
            negative = []
            for n in nums:
                if n > 0:
                    positive.append(n)
                else:
                    negative.append(n)
            
            # merger two arrays 
            i = 0
            j = 0
            k = 0
            print(positive, " ", negative)
            while i < len(positive) or j < len(negative):
                print("k ", k)
                if k % 2 == 0:
                    nums[k] = positive[i]
                    i += 1
                else:
                    print("j", negative[j])
                    nums[k] = negative[j]
                    j += 1
                
                k += 1
        return nums

# print(rearrangeArray([-1,1]))

#2 easy

#3
# 2150. Find All Lonely Numbers in the Array
from collections import Counter
def findLonely(self, nums: List[int]) -> List[int]:
        mapping = collections.Counter(nums)
        res = []
        for n in nums:            
            if (n-1) not in mapping.keys() and (n+1) not in mapping.keys() and mapping[n] == 1:
                res.append(n)
        return res
        
# print(findLonely([1,3,5,3]))
# print(findLonely([10,6,5,8]))


#4
# 2151. Maximum Good People Based on Statements
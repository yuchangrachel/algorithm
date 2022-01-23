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

from collections import Counter
def findLonely(nums):
        # res = []
        # visit = set()
        # for n in nums:
        #     if n in visit:
        #         if n in res:
        #             res.remove(n)
        #         continue
        #     else:
        #         visit.add(n)
        #         if (n+1) not in nums and (n-1) not in nums:
        #             res.append(n)
                
        # return res
        mapping = Counter(nums)
        res = []
        for n in nums:
            if mapping[n] > 1:
                continue
            else:
                if (n+1) not in nums and (n-1) not in nums:
                    res.append(n)
        return res
        
            
print(findLonely([1,3,5,3]))
print(findLonely([10,6,5,8]))
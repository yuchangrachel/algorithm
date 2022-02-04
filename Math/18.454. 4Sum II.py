'''
    TOPIC: like 2sum
    STEP:brute force O(n^4) -> O(n^2)store A+B in map {total:freq}, then when iterate C+D=sum, see if 0-sum already in map
    '''
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        mapping = collections.defaultdict(int)
        for n in nums1:
            for n2 in nums2:
                mapping[n+n2] += 1
        
        for n in nums3:
            for n2 in nums4:
                target = 0-(n+n2)
                res += mapping[target]
                # if mapping[target] > 0:
                #     res += 1
                #     mapping[target] -= 1
        return res
            
        
        
#18.4sum
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            else:
                valid4 = self.threeSum(nums[i+1:], target-nums[i])
                for v in valid4:
                    v.append(nums[i])
                    res.append(v)
                    
        return res
        
    
    def threeSum(self, nums, target):
        #store valid unique truplets
        res = []
        for i in range(len(nums)-2):
            # avoid first of three is duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = target - nums[i]
                low = i + 1
                high = len(nums)-1
                while low < high:
                    if nums[low] + nums[high] == left:
                        res.append([nums[i], nums[low], nums[high]])
                        while low + 1 < len(nums) and nums[low] == nums[low+1]:
                            low += 1
                        while high - 1 >= 0 and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < left:
                        low += 1
                    else:
                        high -= 1
        return res
            
# Two pointer, binary Search
def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        
        res = []
        
        # don't need to consider index
        nums.sort()
        
        for i in range(0,len(nums) - 2): # actually three loops, outer(-2),inner(-1 and 0)
            # since sorted, compare to neighbor, avoid first num[i] duplicate
            if i > 0 and nums[i] == nums[i-1]: 
                continue
                
            rest = 0- nums[i]
            low = i + 1
            high = len(nums) - 1
            # since sorted, so use binary search
            while low < high:
                if nums[low] + nums[high] == rest:
                    res.append([nums[i], nums[low], nums[high]])

                    # for next round, avoid second and third number duplicate
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < rest:
                    low+=1
                else:
                    high-=1
                    
        return res
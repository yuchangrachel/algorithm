def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0: return []
        
        # 1WAY overwrite input T:O(nlogn) S:O(1)
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        
        # return sorted(nums)
        
        # 2WAY Making a new array, not in place.T:O(nlogn) S:O(1) result not included
        # return sorted([n** 2 for n in nums])
        
        # 3WAY T:O(n) compare and fill in slot; S:O(n)
        # have negative number, compare low and high see who's square is larger, fill in [k]
        res = [0] * (len(nums))
        
        k = len(nums) - 1
        low = 0
        high =len(nums) - 1
        while low <= high:
            if abs(nums[low]) < abs(nums[high]):
                res[k] = nums[high] * nums[high]
                k-=1
                high -= 1
            else:
                res[k] = nums[low] * nums[low]
                k-=1
                low += 1
        
        return res
                
        
        
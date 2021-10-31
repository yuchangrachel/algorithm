def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0: return []
        
        # 1WAY overwrite input T:O(nlogn) S:O(1)
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        
        # return sorted(nums)
        
        # 2WAY Making a new array, not in place.T:O(nlogn) S:O(1) result not included
        # return sorted([n** 2 for n in nums])
        
        
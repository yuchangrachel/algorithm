'''
    TOPIC:Iterate array, update farthest if can reach last index. If 0 at farthestIndex and not last, return false
    ATT:corner case nums=[0] return True
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        farthest = 0
        for i in range(len(nums)):
            if nums[i] == 0 and farthest == i and i < len(nums)-1:
                return False
            
            if farthest >= len(nums)-1:
                return True
            #update farthest
            farthest = max(farthest, i + nums[i])
        
        return True
        
        
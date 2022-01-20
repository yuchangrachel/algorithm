'''
    TOPIC:change one time at most make increasing array(include =) Greedy eg.(4),2,3; -1,(4),2,3, 2,3,3,(2),4 find pattern
    STEP: swap in-place
    1.create count=1, when [i]compare[i-1]: if count already=0 return False
    2.elif i==1(meani-1is index0) or [i] >= [i-2], then change [i-1] =[i]make smaller
    3.else(mean [i] < [i-2]) then change [i] =[i-1] make bigger 
    '''
    def checkPossibility(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0: return False
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if count == 0:
                    return False
                elif i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                count -= 1
        return True

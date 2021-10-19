'''
55. Jump Game
    LOGIC:
    1. Need maxIndex variable update if >= lastIndex => True
'''
def canJump(nums):
        if len(nums) <= 1: return True #[0]
        
        maxIndex = 0
        for i in range(len(nums)):
            if maxIndex <= i and nums[i] == 0: #cannot jump  
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= len(nums) - 1: return True
            
        return False
print(canJump([3,2,1,0,4])) #[0]=>true [3,2,1,0,4]=>false [0,2,3]=>false

'''
45.Jump Game II
    LOGIC:
    1.greedy
    2.set jumpNo, endIndex, farIndex
'''
def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        
        jump = 0
        endIndex = 0
        farIndex = 0
        
        for i in range(0, len(nums)-1, 1): #no need go through last one, since alway can reach lastindex
            farIndex = max(farIndex, i+nums[i])
            if i == endIndex:
                # need another jump
                jump += 1
                endIndex = farIndex
        return jump
            
# 55.Jump Game
'''
    TOPIC:Traverse Array jump value to see if go to last index
    STEP:
    1.corner case nums is [0], one number => true
    2.if meet cur == 0 and farthest <= curindex => false
    3.update farthest, can use farthest to see if reach last
'''
def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        farthest = 0
        for i in range(len(nums)):
            if nums[i] == 0 and farthest <= i: return False
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums)-1: return True
        return False
# print(canJump([3,2,1,0,4])) #[0]=>true [3,2,1,0,4]=>false [0,2,3]=>false

'''
45.Jump Game II
    LOGIC:
    1.greedy
    2.set jumpNo, endIndex, farIndex
'''
def jump2(nums):
    '''
    LOGIC: greedy
    HOW:
    1.step var will calculate minimum jump
    2.endIndex track when finish cur jump
    3.always update endIndex into farIndex, so jump less
    '''
    if not nums or len(nums) == 0: return 0
        
    jump = 0
    farIndex = 0
    endIndex = 0 #when start next jump
    for i in range(len(nums)-1): # no need consider lastone since no jump at that point
        farIndex = max(farIndex, nums[i] + i)
        if i == endIndex: # finish one jump,start new jump
            jump += 1
            endIndex = farIndex
                
            if endIndex >= len(nums)-1: return jump
    return jump
    
print(jump2([2,3,1,1,4]))

        
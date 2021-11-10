/*
198. House Robber
LOGIC:
1.Not like mincost for climbing stair return dp[len-1] or dp[len-2]pick min one, since stair case start from 0index or 1index. 
2.Other case starting from same starting point will return dp[n]
*/
// def rob(self, nums: List[int]) -> int:
//         if not nums or len(nums) == 0: return 0

//         res = 0
//         dp = [0] * len(nums)

//         dp[0] = nums[0]
//         if len(nums) == 1: return dp[0]
//         dp[1] = max(dp[0], nums[1])
//         if len(nums) == 2: return dp[1]

//         for i in range(2, len(nums)):
//             dp[i] = max(dp[i-2] + nums[i], dp[i-1])
//             res = max(res, dp[i])

//         return res

/*
213.
 '''
    LOGIC
    1.It is circular path, if pick last cannot pick first, so how to make choice
    2.create two dp: startfirst, startsecond
    3.compare startfirst[n-1](skip last one) vs. startsecond[n]
    
    '''
    def rob(self, nums: List[int]) -> int:
        # corner case
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        #1st option, start first and stop beforer last, since first is stolen
        firststart = self.helper(nums, 0, len(nums) - 2)
        secondstart = self.helper(nums, 1, len(nums) - 1)
        
        return max(firststart, secondstart)
    
    def helper(self, nums, start, end):
        # same as above
        if start == end: return nums[start]
        if end == start+1: return max(nums[start], nums[end])
        
        # create dp
        dp = [0] *(end-start+1)
        
        #init dp
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start+1])
        
        for i in range(2, len(dp), 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[start+i])
        return dp[len(dp)-1]
    
*/

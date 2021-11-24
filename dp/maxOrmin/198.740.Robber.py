
'''
740. Delete and Earn
    bottom-top dp
    delete one value, meanwhile val+1, val-1 as well(but these two not counted)
    nums order doesn't matter, use freq sort it,down to Robber problem    
'''
def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        # for sort nums:get pair n:freq*n, get max, then set dp size is max_val+1
        max_val = max(sorted(nums))
        input_dp = [0] * (max_val+1) #since include 0
        for n in nums:
            input_dp[n] += n

        # dp[i] only current status skip or take, still need result variable updat maxpoint
        maxpoint = 0
        
        dp=[0]*(max_val+1)
        dp[0] = 0
        dp[1] = input_dp[1]
        # take[2] or skip:just need dp[1]
        dp[2] = max(input_dp[2], dp[1])
        
        for i in range(3,len(input_dp)):
            dp[i] = max(dp[i-1], dp[i-2] + input_dp[i])
            maxpoint = max(maxpoint, dp[i])
        return maxpoint

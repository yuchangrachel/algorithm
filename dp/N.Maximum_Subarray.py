'''
53. Maximum Subarray
    LOGIC:
    1.dp - single val DP
    2.need both dp val and max_result! WHY? dp is for compare add cur, or not, if +cur> cur, will extend subarray;otherwise, start over subarray
'''
def maxSubArray(self, nums: List[int]) -> int:
        max_v = nums[0] #has negative
        dp = nums[0]
        
        for i in range(1,len(nums)):
            dp = max(dp+nums[i], nums[i])
            max_v = max(dp, max_v)
        return max_v

'''
918. Maximum Sum Circular Subarray
'''
'''
53. Maximum Subarray
    LOGIC:
    1.dp - single val DP
    2.need both dp val and max_result! WHY? dp is for compare add cur, or not, if +cur> cur, will extend subarray;otherwise, start over subarray
'''
def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])
        
        return res
# 152. Maximum Product Subarray
def maxProduct(self, nums: List[int]) -> int:
        #TOPIC:maximum product subarray:subproblem,pickORnot=>DP
        #STEP:
        #1.Since have 0, or negative,eg.[-2,3,-4]=>24. so not only think max
        #2.use two dps,one max, one min. compare big dp+cur, small dp+cur, cur
        if not nums or len(nums) == 0: return 0
        f = [0] * len(nums)
        g = [0] * len(nums)
        f[0] = nums[0]
        g[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1]*nums[i], g[i-1] * nums[i], nums[i])
            g[i] = min(f[i-1]*nums[i], g[i-1] * nums[i], nums[i])
            res = max(res, f[i])
        return res
'''
918. Maximum Sum Circular Subarray
'''
def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #TOPIC:similar to maxium sum subarray, but this is circular
        #STEP:
        #1case: find one partition maximum subarray
        #2case: find sepate partition(part of tail and part of head) can combine as maximum array
        #So, total = maxsum + minsum, compare max(maxsum, total-minsum)
        #corner case if use above formula, think all negative, total-minsum=0, but actually i wanna maxsum directly
        if not nums or len(nums) == 0: return 0
        res = 0
        total = 0
        dpmax= 0
        maxoverall = nums[0]
        dpmin=0
        minoverall = nums[0]
        for a in nums:
            dpmax = max(dpmax+a, a)
            maxoverall = max(maxoverall, dpmax)
            dpmin = min(dpmin+a, a)
            minoverall = min(minoverall, dpmin)
            total += a
            
        return max(maxoverall, total-minoverall) if maxoverall > 0 else maxoverall
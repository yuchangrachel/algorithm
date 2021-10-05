# two options, 1step or 2step, so use top-bottom dp: recursion with memorization
def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        
        #create dp, need n
        dp = [0]*n
        return self.helper(0, n, dp)
    
def helper(self, i, n, dp):
        # base case / terminate
        # no step
        if i > n: return 0
        
        #reach destination count one option
        if i == n: return 1
        
        #see if already had record
        if dp[i] > 0: return dp[i]
        
        dp[i] = self.helper(i+1, n, dp) + self.helper(i+2, n, dp)
        return dp[i]
        
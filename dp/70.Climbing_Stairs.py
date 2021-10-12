# 1WAY:top bottom dp
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

# //top bottom recursion with memorization
# var climbStairs = function (n) {
#   if (n <= 1) return n;
#   const dp = new Array(n).fill(0);
#   //startindex to n
#   return helper(0, n, dp);
# };

# const helper = function (i, n, dp) {
#   // terminate case
#   if (i > n) return 0;
#   if (i == n) return 1; //last step

#   //if dp already set, dont need set
#   if (dp[i] != 0) return dp[i];

#   //do memorization
#   dp[i] = helper(i + 1, n, dp) + helper(i + 2, n, dp);
#   console.log(i, " ", dp[i]);
#   return dp[i];
# };

# console.log(climbStairs(3));

# //2WAY: bottom up dp ,two options step one or step two
# var climbStairs = function(n) {
#     if (n == 0) return n
    
#     const dp = new Array(n+1).fill(0)
#     //initiate dp
#     dp[0] = 0
#     dp[1] = 1
#     dp[2] = 2
#     for(let i = 3; i <=n; i++){
#         dp[i] = dp[i-1] + dp[i-2]
#     }
#     return dp[n]
# };


        
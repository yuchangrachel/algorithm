def numTrees(self, n: int) -> int:
        '''
        LOGIC:
        Similar to all possible unique path => dp
        left and right subtree combination use multiple operation since they are independent event
        dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0] keep split sub_dp
        dp[2] = dp[0] * dp[1] + dp[1] * dp[0]
        '''
        dp = [0] * (n+1)
        dp[0] = 1 # empty tree is one unique tree

        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-1-j] #left*right
                print(i, " ", j, " ", i-1-j, dp[i])
        return dp[n]
            
        
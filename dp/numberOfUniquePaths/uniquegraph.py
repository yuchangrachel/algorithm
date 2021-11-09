def uniquePaths(self, m: int, n: int) -> int:
        '''
        LOGIC:
        How many possible unique paths to get destionations? THINK DP
        two ways: move right or move down
        dp[i][j] so far number of paths
        simulate back
        1WAY BOTTOM-TOP DP
        TIME:O(m*n)
        '''
        dp = [[0 for j in range(n)] for i in range(m)]
        
        #first row only one direction: move right (accept from left)
        for i in range(n):
            dp[0][i] = 1
        #first column only one direction: move down(accept from up)
        for j in range(m):
            dp[j][0] = 1
        
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
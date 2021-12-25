'''
    TOPIC: find minimum path sum from top-left to bottom-right. only two move:right, down
    STEP: bottom-up dp, so init dp
    1.create 2d array(default 0, size +1) since no negative dp[i][j] store so far minimum path sum
    2.init dp, first row and first column set grid val+dp(min)
'''
def minPathSum(grid):
        if not grid or not grid[0]: return 0
        #creat dp
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        #init dp
        dp[0][0] = grid[0][0]
        #set first row
        for j in range(1,len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        #set first column:
        for i in range(1,len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[len(grid)-1][len(grid[0]) - 1]

print(minPathSum([[1]]))
# 120. Triangle
'''
TOPIC:find minimum sum path only choose from neighbors of another row
IDEA: bottom-top DP
LOGIC:
this is triangle, so number amount is increasing by rows. better way is from bottom to top
At k layer, ith number:
minpath[k][i] = min(minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i]
minpath[k][i] only use once, so dp 2D-> dp 1D
rewrite:
minpath[i] = min(minpath[i], minpath[i+1]) + triangle[i]
HOW:
1.store last row into dp
2.layer starting from second last row, and layer has (layer+1) elements
'''
def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0: return 0
        dp = triangle[-1]
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(0, layer+1, 1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[layer][i]
        return dp[0]
                
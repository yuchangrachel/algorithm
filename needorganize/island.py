# 695. Max Area of Island
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # corner case
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0: return 0 #no island
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                # return area, so can compare with other islands' areas
                    area = self.dfs(grid, i, j)
                    if area > max_area:
                        max_area = area
        return max_area
    
    def dfs(self, grid, i, j):
        # check boundary or invalid val
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 0:
            return 0
        
        # set visited
        grid[i][j] =0
        
        return 1 + (self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1))
        
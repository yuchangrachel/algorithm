def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        LOGIC:
        dfs deep search the whole current island, visited set 2, then search other island
        '''
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0: return 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 2
                return 1+ dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # find one of island, do dfs find whole island
                    temp = dfs(i, j)
                    max_area = max(temp, max_area)
                    
        return max_area
        
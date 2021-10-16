# find center, dfs 4directions visited-> change to newColor
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # if not image or len(image) == 0: return image
        # if image[sr][sc] == newColor: return image #nothing change
        startColor = image[sr][sc]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r > len(image)-1 or c > len(image[0])-1 or image[r][c] == newColor or image[r][c] != startColor: return
            image[r][c] = newColor
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr, sc)
        
        return image
        

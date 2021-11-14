# 79. Word Search
def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        TOPIC: backtracking since look for whole valid char path, if one of them not works, search other directions(cur cell has four adjacent cells) 
        TIME: O(m*n*4^len(word))
        '''
        if not board or not board[0] or len(board) == 0 or len(board[0]) == 0: return False
        
        self.visited = set() # store tuple
        
        def dfs(i, j, index):
            if index == len(word): return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index] or (i, j) in self.visited: 
                return False
            
            self.visited.add((i, j))
            res = dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1)
            # backtrack, visited-> unvisited
            self.visited.remove((i,j))
            return res
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        
# 212. Word Search II
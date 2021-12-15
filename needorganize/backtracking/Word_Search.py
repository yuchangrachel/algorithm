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

'''
    if (board == null || board[0] == null || board.length == 0 || board[0].length == 0) return false
    const visit = new Array(board.length).fill(false)
    for(let i = 0; i <visit.length; i++){
        visit[i] = new Array(board[0].length).fill(false)
    }
    
    dfs = function(i, j, index){
        if (index == word.length) return true
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || visit[i][j] || board[i][j] != word[index]) return false
        visit[i][j] = true
        //four direction
        let res = dfs(i+1, j, index+1) || dfs(i-1, j, index+1) || dfs(i, j+1, index+1) || dfs(i, j-1, index+1)
        visit[i][j] = false
        return res   
    }
    
    for (let i = 0; i < board.length; i++){
        for (let j = 0; j < board[0].length; j++){
            if (dfs(i, j, 0)) return true
        }
    }
    return false
};
'''
        
# 212. Word Search II

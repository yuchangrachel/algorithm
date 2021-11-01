def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        LOGIC:
        similar to find island 1's surrounded by water 0's.  replace island's 1s into 0s.
        If 0 is on board and other inside 0s connected with border 0, then can't make surrounded regions
        dfs:flip border 0 and connected border 0s -> '$', later flipt back -> '0'
        dfs:flip region 0 > X
        """
        if not board or not board[0] or len(board) == 0 or len(board[0]) == 0: return
        
        def dfs(i , j):
            if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = '$'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        # first check border flip 0 and connected 0 -> $
        # start from first and fast row
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    dfs(i,j)
        
        # start from first column and last column
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == 'O':
                    dfs(i,j)
                    
        # In region, flip 0->X, flip $->O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'
    
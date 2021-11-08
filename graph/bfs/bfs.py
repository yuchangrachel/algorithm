
            
# 116. Populating Next Right Pointers in Each Node
from collections import deque
class Solution:
    # bfs(level order search), will next point to right subtree, so don't need while size, use compare parent's left and right child
    # rebuild tree
    
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            # may next point to the cross same level of child tree so don't use while size
            top = q.pop()
            if top.left and top.right: # for own subtree
                top.left.next = top.right
                q.append(top.left)
                q.append(top.right)
                
                # how to cross check if parent has right tree
                if top.next:
                    top.right.next = top.next.left
                
        return root

# 542. 01Matrix
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        LOGIC:
        Find nearest distance use BFS in graph
        0s all are starting point, store into queue, dont need while index < size template because all 0s are not direct relationship
        1s store max value
        if meet boundary or newNode <= cur + 1 this cell already found shortest distance to 0
        '''
        if not mat or not mat[0] or len(mat) == 0 or len(mat[0]) == 0: return []
        
        q = deque()
        dir =[[1,0], [-1, 0], [0, 1], [0, -1]]
        
        # store 0s into q and 1s reassign as max_val
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')
           
        while len(q) > 0:
            top = q.popleft()
            cur = mat[top[0]][top[1]]
            
            for d in dir:
                x = top[0] + d[0]
                y = top[1] + d[1]
                
                # check 4 direction neighbors if valid or not 
                if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or mat[x][y] <= cur + 1:
                    continue
                else:
                    mat[x][y] = cur + 1
                    
                    # store not 0s but updated distance value into queue
                    q.append((x,y))
        
        return mat
                    

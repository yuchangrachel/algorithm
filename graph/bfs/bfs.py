
            
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
    '''
    LOGIC:
    cell's new value is distance with nearest 0
    If in graph, find shortest distance, will think about bfs.
    if [i][j] == 0:then still[i][j], all 0s are starting points, store into q
    if [i][j] == 1: update to the max, explore neighbors, if boundary or neighbors < cur + 1, neighbor dont need update(since already min)
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0] or len(mat)==0 or len(mat[0])==0: return [[]]
        
        q = deque()
        
        # doing bfs, most time will set 4 direction array first
        dist = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # search 2d array if that is 0, add its coordinate into queue
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j)) # add tuple in queue all 0s are starting point
                else:
                    mat[i][j] = float('inf') # temperarily change in-place
                    
        while len(q) > 0:
            top = q.popleft()
            for dir in dist:
                # x, y are neighbor of 0s
                x = top[0]+dir[0] 
                y = top[1] + dir[1]
                
                #check boundary or invalid input
                if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or mat[x][y] <= mat[top[0]][top[1]] + 1: 
                    continue
                
                #need update neighbor
                mat[x][y] = mat[top[0]][top[1]] + 1
                
                # store neighbor coordinate into q, need reach more cell far away from 0s
                q.append((x,y))
                
        return mat


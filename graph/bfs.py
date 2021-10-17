# 102. Binary Tree Level Order Traversal
# level-order traversal = breath first search
from collections import deque
class Solution:
    # Level order traversal mean use queue
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] #no nodes'values
        
        q=deque()
        q.append(root)
        res = []
        while len(q) > 0:
            size = len(q)
            index = 0
            inner = []
            while index < size:
                top = q.popleft()
                inner.append(top.val)
                
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                index += 1
            res.append(inner)
        return res
            
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

# 994.Rotting Oranges
from collections import deque
class Solution:
    '''
    LOGIC:
    1.If at the beginning, no fresh, min = 0; otherwise check and rot fresh level by level, if cannot rot all fresh, then return -1
    2.bfs 
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0: return -1
 
        freshcount = 0
        
        # bfs
        q = deque()
        direction = [[1,0],[-1, 0], [0, 1], [0,-1]]
        #store all rot's coordinate into q, and spread out
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshcount += 1
       
        minute = 0
        while len(q) > 0 and freshcount > 0:
            size = len(q)
            index = 0
            while index < size:
                top = q.popleft()
            
                for dir in direction:
                    x = top[0] + dir[0]
                    y = top[1] + dir[1]
                
                    # check boundary or invalid input
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y] == 2: continue

                    grid[x][y] = 2 #change 1 to 2
                    # only store new rot
                    q.append((x,y))
                    freshcount -= 1
                index+=1
                
            minute += 1
            
            
        print(grid)
        if freshcount == 0:
            return minute
        else:
            return -1 #can't rot all fresh
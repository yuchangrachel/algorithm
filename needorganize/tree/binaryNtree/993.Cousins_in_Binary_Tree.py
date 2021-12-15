from collections import deque

    '''
    LOGIC:
    1.check two node are cousin if they have same depth with different parents
    2.check if corner case find two node use boolean val + same parents? and compare some depth use bfs(queue) 
    '''
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return None
        
        q = deque([root])
        
        while len(q) > 0:
            # only compare same level
            isX = False
            isY = False
            
            # queue template handle same level
            index = 0
            size = len(q)
            while index < size:
                top = q.popleft()
                
                # check cur is node we want, if yes mark down, will use with later neighbors
                if top.val == x: isX = True
                if top.val == y: isY = True
                
                # can filter some children not match this constraint
                if top.left and top.right:
                    if (top.left.val == x and top.right.val == y) or (top.left.val == y and top.right.val == x): # same cur parent 
                        return False
                
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                
                index+=1
            
            # finish one level, check if find both nodes
            if isX == True and isY == True: 
                return True
            if isX == False and isY == True: 
                return False
            if isX == True and isY == False: 
                return False
            
        
        return False
                
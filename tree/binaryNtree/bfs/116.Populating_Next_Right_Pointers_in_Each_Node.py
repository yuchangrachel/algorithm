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
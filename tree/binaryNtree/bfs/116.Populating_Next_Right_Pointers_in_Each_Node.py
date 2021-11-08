from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        LOGIC:
        Level order traversal
        cross subtree, so don't need while size template
        if parents point to their sibling, so their children are cousin,can be linked
        '''
        if not root: return None
        
        q = deque([root])
        
        while len(q) > 0:
            top = q.popleft()
            if top.left and top.right:
                top.left.next = top.right 
            if top.next and top.right:
                # cross subtree
                top.right.next = top.next.left
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        
        return root
                

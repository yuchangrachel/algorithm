116
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
                
117
var connect = function(root) {
    //1WAY BFS - queue S:O(n) ADD next pointer for nodes
    if (root == null) return root
    const q = []
    q.push(root)
    
    while (q.length > 0){
        let size = q.length
        while (size > 0){
            let top = q.shift()
            if (size >1){ //have more in cur level
                top.next = q[0]
            }
            size -= 1
            if (top.left != null) q.push(top.left)
            if (top.right != null) q.push(top.right)
        }  
    }
    return root
};

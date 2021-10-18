'''
    recursive:
    use helper(root, root), do two roots one for left subtree and another for right subtree
    T:O(n/2)
    S:O(logn) in recursive call
''' 
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)
    
def helper(self, r1, r2):
        if not r1 and r2: return False
        if r1 and not r2: return False
        if not r1 and not r2: return True
        
        # check both sides' vals
        if r1.val != r2.val: 
            return False
        else:
            return self.helper(r1.left, r2.right) and self.helper(r1.right, r2.left)

from collections import deque
class Solution:
    '''
    Iterative
    compare level by level, T:O(logn) / O(heigh of tree) use bfs(queue)
    store left and right into q,
    pop pair comparison
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        q = deque([root.left, root.right])
        while len(q) > 0:
            top1 = q.popleft()
            top2 = q.popleft()
            
            if not top1 and not top2:
                # NOT TURE since didnt traverse whole tree yet!!
                continue 
            elif (not top1 or not top2) or (top1.val != top2.val): 
                return False
            else:
                # keep tracking their children
                q += [top1.left, top2.right, top1.right, top2.left]
        return True
                
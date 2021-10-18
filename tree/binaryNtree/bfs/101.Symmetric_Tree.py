'''
    recursive:
    use helper(root, root), do two roots one for left subtree and another for right subtree
    T:O(n/2)
    S:O(logn) in recursive
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
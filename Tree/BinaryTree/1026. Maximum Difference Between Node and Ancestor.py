'''
    TOPIC:cur as ancestor, find his child node has with max diff to him
    STEP:
    1.pretraversal, traverse parent first(find max diff for parent), then find max, min(because abs, [1-8][8-14]), update res max min to next child
'''
def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = [0]*1
        self.preorder(root.val, root.val, root, res)
        return res[0]
    
def preorder(self, mini, maxi, root, res):
        if not root: return 
        res[0] = max(res[0], abs(maxi-root.val))
        res[0] = max(res[0], abs(root.val-mini))

        maxi= max(maxi, root.val)
        mini = min(mini,root.val)
        self.preorder(mini, maxi, root.left, res)
        self.preorder(mini, maxi, root.right, res)
        
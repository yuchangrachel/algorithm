#94
'''
    recursion: 
    Time complexity : O(n). The time complexity is O(n) because the recursive function is T(n) = 2 \cdot T(n/2)+1T(n)=2⋅T(n/2)+1.
    Space complexity : The worst case space required is O(n), and in the average case it's O(logn) where nn is number of nodes.

    '''
def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
    
def inorder(self, root, res):
        if not root: 
            return 
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

'''
    Iteration: 
    LOGIC: 
    since need find leftmost first, so use cur pointer searching to the leaves
    T:O(n) S:O(n)
'''
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        stack = [] # dont store root first, since need while cur store parent into stack
        res = []
        cur = root
        while cur or len(stack) > 0: #dont store root at first
            #keep tracking if there is left subtree
            while cur:
                stack.append(cur)
                cur = cur.left
                
            # down to leaf subtree's leave
            # no left child anymore, cur is leaf, so pop and store into res
            if len(stack) > 0:
                top=stack.pop()
                res.append(top.val)
            
                # go to right subtree no matter hash right or not, goal is pop stack
                cur = top.right
        return res
            
#173. Binary Search Tree Iterator
'''
    TOPIC:inorder iterate
    STEP:
    1.in constructor, while cur, search left
    2.next method, will return pop one, then also store new smallest(starting from right) do while loop search left again
    3.hasnext method, if nothing to pop from stack, so no right anymore, then done all tree
'''
def __init__(self, root: Optional[TreeNode]):
        cur = root
        self.stack = []
        while cur:
            self.stack.append(cur)
            cur = cur.left

#which node is next smallest, default is leftmost(in contrustor)
def next(self) -> int:
        nextsmall = self.stack.pop()
        #see cur if has right
        if nextsmall.right:
            cur = nextsmall.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        
        return nextsmall.val

def hasNext(self) -> bool:
        return len(self.stack) != 0


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

#94 inorder traversal
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
            
# 530.Minimum absolute difference in BST
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        BST inorder:sorted
        How to get mindiff, comes from neighbor. compare to prevnode, update diff
        '''
        self.min_diff =float('inf')
        self.prev = -1 #store prev node, 
        
        def inorder(root):
            if not root:return
            inorder(root.left)
            
            if self.prev != -1: #no prev, so nothing compare with root 
                self.min_diff = min(self.min_diff, abs(self.prev - root.val))

            self.prev = root.val
            
            inorder(root.right)
            
            
        inorder(root)
        return self.min_diff
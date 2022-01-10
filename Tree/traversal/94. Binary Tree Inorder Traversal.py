'''
    TOPIC: recursion to traversal or iterative
    RECURSION TIME:0(n) T(n) = 2 \cdot T(n/2)+1T(n)=2⋅T(n/2)+1. SPACE: O(n) average is O(logn)
Space complexity: O(n)O(n)
    ITERATIVE TIME:O(N) SPACE:O(N)
    STEP:iterative
    1.create stack=[],cur=root, while stack or cur: 2.while loop find left,stack add before move pointer
    3.reassign cur = stack.pop() 4.cur = cur.right
'''
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        stack = []
        cur = root
        
        while len(stack) > 0 or cur:
            while cur:
                #add stack first, move on cur pointer
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
            
            
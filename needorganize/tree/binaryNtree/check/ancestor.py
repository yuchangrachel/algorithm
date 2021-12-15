# 235. Lowest Common Ancestor of a Binary Search Tree
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None
        
        # case1: p, q both in left/right subtree, do recursion. 
        # case2: p , q in different subtrees, then current node is lowest ancestor for both
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# 236. Lowest Common Ancestor of a Binary Tree
'''
    TOPIC:ancestor
    STEP:
    1.if left and right return NOT NULL, cur as LCA
    2,if left return NULL, right is LCA
    3.if right return NULL, left is LCA
     eg.root(3), search p(5), q(4), do recursion handle 5 first, return right away, which near root, wont go 4
'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q: return root
        lefter = self.lowestCommonAncestor(root.left, p, q)
        righter = self.lowestCommonAncestor(root.right, p, q)
        if lefter and righter: #both not null
            return root
        return lefter or righter

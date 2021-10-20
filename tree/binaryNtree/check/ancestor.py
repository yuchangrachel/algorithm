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
# https://www.youtube.com/watch?v=WRAJ8Q9bICM
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if (not root) or (root == p) or (root == q):
            return root
        
        left_sub = self.lowestCommonAncestor(root.left, p, q)
        right_sub = self.lowestCommonAncestor(root.right, p, q)
        
        if left_sub and right_sub:
            return root
        return left_sub or right_sub
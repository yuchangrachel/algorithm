# search nodes from root to leaf dfs traversal(pre-order, in-order, post-order)
# pick one tree as result tree, build tree
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # corner case/base case
        if not root1: return root2
        if not root2: return root1
        if not root1 and not root2: return None
        root1.val += root2.val
        
        # build tree required
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
    
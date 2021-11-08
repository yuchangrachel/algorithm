def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        LOGIC:
        REBUILD TREE
        Let tree2 merge into tree1, do level order traversal, if same position has different values, sum up them, update new value of root in tree1
        '''
        if not root1 and root2: return root2
        if root1 and not root2: return root1
        if not root1 or not root2: return None
        else:
            # overlap
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1

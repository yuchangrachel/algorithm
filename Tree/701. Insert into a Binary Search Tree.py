'''
    TOPIC:BST insert, think BST val determine should traverse to which branch from two branches
    STEP:
    1.dfs traverse, until see None mean insert position, mean basic case null:insert new node
    2.in the end return root because return whole tree
    '''
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # empty postion need inserted
        if not root: return TreeNode(val)
        if val > root.val: # go to right branch
            root.right = self.insertIntoBST(root.right, val)
        else: 
            root.left = self.insertIntoBST(root.left, val)
        return root
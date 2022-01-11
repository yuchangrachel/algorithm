
    '''
    TOPIC:sum all branches from root to leaf. convert binary to decimal
    STEP:dfs traverse tree dfs(root, "") dfs(root, str(s+root.val)),handle subtotal add to sum
    1.create helper(root,s)
    2.if leaf handle subtotal,total += int(str(s+root.val), 2) convert binary to decimal
    3.else, do recursion helper(root.left/right, str(s+root.val))
    ATT:
    1.avoid use global variable res or closure method, can use res with size 1 to pass to helper. Remember! primitive variable changed in helper won't affect main method
    2.convert binary to decimal use int(Number, 2)
    '''
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = [0]*1
        self.preorder(root, res, "")
        return res[0]
        
    def preorder(self, root, res, s):
        if not root:
            return
        elif not root.left and not root.right:
            res[0] = res[0] + int(s+str(root.val), 2)
            return
        
        self.preorder(root.left, res, s + str(root.val))
        self.preorder(root.right, res, s + str(root.val))
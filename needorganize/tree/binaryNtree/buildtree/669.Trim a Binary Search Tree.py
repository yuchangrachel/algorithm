# 669. Trim a Binary Search Tree
def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #TOPIC: trim BST, let all nodes in [low, high]. rebuild tree
        if not root: return None
        if root.val > high: # impossbile go through right subtree
            return self.trimBST(root.left, low, high)
        if root.val < low: # impossible go through left subtree
            return self.trimBST(root.right, low, high)
        #now root.val in [low, high], see if its all subtree all valid
        #REBUILD TREE TEMPLATE
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
        
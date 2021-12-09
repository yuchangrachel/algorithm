#105. Construct Binary Tree from Preorder and Inorder Traversal
'''
    TOPIC:preorder+inorder=>build binary tree
    STEP:
     1.first in preorder is root, responsively to find same node in inorder, that will divide left and right subtree
    2.Build tree need recursion, preorder for finding cur root and pop it directly, 
    DONT DO RECURION UPDATE PREORDER:preorder[1:] because inorder split smaller branch will null first, 
    then inorder divide: root.left = inorder[:root], root.right=inorder[root+1:]
'''
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        root=TreeNode(preorder.pop(0))
        rootIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:rootIndex])
        root.right = self.buildTree(preorder, inorder[rootIndex+1:])
        return root
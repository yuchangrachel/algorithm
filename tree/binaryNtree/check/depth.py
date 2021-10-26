class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

# check is tree is balanced or not       
def isBalanced(root):
        if not root: return True
        
        # Each node need to check maxheight see if balanced or not
        left = NodeMaxHeight(root.left)
        right = NodeMaxHeight(root.right)
        if abs(left - right) > 1: return False
        
        return isBalanced(root.left) and isBalanced(root.right)

# get max depth of whole tree
def NodeMaxHeight(root):
        if not root: return 0
        return 1 + max(NodeMaxHeight(root.left), NodeMaxHeight(root.right))

# get min depth of whole tree
def minDepth(root):
        if not root: return 0
        left = minDepth(root.left)
        right = minDepth(root.right)
        #think skew tree
        if not left:
            return right + 1
        elif not right:
            return left + 1
        else:
            return 1 + min(left, right)
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print(isBalanced(root))
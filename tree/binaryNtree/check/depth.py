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
    #dfs
        # if not root: return 0
        
        # # think about skew 
        # if not root.left:
        #     return 1 + minDepth(root.right)
        # if not root.right:
        #     return 1 + minDepth(root.left)
        # return 1 + min(minDepth(root.left), minDepth(root.right))
    #bfs
        if not root: return 0
        
        #bfs 
        q = deque([root])
        level = 1 # root counted
        
        while len(q) > 0:
            size = len(q)
            index = 0
            while index < size:
                top = q.popleft()
                if not top.left and not top.right: # this is leaf
                    return level
                else:
                    if top.left:
                        q.append(top.left)
                    if top.right:
                        q.append(top.right)
                index+= 1
            level += 1
        return 0
    
root = TreeNode(1)
root.left = TreeNode(20)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print(isBalanced(root))
print(minDepth((root)))
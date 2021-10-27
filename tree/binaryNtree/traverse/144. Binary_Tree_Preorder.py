# 144. Binary Tree Preorder Traversal
# recusion
def preorderTraversal(self, root):
        res= []
        self.preorder(root, res)
        return res
        
def preorder(self, root, res):
        if not root: return 
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

# iteration
'''
    LOGIC:
    dfs traversal use stack
    stack store node,each time pop and find its children
    TIME COMPLEXITY:
    traverse all nodes and store into result array
    T:O(n) 
    S:O(n)store stack, EXCLUDE result
'''
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        stack = [root]
        res = []
        while len(stack) > 0:
            top = stack.pop()
            res.append(top.val)
            
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return res
        
#589. N-ary Tree Preorder Traversal
 def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        def dfs(root):
            if not root: return
            self.res.append(root.val)
            if root.children:   
                for i in range(len(root.children)):
                    dfs(root.children[i])
        dfs(root)
        return self.res

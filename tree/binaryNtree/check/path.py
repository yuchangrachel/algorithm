'''
543. Diameter of Binary Tree
REFER:
https://www.youtube.com/watch?v=3vZV-6qPDmE
LOGIC:
1.diameter is longest path between two node. path may not pass through root
2.how to diameter: dfs left and right subtree mark max
3.helper() is calculating max depth from root to leaf
'''
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = [0] * 1 # longest path between two nodes
        max_depth = self.helper(root, self.diameter) # mark each node's depth
        return self.diameter[0]
    
def helper (self, root, diameter):
        if not root: return 0
        # dfs down to leaf
        left = self.helper(root.left, diameter)
        right = self.helper(root.right, diameter)
        diameter[0] = max(diameter[0], left+right)
        # return back to parent
        return max(left, right) + 1 #1 mean one edge counted  # find maximum depth

def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        '''
        How to find two nodes whose path are longest, may not pass through root, but difinitely reach two leaves.
        dfs go to bottom and go up count depth,compare maxdepth(left, right) + 1
        update diameter(left+right)
        '''
        if not root: return 0
        self.diameter = 0
        def dfs(root):
            if not root: return 0
            
            lefter = dfs(root.left)
            righter = dfs(root.right)
            
            self.diameter = max(self.diameter, lefter+righter)
            
            #maxdepth
            return 1 + max(lefter, righter)
            
            
        dfs(root)
        return self.diameter
        
# 257 Binary Tree Paths
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        
        self.res = []
        
        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                self.res.append(path)
                return            
            dfs(root.left, path + '->')
            dfs(root.right, path + '->')
                
        
        dfs(root, "")
        return self.res
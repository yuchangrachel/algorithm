'''
543. Diameter of Binary Tree
REFER:
https://www.youtube.com/watch?v=3vZV-6qPDmE
LOGIC:
1.diameter is longest path between two node. path may not pass through root
2.how to diameter: dfs left and right subtree mark max
3.helper() is calculating max depth from root to leaf
'''
class Solution:
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
        
    
# 104.Maximum Depth of Binary Tree
'''
    find longest path from root to leaves
    dfs traversal, recursion go to bottom, then bottom-top call
'''
def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
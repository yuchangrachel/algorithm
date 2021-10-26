'''
    Travesal tree from top to leaves. Do DFS(preorder) from bottom to top recursion
    TIME:O(n) S(h)
'''
def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # put total in argument of recursion, need keep updating(like global var)
        return self.dfs(root, 0)
    
def dfs(self, root, total):
        if not root: return 0
        curTotal = total * 10 + root.val
        
        #check if root is leaf
        if not root.left and not root.right:
            return curTotal
        
        # otherwise check left and right subree
        return self.dfs(root.left, curTotal) + self.dfs(root.right, curTotal)

# 112. Path Sum
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:   
        if not root: return False
        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
# 404.Sum of left leaves
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if root.left and not root.left.left and not root.left.right: 
            #it is left leaf
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) #no leaves
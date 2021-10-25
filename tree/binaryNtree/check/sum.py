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
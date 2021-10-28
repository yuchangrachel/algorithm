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
    
#938. Range Sum of BST 
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        traverse tree's all nodes and check if in this range, if yes add to sum
        '''
        self.sum = 0
        def preorder(root):
            if not root: return
            if root.val >= low and root.val <= high:
                self.sum += root.val
            
            # use bst characteristics improve code
            if root.val > high:
                preorder(root.left)
            elif root.val < low:
                preorder(root.right)
            else:
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return self.sum
    
#1022. Sum of Root To Leaf Binary Numbers  
def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # traverse from root to leaf, Each path is binary string converting to 10-base and sum up all these 10-base
        def dfs(root, s):
            total = 0
            if not root:
                return total

            if not root.left and not root.right:
                total += int(s + str(root.val), 2) # convert binary -> int

            if root.left:
                total += dfs(root.left, s + str(root.val))
            if root.right:
                total += dfs(root.right, s + str(root.val))
                
            return total
            
        return dfs(root, "")
    
    #OR
    '''
        def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # traverse from root to leaf, Each path is binary string converting to 10-base and sum up all these 10-base
        self.total = 0
        def dfs(root, s):
            if not root: return 

            if not root.left and not root.right:
                self.total += int(s + str(root.val), 2) # convert binary -> int
                return

            dfs(root.left, s + str(root.val))
            dfs(root.right, s + str(root.val))
            
        dfs(root, "")
        return self.total
        '''
# 108. Convert Sorted Array to Binary Search Tree
'''
    TOPIC:convert sorted array to BST(inorder) Build Tree(TEMPLATE: root.left..., root.right ..., return root)
    STEP:
    1.find nums[mid] is root,create newTreeNode as root
    2.rec(nums[:mid]) and rec(nums[:mid])
'''
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums or len(nums) == 0: return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
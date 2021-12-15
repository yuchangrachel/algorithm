'''
    TOPIC:Find node, delete it and update BST
    STEP:traverse tree, reassign
    1.USE BST search correct position
    1.If deleteNode.left and right if one null, another replace
    2.If left and right both not null, maintain same left tree, find leftmost(smallest) on right subtree, replace deletenode's val NOT NODE SINCE HAVE LEFT SUBTREE!!!, and also remember delete
    smallest one also(since already used)
    3.Both left and right null, root = null
         7
        / \
       4   8
     /   \   
    2     6
     \   /
      3 5
      delete4, 5 replace
'''
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        #BST
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # find deletenode
            #left or right either null
            if not root.left and root.right:
                root = root.right
            elif not root.right and root.left:
                root = root.left
            elif root.left and root.right: #both left and right not null
                # find leftmost in right subtree, left subtree maintain same
                left_temp = root.left
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val 
                #used temp, so delete original smallest, that is on right subtree, need delete is temp.val(update key)
                root.right = self.deleteNode(root.right, temp.val)
            else: #both null
                root = None
        return root # finally return top root of tree
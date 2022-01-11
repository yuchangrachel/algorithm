'''
    TOPIC:N-ary tree preorder recursion&iterative
    STEP recursion:self.helper(child,res)
    STEP iterative:stack push children from len to 0
'''
def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while len(stack)>0:
            pop = stack.pop()
            res.append(pop.val)
            for i in range(len(pop.children)-1, -1, -1):
                stack.append(pop.children[i])
        return res
        
    
# RECURSION    
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root: return []
#         res = []
#         self.helper(root, res)
#         return res
    
#     def helper(self, root, res):
#         if not root: return
        
#         res.append(root.val)
#         for child in root.children:
#             self.helper(child, res)
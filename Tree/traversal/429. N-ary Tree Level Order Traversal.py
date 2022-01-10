'''
    TOPIC:N-aray Tree BFS
    STEP:iterative(BFS) template BFS
    STEP:recursion
    1.create helper method(root,level) for traversal
    2.recursion-base:leve=len(res) add new inner[root] else res[level]apppend root. if child, do helper(child, level+1)
    '''
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        self.preorder(root, 0, res)
        return res
    
    def preorder(self,root, level, res):
        if not root: return
        if level == len(res):
            res.append([root.val]) #create new inner
        else:
            res[level].append(root.val)
        
        for child in root.children:
            self.preorder(child, level+1, res)
        
# BFS:        
#         q = deque()
#         q.append(root)
#         while len(q) > 0:
#             index = 0
#             size = len(q)
#             inner = []
#             while index < size:
#                 pop = q.popleft()
#                 inner.append(pop.val)
#                 if pop.children:
#                     for child in pop.children:
#                         q.append(child)
#                 index += 1
#             res.append(inner)
        
#         return res
                    
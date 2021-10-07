"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        # create hashmap store{oldnode:newnode} both nodes has .next and .random
        dic = {None:None}
        
        # use new pointer tracking head
        cur = head
        
        # first pass, create mapping old-> new node
        while cur:
            dic[cur] = Node(cur.val)      
            cur = cur.next
        
        # second pass, set props for newnode
        cur = head
        while cur:
            newNode = dic[cur]
            newNode.next = dic[cur.next]
            newNode.random = dic[cur.random] 
            cur = cur.next
                   
        return dic[head]
    

#138. Copy List with Random Pointer
def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        LOGIC: deep copy of linkedlist
        Since a node can be referenced from multiple nodes due to the random pointers, avoid making multiple copies of the same node. 
        use mapping:oldnode -> newnode
        first store dic[old] = newnode
        second loop round add .next and .random
        '''
        
        if not head: return None
        # need initial with type
        dic = {None:None}
        
        cur = head
        # first loop create old->new mapping, and traverse old linkedlist, storing all nodes next relationship
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        
        #second loop: now old already in map, find it, .next and .random will copy to newNode
        cur = head
        while cur:
            newNode = dic[cur]
            newNode.next = dic[cur.next]
            newNode.random = dic[cur.random]
            cur = cur.next
        
        return dic[head]
        
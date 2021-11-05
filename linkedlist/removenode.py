#19.Remove nth node from back of linkedlist
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        LOGIC
        Remove nth from back. THIS IS CHAIN OF LINKEDLIST
        1.one loop get len
        2.find prev before break, len-n=prev pos
        3.relink after delete
        '''
        if not head: return None
        
        length = self.getLen(head)
        prev = None
        cur = head
        prevpos = length - n 
        index = 0
        
        # when traversing cur, find prev position
        while cur:
            if index == prevpos:
                break #find prev
            prev = cur
            cur = cur.next
            index += 1
        
        #corner case check if delete head
        if not prev:
            head = cur.next # change head
        else:
            prev.next = cur.next
        
        return head
        
    
def getLen(self, head):
        cur = head
        len = 0
        while cur:
            cur = cur.next
            len += 1
        
        return len
        
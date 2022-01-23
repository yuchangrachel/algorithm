'''
    TOPIC:Dont think lomuto partition algorithm for array, this is not stable, not works in linkedlist
    STEP:
    1.create new linkedlist store all nodes smaller than x. then merge original 
    '''
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        small = smallhead = ListNode(-1)
        l2 = h2 = ListNode(-1)

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        
        #combine all linkedlists
        #avoid cycle, need remove latter part tail.next
        l2.next = None
        small.next = h2.next
        return smallhead.next
        
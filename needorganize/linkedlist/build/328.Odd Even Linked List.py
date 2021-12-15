def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TOPIC: REORDER LIST.create two TwoList:even indices, odd indices.index starting from index-1.
        #STEP:
        #1.use index keep tracking who at odd index and at even index respectively, divide two linkedlist
        #2.combine with two linkedlist
        if not head or not head.next: return head

        #init: None
        #create two new linkedlists
        oddHead = ListNode(-1)
        evenHead = ListNode(-1)
        #to reconnect so need tail
        oddEnd = oddHead
        evenEnd = evenHead
        index = 1
        cur=head
     
        while cur:
            if index % 2 != 0: #odd index
                oddEnd.next = cur
                oddEnd = oddEnd.next
            else: #even index
                evenEnd.next = cur
                evenEnd = evenEnd.next
            index += 1
            cur = cur.next
        
        oddEnd.next = evenHead.next
        evenEnd.next = None
        
        return oddHead.next
        
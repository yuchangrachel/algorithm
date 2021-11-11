def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        TOPIC: two pointer
        slow =head
        fast = head.next
        swap slow with fast, cur pointer will arrive fast.next
        '''
        if not head or head.next == None: return head #no need swap
        
        #when swap will change head, so need dummy
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            self.swap(cur)
            cur = cur.next.next #skip pair
        
        return dummy.next
            
    def swap(self, prev):
        temp = prev.next #store 1
        prev.next = temp.next # break 1,2 let prev-> 2
        temp.next = temp.next.next#1 -> rest(skip2)
        prev.next.next = temp # go back first link , link 2->1
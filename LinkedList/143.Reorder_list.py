'''
    TOPIC:L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    STEP:MIDDLE, REVERSE, MERGE
    1.keep head, step only half
    2.find middle, seperate first part(include middle), second part;second part has longer length.
    3.reverse second part, then let second merge into first
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return 
        
        middle = self.findMiddle(head)
        secondHead = self.reverse(middle.next)
        middle.next = None
        self.merge(head, secondHead)

    
    def reverse(self,head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp
        return prev
        
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, h1, h2):
        dummy = ListNode(-1)
        dummy.next = h1
        index = 0
        while h1 and h2: #list2 longer
            if index % 2 == 0:
                dummy.next = h1
                h1 = h1.next
            else:
                dummy.next = h2
                h2 = h2.next
            index += 1
            dummy = dummy.next
        
        if h1:
            dummy.next = h1
        if h2:
            dummy.next = h2
        

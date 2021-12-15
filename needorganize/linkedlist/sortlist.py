'''
    LOGIC: SORT
    for list can do merge sort O(nlogn)
    1.find middle, seprate two lists and do recursion from top to bottom, get single ele
    2.merge two lists when compare single element from list1 and list2
    
''' 
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        # find middle
        prevslow = None
        fast = slow = head
        while fast and fast.next:
            prevslow = slow
            slow = slow.next
            fast = fast.next.next
            
        # break two lists
        prevslow.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
        
def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        cur = dummy
        
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
                
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
                
        return dummy.next
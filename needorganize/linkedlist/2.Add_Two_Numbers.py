def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # corner case
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        
        # build new linkedlist
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            cur.next = ListNode(temp%10)
            carry = temp // 10
            cur = cur.next
        
        if carry != 0:
            cur.next = ListNode(1)
        
        return dummy.next
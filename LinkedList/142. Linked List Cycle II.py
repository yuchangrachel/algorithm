'''
    TOPIC:SLOW FAST TWO POINTER:find start point of cycle
    STEP:fast will earlier enter loop than slow, so when fast meet slow at first, fast run twice in loop. 
    after meet first, slow and fast will try same speed see if meet again. if meet again, that is start point of cycle
'''
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # meet first time
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        
        p1 = l1
        p2 = l2
        
        # need build linkedlist, so need dummy
        dummy = ListNode(-2)
        cur = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = ListNode(p1.val)
                p1 = p1.next
            else:
                cur.next = ListNode(p2.val)
                p2 = p2.next
            cur = cur.next
        
        if p1:
            cur.next = p1
        
        if p2:
            cur.next = p2

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # middle, reverse second par, merge them with %
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        middle = self.middle(head)
        reversed = self.reverse(middle.next)
        middle.next = None # break two parts
        self.merge(head, reversed)
        
    def middle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def merge(self, head, head2):
        # still modify head, but create dummy tracking whole linkedlist
        dummy = ListNode(-1)
        index = 0
        dummy.next = head
        #second part shorter
        while head2:
            if index % 2 == 0:
                dummy.next = head
                head = head.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index+=1
        if head: dummy.next = head
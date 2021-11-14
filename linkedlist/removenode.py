# 203. Remove Linked List Elements
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        TOPIC: Remove all nodes whose val == val
        HOW:
        maybe remove head base on val, so need create dummy
        '''
        if not head: return None
        
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy # cur as prev, prev link to .next.next
        
        while cur.next:
            if cur.next.val == val:
                # need remove
                cur.next = cur.next.next
            else:
                cur = cur.next  
        
        return dummy.next

#237. Delete Node in a Linked List
def deleteNode(self, node):
        """
        node is needed to be deleted
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node: return
        
        if node.next:
            node.val = node.next.val # store next val into cur, then (node.next)node can skip
            node.next = node.next.next # since node.next is skipped

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
            if index == prevpos: # MUST IN THIS LINE, check first
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
        
#83. Remove Duplicates from Sorted List
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        TOPIC: remove extra duplicate from linkedlist
        HOW:
        Definitely won't remove head
        Compare with next neighbor
        '''
        if not head: return None
        
        cur = head #no need prev since head always keep 
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.next.next # store
                cur.next = temp # cur pointer wont't move forward since maybe more 1 duplicate
            else:
                cur = cur.next
        return head

'''     
82. Remove Duplicates from Sorted List II
'''
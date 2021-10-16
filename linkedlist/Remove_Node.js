/*
19.
1.Get length of linkedlist
2. len-n is prev pos. then cur then cur.next.
*/
var removeNthFromEnd = function (head, n) {
  if (head == null || n == 0) return head; //nothing need to move
  let len = getLen(head);
  let prev_pos = len - n; //index starting from 0
  let index = 0;
  let prev = null;
  let cur = head;
  //find prev position
  while (cur) {
    if (index == prev_pos) break; //find pre
    prev = cur;
    cur = cur.next;
    index++;
  }
  if (prev) {
    cur = prev.next;
    prev.next = cur.next;
  } else {
    //if remove head
    head = cur.next;
  }

  return head;
};

const getLen = function (head) {
  let len = 0;
  let cur = head;
  while (cur) {
    cur = cur.next;
    len++;
  }
  return len;
};

/*
203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        
        # return new head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy # dont need prev, since need to updat prev as well, so only need one variable
        
        while cur.next:
            if cur.next.val == val:
                # need delete
                cur.next = cur.next.next
                # may have elements
            else: 
                cur = cur.next
        
        return dummy.next
*/

/*
83. Remove Duplicates from Sorted List
# How to compare with neighbors?
# No need dummy since no build linkedlist, no matter include duplicate or not, head still there
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp =cur.next.next
                cur.next = temp # still this cur. 
            else:
                cur = cur.next
        
        
        return head
        
*/

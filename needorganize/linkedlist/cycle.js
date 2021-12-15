//141.Linkedlist cycle
//determine linkedlist has cycle or not, use fast and slow pointer. If has cycle, finally will envolve cycle. So both of pointers cannot be null. means fast may run cycle twice but slow just run. and then meet each other.
var hasCycle = function (head) {
  if (head == null) return false;

  let slow = head;
  let fast = head;
  while (slow && fast && fast.next) {
    //if statement need handle all situations which occur inside of statement
    fast = fast.next.next;
    slow = slow.next;
    if (fast == slow) return true;
  }
  return false;
};

//142.Linked List Cycle II
//fast is 2times speed/distance than slow
//after first time meet, slow will go to head, fast will keep moving from meet point, they will meet in start of cycle
var detectCycle = function (head) {
  if (head == null) return head;

  let slow = head;
  let fast = head;

  //first meet
  while (slow && fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow == fast) {
      //meet first time
      let slow2 = head;
      while (slow2 != fast) {
        //dont use slow2&&fast since maybe first one may be start of cycle
        slow2 = slow2.next;
        fast = fast.next;
      }
      return slow2;
    }
  }
  return null;
};

//160. Intersection of Two Linked Lists
'''
    OPIC:Intersection of Two LinkedList => CYCLE logic
    LOGIC:
    1.This is linkedlist Intersection, both use .next, if reach end, then switch into opposite side's head
    2.Maybe go to two rounds, then they meet, sumiliar two pointer(fast&slower)
    3.No intersection: if go through many rounds, both arrive null(after tail)
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        curA = headA
        curB = headB
        
        while curA != curB:
            if not curA:
                curA = headB
            else:
                curA = curA.next
            if not curB:
                curB = headA
            else:
                curB = curB.next
        return curA

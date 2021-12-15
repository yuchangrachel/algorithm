//206. Reverse Linked List
var reverseList = function (head) {
  //corner case
  if (head === null || head.next === null) return head;

  let cur = head;
  let prev = null;

  //iterate list
  while (cur != null) {
    //before break store latter part
    let temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp; //moving similiar cur = cur.next
  }
  return prev;
};

/*
92.Reverse linkedlist
Input: (head = [1, 2, 3, 4, 5]), (left = 2), (right = 4);
Output: [1, 4, 3, 2, 5];
*/
var reverseBetween = function (head, left, right) {
  //corner case
  if (head == null || left > right) return null;

  //three parts: beforewindow + reversewindow + latter, return rebuilt reversedlist
  let dummy = new ListNode(-1);
  dummy.next = head;
  let cur = dummy.next;
  let prev = dummy; //not null there, need to be node in new list, not random

  //find before window point
  for (let i = 1; i < left; i++) {
    prev = prev.next;
  }
  cur = prev.next; //starting of window

  //reverse part
  //store new node wont affect other parts
  let prevNode = null;
  for (let i = left; i <= right; i++) {
    //reverseNo=right-left+1
    let temp = cur.next;
    cur.next = prevNode;
    prevNode = cur;
    cur = temp;
  }

  //connect three parts
  prev.next.next = cur;
  prev.next = prevNode;

  return dummy.next;
};

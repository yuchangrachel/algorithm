/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
  if (head == null) return head;
  //reverse some part, connect it with prev part and latter part, mean rebuild linkedlist
  let dummy = new ListNode(-1);
  let prev = dummy;
  dummy.next = head;

  //find prev before window for reverse, prev for connecting to latter parts
  for (let i = 1; i < left; i++) {
    prev = prev.next;
  }
  let cur = prev.next; //starting window

  //reverse window
  let node = null; //see as new whole linkedlist
  //window size is right-left+1 node numbers
  for (let i = 0; i < right - left + 1; i++) {
    let temp = cur.next;
    cur.next = node;
    node = cur;
    cur = temp;
  }

  //connect three parts
  prev.next.next = cur; //first connect latter part
  prev.next = node;

  return dummy.next;
};

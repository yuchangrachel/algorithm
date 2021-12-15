// 234. Palindrome Linked List
var isPalindrome = function (head) {
  //TOPIC: find middle, reverse(latter part), compare two list (former and latter) if same
  //Think it is odd length or even length

  if (head === null) return true;
  let len = getLen(head);
  let mid = middle(head);
  let temp = null; //store head of latter part
  //check even or odd length
  if (len % 2 == 0) {
    temp = mid.next;
    mid.next = null; //break
  } else {
    temp = mid.next;
    mid = null;
  }
  let latter = reverse(temp);
  //compare first and latter part
  let first = head;
  let second = latter;
  while (first != null && second != null) {
    if (first.val != second.val) return false;
    else {
      first = first.next;
      second = second.next;
    }
  }
  return true;
};

const reverse = function (node) {
  let prev = null;
  let cur = node;
  while (cur != null) {
    let temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }
  return prev;
};
const middle = function (node) {
  let slow = node;
  let fast = node;

  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
};
const getLen = function (node) {
  let len = 0;
  let cur = node;
  while (cur != null) {
    cur = cur.next;
    len++;
  }
  return len;
};

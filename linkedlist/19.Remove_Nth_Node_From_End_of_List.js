/*
1.Get length of linkedlist
2. len-n is prev pos. then cur then cur.next.
*/
var removeNthFromEnd = function(head, n) {
    if (head == null || n == 0) return head //nothing need to move
    let len = getLen(head)
    let prev_pos = len - n //index starting from 0
    let index = 0
    let prev = null
    let cur = head
    //find prev position
    while (cur){
        if (index == prev_pos) break  //find pre
        prev = cur
        cur = cur.next
        index++
    }
    if (prev){
        cur = prev.next
        prev.next = cur.next
    }  else{
        //if remove head
        head = cur.next        
    }
    
    return head
};

const getLen = function(head){
    let len = 0
    let cur = head
    while (cur){
        cur = cur.next
        len++
    }
    return len
}
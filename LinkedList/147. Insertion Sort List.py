#147. Insertion Sort List
'''
    TOPIC:Insertsort(sorted part + unsorted part)
    STEP:
    1.When head may change, create dummy
    2.create variable:dummy,prev(head),cur(head),if find smaller, then go back while to find spot to swap

'''
def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(-1)
        prev = head #the last one in sorted part
        cur = head #cur pointer
        dummy.next = prev
        while cur:
            if prev.val <= cur.val:
                #sorted, no need swap
                prev = cur 
                cur = cur.next
            else:
                #need move cur out, before that, store cur.next
                prev.next = cur.next
                headTemp = dummy #go back to begin
                while headTemp.next and headTemp.next.val < cur.val:
                    headTemp = headTemp.next
                #insert before this headTenp.next
                cur.next = headTemp.next
                headTemp.next = cur #add cur
                cur = prev.next#need go back searching pointer
        return dummy.next
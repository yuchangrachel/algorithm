'''
TOPIC:merge2sortedlists extend. 
STEP:divide and conquer, each time make lists length shorter, until only one list
1.each time pair merge, add to temp, then let lists = temp
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0: return None
        while len(lists) > 1:
            temp = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                temp.append(self.merge2Lists(l1,l2))
            lists = temp
            
        return lists[0]
                
        
        
    def merge2Lists(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
                
                
        
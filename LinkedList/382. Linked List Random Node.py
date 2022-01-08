'''
    TOPIC:linkedlist traverse + randint(start,stop+1)
    STEP:getLen(), randint(0, len-1)
'''
    def __init__(self, head: Optional[ListNode]):
        # get list and count length(fixed)
        self.length = 0
        self.head = head
        cur = head
        while cur:
            cur = cur.next
            self.length += 1


    def getRandom(self) -> int:
        index = random.randint(0, self.length-1)
        cur = self.head
        
        while index > 0:
            cur = cur.next
            index -= 1
            
        return cur.val 
        
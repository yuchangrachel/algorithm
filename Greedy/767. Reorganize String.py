'''
    TOPIC:similiar to TASK SCHEDULER.but this now display res
    STEP:
    1.create hashmap{char:freq}, also create maxheap, sort base on mostfreq. if counter more than half, trim 
    2.while len(q) >= 2: each time pop most freq 2 pair; if v -1 > 0: push again
    3.res.append(last one)
'''
import collections
import heapq
def reorganizeString(s):
        mapping = collections.Counter(s)
        maxheap = []
        res = ""
        for k, v in mapping.items():
            if v > ((len(s) + 1) // 2): 
                return "" #trim
            heapq.heappush(maxheap, (-v, k))

        while len(maxheap) >= 2:
            pop1= heapq.heappop(maxheap)
            pop2 = heapq.heappop(maxheap)
            res += pop1[1] + pop2[1]

            if (-pop1[0]-1) > 0:
                #push back
                heapq.heappush(maxheap, (-(-pop1[0]-1), pop1[1]))
   
            if (-pop2[0]-1) > 0:
                #push back
                heapq.heappush(maxheap, (-(-pop2[0]-1), pop2[1]))

        #even mapping size is not even, leave one 
        if len(maxheap) > 0:
            res += heapq.heappop(maxheap)[1]
            
        return res
        
print(reorganizeString("baaba"))  #ababa
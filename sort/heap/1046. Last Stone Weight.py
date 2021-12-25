'''
    TOPIC:find biggest two numbers -> heap
    STEP:
    1.create maxheap store stones array
    2.handle negative
'''
import heapq
import math
def lastStoneWeight(stones):
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        print(maxheap)
        while len(maxheap) >= 2:
            firstBig = heapq.heappop(maxheap)
            secondBig = heapq.heappop(maxheap)
            if firstBig != secondBig:
                diff = -firstBig - (-secondBig)
                heapq.heappush(maxheap, -diff)
        return 0 if len(maxheap) == 0 else -heapq.heappop(maxheap)
print(lastStoneWeight([2,7,4,1,8,1]))

print(math.ceil(4/4))
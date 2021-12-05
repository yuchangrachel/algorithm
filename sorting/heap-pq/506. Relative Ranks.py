import heapq
def findRelativeRanks(score):
        #TOPIC:String represent,first max, second max, third max,..
        #STEP:
        #1.CREATE minheap increasing order, first pass for store (point, index) into heap
        #2.COMPARE second loop, compare original array
        if not score or len(score) == 0: return []
        
        heap = []
        res =[""] * len(score)
        for i, score in enumerate(score):
            heapq.heappush(heap, (-score, i))

        count = 0
        while heap:
            score, i = heapq.heappop(heap)
            count += 1
            if count == 1:
                res[i] = "Gold Medal"
            elif count == 2:
                res[i] = "Silver Medal"
            elif count == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(count)
        
        return res
print(findRelativeRanks([10,3,8,9,4]))
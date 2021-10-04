# Python has built in method for heap. default is minheap.

# 215
# heapsort O(nlogk)
# When find kth largest ele, minheap, add ele into heap each time, heap will sort, pop smallest, that is why use minheap
import heapq
def findKthLargest(nums,k):
    if nums is None or len(nums) == 0 or k > len(nums): return -1
        
    # create min pq initial with k size
    pq = nums[0:k]
    heapq.heapify(pq)  #lgk
        
    for x in nums[k:]:
        heapq.heappush(pq, x)
        heapq.heappop(pq)

    #or SLOWER
    pq = [] 
    for x in nums:
        heapq.heappush(pq, x)
        if len(pq) > k:
            heapq.heappop(pq)

    return pq[0]
        
print(findKthLargest([3,2,1,5,6,4], 2))

#1985
def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if nums is None or len(nums) == 0 or len(nums) < k: return ""
        
        pq = []
        for x in nums:
            heapq.heappush(pq, int(x))
            if len(pq) > k:
                heapq.heappop(pq)
        
        return str(pq[0])
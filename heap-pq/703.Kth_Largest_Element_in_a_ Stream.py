class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # add property, so method can use it create minheap, k size
        # 1WAY
        # self.minheap = []
        # self.k =k
        # for x in nums:
        #     heappush(self.minheap, x)
        #     if self.k < len(self.minheap):
        #         heappop(self.minheap)
        
        # 2WAY faster
        self.minheap = nums
        self.k = k
        heapify(self.minheap)
        while len(self.minheap) > k:
            heappop(self.minheap)
    
    
    def add(self, val: int) -> int:
        heappush(self.minheap, val)
        if self.k < len(self.minheap):
            heappop(self.minheap)
        return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
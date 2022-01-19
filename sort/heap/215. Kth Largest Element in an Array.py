import heapq
class Solution:
    '''
    TOPIC:Kth largest
    1WAY:brute force O(nlogn) sorted, find find last k index 
    2WAY:MINHEAP O(nlogn) build O(n) heapify(nlogn) =>combine as heapsort
    3WAY:randomized QUICKSELECT-PARTITION average O(n): http://yuandali.me/2017/01/17/Two-Pointers/
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pIndex = random.randint(left, right)
            new_pIndex = self.LomutoPartition(nums, left, right, pIndex)
            if new_pIndex == k - 1:
                # find it 
                return nums[new_pIndex]
            elif new_pIndex > k - 1:
                right = new_pIndex - 1
            else:
                left = new_pIndex + 1
        
        
        
    def LomutoPartition(self, nums, l, r, pIndex): # larger | pivot | smaller
        pivot = nums[pIndex]
        low = l
        nums[pIndex], nums[r] = nums[r], nums[pIndex]
        for i in range(l, r):
            if nums[i] > pivot:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
        
        
        
# 1WAY:MINHEAP       
#         heap = []
#         for n in nums:
#             heappush(heap, n)
#             if len(heap) > k:
#                 heappop(heap)
        
#         return heappop(heap)  OR heap[0]
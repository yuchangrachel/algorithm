# find kth smallest ele, use max heap o(nlogk), push first, if more than size, pop largest in head of heap
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if matrix is None or matrix[0] is None or len(matrix) == 0 or len(matrix[0]) == 0 or k > len(matrix)*len(matrix[0]): return -1 # no num
        
        pq = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(pq, -matrix[i][j]) #maxheap change val ->-val
                if len(pq) > k:
                    heapq.heappop(pq)
        return -pq[0]
                    
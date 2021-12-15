# K closest pointers to (0,0), think about maxHeap
    # heap sort based on sqr
    # O(nlogk)
    # sort built in OR heapsort
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or len(points) == 0: return []
        
        points = sorted(points, key=lambda point: point[0]** 2 + point[1] ** 2)
        k_closet = heapq.nsmallest(k, points, key=lambda point: point[0]** 2 + point[1] ** 2)
        return points[:k]
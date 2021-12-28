import heapq
'''
    TOPIC:k smallest distance, return the pairs
    STEP:
    1.sort distance, but return pair, so reassign points(distance, point) array
    2.heapify reassigned points array(minheap,increasing order) return first k pairs
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(point[1]*point[1] + point[0] *point[0], point) for point in points]
        heapq.heapify(points)
        return [heapq.heappop(points)[1] for _ in range(k)]
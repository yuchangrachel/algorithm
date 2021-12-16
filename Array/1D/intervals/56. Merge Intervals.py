#56. Merge Intervals
'''
    TOPIC:Intervals
    STEP:how to merge many intervals: first add interval(array of object), so can update later
'''
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0: return []
        
        res = []
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        res.append(prev)
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1]) 
            else:
                #new interval
                prev = cur
                res.append(prev)
        return res
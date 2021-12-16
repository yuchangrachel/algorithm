#56. Merge Intervals
'''
    TOPIC:Intervals
    STEP:how to merge many intervals: first add interval(array of object), so can update later
'''
def merge(intervals):
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

#435. Non-overlapping Intervals
'''
    TOPIC:remove overlap interval at minimum step(GREEDY)
    STEP:sort [0], if cur[0] < flag[1], count++, flag=min(flag[1], cur[1]), greedy get more possible nonoverlap
'''
def eraseOverlapIntervals(intervals):
        if not intervals or len(intervals) == 0: return 0
        res = 0
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] < prev[1]:
                res += 1
                prev[1] = min(cur[1], prev[1])
            else:
                # update prev
                prev = cur
        return res
print(eraseOverlapIntervals(
[[1,100],[11,22],[1,11],[2,12]]))
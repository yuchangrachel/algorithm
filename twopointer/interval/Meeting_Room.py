'''
1094. Car Pooling
1WAY
    LOGIC: TO(nlogn)
    Overlap Interval
    1.sort starttime, then sort endtime Like meeting room problem
'''
def carPooling(self, trips, capacity):
        if not trips or len(trips) == 0: return False

        start_time = sorted(trips, key=lambda x:x[1])
        end_time = sorted(start_time, key=lambda x:x[2])
        
        people = 0
        start = end = 0
        while start < len(trips):
            if start_time[start][1] < end_time[end][2]: #before end point, start point still having passangers
                people += start_time[start][0]
            else:
                people -= end_time[end][0] # end point people drop off
                end += 1
                continue # must have!
            start+=1
            if people > capacity: return False
        
        return True
'''
2WAY
    LOGIC:
    Overlap Interval
    1.store (start/end, get/drop) tuple in list, sorted
'''
def carPooling(self, trips, capacity):
        if not trips or len(trips) == 0: return False
        
        res = [] # store start/end getpeople/dropoff
        for n, start, end in trips:
            res.append((start, n))
            res.append((end, -n))
            res.sort()
        
        people = 0
        for trip in res:
            people += trip[1] #accumulate sum
            if people > capacity: return False
        return True

print(carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]], 12)) #false
print(carPooling([[1,1,4],[9,4,9],[9,1,9],[2,3,5],[4,1,5],[10,4,5]],33))#false
print(carPooling([[2,1,5],[3,3,7]], 5))
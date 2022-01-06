'''
    TOPIC:Interval sort. But now curpass will keep change, so store curpass+from/curpass-to in res array
    STEP:
    1.create res, traverse trips, store [from,n] and [to,-n]
    2.sort res, sort res[1] first handle pick/drop amount, let small amount finish as early as possible. then sort res[0] see time
'''
def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = []
        for trip in trips:
            res.append([trip[1], trip[0]])
            res.append([trip[2], trip[0]*(-1)])
        res.sort(key=lambda x:x[1])
        res.sort(key=lambda x:x[0])
        
        total = 0
        for i in range(len(res)):
            total += res[i][1]
            if total > capacity:
                return False
        return True
        
'''
    TOPIC:Overlap Interval Question Always THINK endclose.
    STEP:subarray[0,1] mean size of ballon.see how to let arrows can shoot as many as ballons
    1.sort [1]then [0], 
    2.flag will update min endclose because some ballon only at certain narrow space
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        points.sort(key=lambda x:x[0])
        flag = points[0]
        res = 1
        for i in range(1, len(points)):
            cur = points[i]
            if cur[0] <= flag[1]: #overlap
                flag[1] =  min(flag[1], cur[1])
            else: #nonoverlap
                res += 1
                flag = cur
        
        return res
                
                
print(findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) # 2
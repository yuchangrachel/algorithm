'''
56. Merge Intervals
    LOGIC: interval+sort
    HOW:
    sort start only, since end will use max compare later
    set prev as flag, traverse compare to prev, not compare with neighbor since interval may overlap more lists, keep updating prev
'''
def merge(intervals):
        if not intervals or len(intervals) == 0: return []

        intervals = sorted(intervals, key=lambda x:x[0])
        prev = [intervals[0][0], intervals[0][1]]
        res = [prev]
        
        for i in range(1, len(intervals),1):
            if intervals[i][0] <= prev[1]:
                #overlap prev's end will extend
                #prev[1] must compare to intervals[i][1], see who is bigger, update prev(prev is mutable object)
                prev[1] = max(prev[1], intervals[i][1])
            else:
                #update prev
                prev = [intervals[i][0], intervals[i][1]]
                res.append(prev) 
        return res
print(merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])) #[[1,3],[4,7]]

#SAME SOLUTION
# 57. Insert Interval
# var insert = function(intervals, newInterval) {
#     if (intervals === null && newInterval === null) return []
    
#     const res = []
    
#     intervals.push(newInterval)
    
#     intervals.sort((a,b) => a[0]-b[0])
    
#     let prev = [intervals[0][0], intervals[0][1]]
#     res.push(prev)
    
#     for (let i = 1; i < intervals.length; i++){
#         let cur = intervals[i]
#         if (cur[0] <= prev[1]){
#             prev[1] = Math.max(prev[1], cur[1])
#         }
#         else{
#             //update prev
#             prev = cur
#             res.push(prev)
#         }
#     }
#     return res
# };

# 986. Interval List Intersections
'''
var intervalIntersection = function(firstList, secondList) {
    //TOPIC: Two List interval TWO POINTER
    //HOW: think cases, if no intervals, moveforward; else interval[max(first), min(second)], when merge need move forward
    if (firstList == null || secondList == null) return []
    
    const res = []
    let i = 0
    let j = 0
    while (i < firstList.length && j < secondList.length){
        if (firstList[i][0] > secondList[j][1]) //no interval move on
            j+=1
        
        else if (secondList[j][0] > firstList[i][1]){ //no interval move on
            i+=1
        }
        else{
            //has interval
            let interval = [Math.max(firstList[i][0], secondList[j][0]), Math.min(firstList[i][1], secondList[j][1])]
            res.push(interval)
            //move on
            //see whose end is bigger
            if (firstList[i][1] > secondList[j][1])  j++
            else if (firstList[i][1] < secondList[j][1]) i++
            else{
                //same length
                i++
                j++
            }
        }
    }
    return res
};
'''
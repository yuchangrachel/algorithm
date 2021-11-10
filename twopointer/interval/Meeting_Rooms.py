'''
252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
determine if a person could attend all meetings.(0,8) and (8, 10) not conflict
Example 1:
Input:
[[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input:[[7,10],[2,4]]
Output:true
'''
'''
TOPIC:interval, two pointer, sort
HOW:sort starttime only, dont need sort endtime since[5,10][5,8], impossible attend all meetings. if cur meeting starttime is earlier than previous meeting endtime, cannot attend all meetings
'''
def canAttendMeetings1(intervals):
    if not intervals or len(intervals) == 0: return False

    intervals.sort(key=lambda x:x[0])
    
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

print(canAttendMeetings1([[7,10],[2,4]]))

'''
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
find the minimum number of conference rooms required.
输入: intervals = [(0,30),(5,10),(15,20)]
输出: 2
解释:
需要两个会议室
会议室1:(0,30)
会议室2:(5,10),(15,20)
样例2
输入: intervals = [(2,7)]
输出: 1
解释:
只需要1个会议室就够了
'''
'''
SAME ANSWER:
Lintcode:#391Number of Airplanes in the Sky
给出飞机的起飞和降落时间的列表，用序列 interval 表示. 请计算出天上同时最多有多少架飞机？
如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。
样例
样例 1:
输入: [(1, 10), (2, 3), (5, 8), (4, 7)]
输出: 3
解释: 
第一架飞机在1时刻起飞, 10时刻降落.
第二架飞机在2时刻起飞, 3时刻降落.
第三架飞机在5时刻起飞, 8时刻降落.
第四架飞机在4时刻起飞, 7时刻降落.
在5时刻到6时刻之间, 天空中有三架飞机.
样例 2:
输入: [(1, 2), (2, 3), (3, 4)]
输出: 1
解释: 降落优先于起飞.
'''
'''
TOPIC: intervals, two pointers, sort
THINK:
Not ask if attend all meetings, but ask minimum room numbers for meeting, need two sorted list:one start, one end based on start
if cur[0] < prev[1] room++; if cur[0] > prev[1], reuse, prev++.
'''
def minMeetingRooms(intervals):
    if not intervals or len(intervals) == 0: return 0
    
    room = 0
    prev = 0
    
    start = sorted(intervals, key=lambda x:x[0])
    end = sorted(start, key=lambda x:x[1])
    
    for i in range(0, len(intervals), 1):
        if start[i][0] < end[prev][1]:
            room += 1
        else:
            prev += 1
    return room

print(minMeetingRooms([[0,30],[5,10],[15,20]]))   

'''
1094. Car Pooling
1WAY HARD !!!!!!!!
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
# var carPooling = function(trips, capacity) {
#     /*
#     TOPIC: sort, interval
#     HOW:
#     since pick and drop, so people will increase and decrease
#     fromtime+people, totime-people, store this result list
#     check each ele in list if <= capavity
#     */
#     if (trips === null || trips.length == 0 || capacity == 0) return False
    
#     const res = []
    
#     for (let trip of trips){
#         res.push([trip[1], trip[0]])
#         res.push([trip[2], trip[0]*(-1)])
#     }
#     res.sort((a, b) => a[1] - b[1]);
#     res.sort((a, b) => a[0] - b[0]);
    
#     let people = 0
#     for (let result of res){
#         people += result[1]
#         if (people > capacity) return false
#     }
#     return true
# };
print(carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]], 12)) #false
print(carPooling([[1,1,4],[9,4,9],[9,1,9],[2,3,5],[4,1,5],[10,4,5]],33))#false
print(carPooling([[2,1,5],[3,3,7]], 5))
/*
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
*/

const canAttendMeetings = function (intervals) {
  if (intervals == null || intervals.length == 0) return false;

  //sort base on interval[0], then sort interval[1], if they has overlap, immediately return false, otherwise keep checking
  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] > intervals[i - 1][1]) return false;
  }

  return true;
};
// console.log(
//   canAttendMeetings([
//     [0, 30],
//     [5, 10],
//     [15, 20],
//   ])
// );



/*
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
*/
const minMeetingRooms = function (intervals) {
  if (intervals == null || intervals.length == 0) return 0;

  //ask how many rooms we need, that means they need to know start of meeting and end of meeting
  //if prev end > next start, add room, otherwis reuse
  //sort meeting base on start, copy this sort and sort again base on end
  //Also work in single case:[[1,3]]
  let start = intervals.sort((a, b) => a[0] - b[0]);
  let end = [...intervals].sort((a, b) => a[1] - b[1]);
  console.log("start: ", start);
  console.log("end: ", end);

  let prev = 0,
    room = 0;
  for (let i = 0; i < intervals.length; i++) {
    //no matter overlap or not keep track start of meeting
    if (start[i][0] < end[prev][1]) {
      room++;
    } else {
      //reuse
      prev++; //only start after prev, will update prev
    }
    console.log("prev: ", prev, "  ", "cur: ", i, "  room: ", room);
  }
  return room;
};
//start:[0,30],[5,10],[15,20],[19,25]: cur pointer
//end:[5,10],[15,20],[19,25],[0,30]: prev pointer

// console.log(
//   "minimum room numbers: ",
//   minMeetingRooms([
//     [0, 30],
//     [5, 10],
//     [15, 20],
//     [19, 25],
//   ])
// );
// console.log(
//   "mini rooms: ",
//   minMeetingRooms([
//     [1, 6],
//     [5, 10],
//     [8, 12],
//   ])
// );
/*
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
*/
//same logic as #252
/*
def countOfAirplanes(airplanes):
    # write your code here
    start = sorted(airplanes,key=lambda x:x[0])
    print(start)
    end = sorted(start, key=lambda x:x[1])
    print(end)
    prev = 0
    res = 0
    for i in range(len(airplanes)):
        if start[i][0] < end[prev][1]: res += 1
        else: prev += 1
    return res

print(countOfAirplanes([[1, 10], [2, 3], [5, 8], [4, 7]]))
# print(countOfAirplanes([[1, 2], [2, 3], [3, 4]]))
*/

//Lintcode 577  mergeKSortedIntervalLists
/*
输入: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
输出: [(1,3),(4,8),(9,10)]
*/

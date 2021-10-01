/*
56. Merge Intervals
*/

//sort based on interval[0]
//check neighbor see if can merge
var merge = function (intervals) {
  if (intervals == null || intervals.length == 0) return [];

  //sort intervals itself
  intervals.sort((a, b) => a[0] - b[0]);

  //declare result array
  let prev = [intervals[0][0], intervals[0][1]];
  let res = [prev];

  for (let cur of intervals) {
    if (cur[0] <= prev[1]) {
      //can merge
      prev[1] = Math.max(cur[1], prev[1]); //update prev, beacause prev is array(mutable object), so prev in res will also update too
    } else {
      //mean now start new interval
      prev = cur;
      res.push(prev);
    }
  }
  return res;
};

// console.log(
//   //[1,7],[9,10]
//   merge([
//     [1, 6],
//     [2, 7],
//     [9, 10],
//   ])
// );

//57.Insert Interval
/*
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] 
that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order 
by starti and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
*/
var insert = function (intervals, newInterval) {
  //corner case
  if (intervals == null && newInterval) return [newInterval];
  if (newInterval == null && intervals) return intervals;

  //insert newinterval into intervals, then sort, then merge
  intervals.push(newInterval);

  //sort
  intervals.sort((a, b) => a[0] - b[0]);
  console.log(intervals);
  //merge
  let prev = [intervals[0][0], intervals[0][1]];
  let res = [prev];
  for (let cur of intervals) {
    //handle merge
    //update prev
    if (cur[0] <= prev[1]) {
      prev[1] = Math.max(prev[1], cur[1]);
    }

    //no overlap
    else {
      prev = cur;
      res.push(prev);
    }
  }
  return res;
};

console.log(
  insert(
    [
      [1, 3],
      [6, 9],
    ],
    [2, 5]
  )
);

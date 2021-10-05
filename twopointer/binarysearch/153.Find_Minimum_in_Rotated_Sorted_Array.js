//How to find minimum,see positions: low mid high(sorted); high low mid; mid high low; high mid low(X)
//base on right, since right alway ascending may after rotated
/*
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
*/
var findMin = function (nums) {
  if (nums == null || nums.length == 0) return -1;

  let low = 0,
    high = nums.length - 1;
  while (low < high) {
    //find unsure range not target, so <
    let mid = parseInt((low + high) / 2);
    if (nums[mid] > nums[high]) {
      //minimum must after mid
      low = mid + 1;
    } else {
      high = mid; //since while loop(low < high) not include, here muct include, so not high = mid -1
    }
  }
  return nums[low];
};

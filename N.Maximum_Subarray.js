//53. Maximum Subarray
var maxSubArray = function (nums) {
  //[5,3,-11,9]
  if (nums == null || nums.length == 0) return -Infinity;
  let max = nums[0]; //5

  //initiate dp this dp store single val not array since only need maximum val
  let dp = nums[0]; //5

  for (let i = 1; i < nums.length; i++) {
    dp = Math.max(dp + nums[i], nums[i]); //5+3 > 3; 8-11 > -11; -3<9
    //update dp and max in the meantime
    max = Math.max(dp, max);
  }
  return max;
};

//greedy
var canJump = function (nums) {
  if (nums == null || nums.length <= 1) return true;

  //check how far i go
  let maxIndex = 0;
  for (let i = 0; i < nums.length && i <= maxIndex; i++) {
    maxIndex = Math.max(maxIndex, nums[i] + i); //jump to index(nums[i]+i)
    if (maxIndex >= nums.length - 1) return true;
  }
  return false;
};

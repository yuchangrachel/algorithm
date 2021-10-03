//26
//return all unique elements, remove extra duplicates
//two pointer: same directions for i, j pointers, move in-place
var removeDuplicates = function (nums) {
  if (nums == null || nums.length == 0) return 0;
  let index = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[index] != nums[i]) {
      nums[++index] = nums[i];
    }
  }
  return index + 1;
};

//80
//return unique element or <= 2 elements, remove extra duplicates
//two pointer: same directions for i, j pointers, move in-place
var removeDuplicates2 = function (nums) {
  if (nums == null || nums.length == 0) return 0;
  let index = 0;
  let count = 1; // count occurance times for nums
  let flag = nums[index];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] == flag && count < 2) {
      nums[++index] = nums[i];
      count++;
    } else if (nums[i] != flag) {
      count = 1;
      nums[++index] = nums[i];
      flag = nums[i];
    }
  }

  return index + 1;
};

//27. Remove Element
//remove val who has duplicates, not only remove extra, also itself
//two pointers same direction
/*
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
*/
var removeElement = function (nums, val) {
  if (nums == null || nums.length == 0) return 0;
  let index = -1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      nums[++index] = nums[i];
    }
  }
  return index + 1;
};

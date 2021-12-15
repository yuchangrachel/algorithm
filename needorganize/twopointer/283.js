/*
283. Move zeros

move in-place
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
*/
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  //corner case invalid input
  if (nums == null || nums.length == 0) return;
  let right = 0; //update valid ele in array
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      nums[right++] = nums[i];
    }
  }
  while (right < nums.length) {
    nums[right++] = 0;
  }
};

//swap
var moveZeroes = function (nums) {
  //corner case invalid input
  if (nums == null || nums.length == 0) return;
  let j = 0; //update valid ele in array
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
      j++;
    }
  }
};

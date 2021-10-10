//1WAY T:O(nlogn) S:O(n)
var sortedSquares = function (nums) {
  if (nums == null || nums.length == 0) return [];
  nums.sort((a, b) => Math.abs(a) - Math.abs(b));
  const res = [];
  for (let n of nums) res.push(n * n);

  return res;
};

//2WAY T:O(n) S:O(n)
var sortedSquares = function (nums) {
  if (nums == null || nums.length == 0) return [];

  const res = new Array(nums.length).fill(0);
  let low = 0,
    high = nums.length - 1,
    k = nums.length - 1;
  while (low <= high) {
    if (Math.abs(nums[low]) <= Math.abs(nums[high])) {
      res[k--] = nums[high] * nums[high];
      high--;
    } else {
      res[k--] = nums[low] * nums[low];
      low++;
    }
  }
  return res;
};

//3WAY T:O(nlogn) S:O(1)
var sortedSquares = function (nums) {
  if (nums == null || nums.length == 0) return [];

  for (let i = 0; i < nums.length; i++) {
    nums[i] *= nums[i];
  }
  return nums.sort((a, b) => a - b);
};

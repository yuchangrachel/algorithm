//1WAY: O(n) in -place;
var sortArrayByParity = function (nums) {
  if (nums == null || nums.length == 0) return [];
  let i = 0,
    j = nums.length - 1;
  while (i <= j) {
    if (nums[i] % 2 != 0) {
      //odd swap with j
      while (nums[j] % 2 != 0 && i < j) {
        j--;
      }
      let temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
    }
    i++;
  }
  return nums;
};

//2WAY: sort T: O(nlogn) S:O(n) forEach
var sortArrayByParity = function (nums) {
  if (nums == null || nums.length == 0) return [];
  const temp = [];
  nums.forEach((num) => (num % 2 === 0 ? temp.unshift(num) : temp.push(num)));
  return temp;

  //3WAY: using filter
  return [
    ...nums.filter((n) => n % 2 === 0),
    ...nums.filter((n) => n % 2 !== 0),
  ];

  //4WAY: python
  return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 != 0]
};



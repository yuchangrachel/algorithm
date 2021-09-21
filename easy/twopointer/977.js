var sortedSquares = function (nums) {
  //1SOLUTION:built-in method O(nlogn)
  return nums.map((num) => num * num).sort((a, b) => a - b);

  //2SOLUTION:extra space but T:O(n)
  //use two pointers, compare leftmost and rightmost. who is bigger since has positive and negative
  const res = new Array(nums.length);
  let i = 0;
  let j = nums.length - 1;
  let k = nums.length - 1;
  while (i <= j) {
    if (nums[i] * nums[i] < nums[j] * nums[j]) {
      res[k] = nums[j] * nums[j];
      k--;
      j--;
    } else {
      res[k] = nums[i] * nums[i];
      k--;
      i++;
    }
  }
  return res;
};

/*
JS KNOWLEDGE:
list.map -> return new list. 
list.sort((a,b)=> a-b) must have arrow func
*/

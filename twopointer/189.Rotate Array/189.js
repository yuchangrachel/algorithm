const rotate = function (nums, k) {
  k = k % nums.length; //k may > nums.length
  //three-times flip
  reverse(nums, 0, nums.length - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, nums.length - 1);
};

const reverse = function (list, start, end) {
  while (start < end) {
    let temp = list[start];
    list[start] = list[end];
    list[end] = temp;
    start++;
    end--;
  }
};

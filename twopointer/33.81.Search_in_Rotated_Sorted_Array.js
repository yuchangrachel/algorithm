//33
var search = function (nums, target) {
  if (nums == null || nums.length == 0) return -1;

  let low = 0,
    high = nums.length - 1;
  while (low <= high) {
    //<= because find target
    let mid = parseInt((low + high) / 2);
    if (nums[mid] == target) return mid;
    else if (nums[low] <= nums[mid]) {
      //this range is ascending order must <= eg.[3,1] 1
      if (target >= nums[low] && target <= nums[mid]) {
        high = mid - 1;
      } else low = mid + 1;
    } else {
      //mean rotated. after mid will ascending order
      if (target >= nums[mid] && target <= nums[high]) {
        low = mid + 1;
      } else high = mid - 1;
    }
  }
  return -1;
};

//81
//include duplicate [2,5,6,0,0,1,2] target = 0
//when duplicate move one pointer until not the same
var search = function (nums, target) {
  if (nums == null || nums.length == 0) return false;

  let low = 0,
    high = nums.length - 1;
  while (low <= high) {
    let mid = parseInt((low + high) / 2);
    if (nums[mid] == target) return true;
    else if (nums[low] < nums[mid]) {
      //this range is ascending order, not include same value since will peak or valley
      if (target >= nums[low] && target <= nums[mid]) {
        high = mid - 1;
      } else low = mid + 1;
    } else if (nums[low] > nums[mid]) {
      //rotated, mean after mid will be in sorted order
      if (target >= nums[mid] && target <= nums[high]) {
        low = mid + 1;
      } else high = mid - 1;
    } else {
      //duplicate nums[low] = nums[mid]
      low++; //skip nums[low]
    }
  }
  return false;
};

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
def search(self, nums: List[int], target: int) -> int:
        '''
        LOGIC: binary search two pointer
        HOW:get mid, compare [low, mid] if in increasing order, check if target in this range
        '''
        if not nums or len(nums) == 0: return -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: # low pos = mid pos, same number should be counted               
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1 # follow binary search logic
                else:
                    # so answer may in another side
                    low = mid + 1
            else: #already rotated, [mid ... high] in increasing order
                if nums[mid] <= target<= nums[high]:
                    low = mid + 1
                else: 
                    high = mid - 1
        return -1
                    

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
def search(self, nums: List[int], target: int) -> bool:
        '''
        TOPIC: binary search, two pointers
        HOW:
        this question compare to #33, this question has more constraint:has duplicate
        rotate will separate some duplicates in different sides[2,2,5,5,6,0,0,1,2]
        How to handle duplicate, when [low] < [mid]. not [low]<=[mid],mean [low ...mid] all elements are same, low ++
        '''
        if not nums or len(nums) == 0: return False
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return True
            elif nums[mid] > nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1 # duplicates so ignoare all same ones
        return False
                
        

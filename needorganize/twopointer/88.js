/*
88.Merge Sorted Array

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
*/

var merge = function (nums1, m, nums2, n) {
  if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0)
    return;
  //starting from back, avoid replace orginal ele
  let i = m - 1,
    j = n - 1,
    k = m + n - 1; //i tracking n1, j tracking n, k tracking result
  while (i >= 0 && j >= 0) {
    if (nums1[i] >= nums2[j]) {
      nums1[k--] = nums1[i--];
    } else {
      nums1[k--] = nums2[j--];
    }
  }

  while (i >= 0) {
    nums1[k--] = nums1[i--];
  }
  while (j >= 0) {
    nums1[k--] = nums2[j--];
  }
};

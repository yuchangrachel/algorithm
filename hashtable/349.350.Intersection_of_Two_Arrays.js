/*
349.
LOGIC:
1.Dont need create extra data structure store, use shorter num as compared array, if n in nums2 also in nums1, push into res array
KNOWLEDGE:
in js: new Set(), set.add, set.has(), Array.from(set), array.includes(v)
in py: set(), set.add, if v in set, list(set), if v in array
*/
var intersection = function (nums1, nums2) {
  if (nums1.length < nums2.length) {
    temp = nums1;
    nums1 = nums2;
    nums2 = temp;
  }
  const res = new Set();
  for (let c of nums2) {
    if (nums1.includes(c)) res.add(c);
  }

  return Array.from(res);
};

// def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
//         if len(nums1) > len(nums2):
//             temp = nums1
//             nums1 = nums2
//             nums2 = temp

//         res = set()
//         for n in nums2:
//             if n in nums1:
//                 res.add(n)
//         return list(res)

/*
350
LOGIC:
1.since may appear many times, so use hash store shorter array
COMPLEXITY: T:O(N + M), O(N) for iterate one of the array to create a hashmap and O(M) to iterate the other array. S:O(N).
*/
var intersect = function (nums1, nums2) {
  if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0)
    return [];

  if (nums1.length > nums2.length) {
    temp = nums1;
    nums1 = nums2;
    nums2 = temp;
  }
  const res = [];
  const dic = new Map();
  //store nums1
  for (let n of nums1) {
    dic.set(n, (dic.get(n) || 0) + 1);
  }

  for (let n of nums2) {
    if (dic.has(n) && dic.get(n) > 0) {
      res.push(n);
      dic.set(n, dic.get(n) - 1);
    }
  }
  return res;
};
/*
350.FOLLOW-UP1
What if the given array is already sorted? How would you optimize your algorithm?
LOGIC:two pointer
*/
var intersect1 = function (nums1, nums2) {
  if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0)
    return [];

  let i = 0,
    j = 0,
    res = [];
  while (i < nums1.length && j < nums2.length) {
    if (nums1[i] == nums2[j]) {
      res.push(nums1[i]);
      i++;
      j++;
    } else if (nums1[i] < nums2[j]) {
      i++;
    } else {
      j++;
    }
  }
  return res;
};
console.log(intersect1([1, 2, 3, 5, 7, 9], [2, 3, 4, 7, 8]));

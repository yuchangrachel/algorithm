/*
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
*/

//need delete some char in s, so convert into array(modify s)
//iterate array until find part at [curIndex, cur + part.length)
var removeOccurrences = function (s, part) {
  if (s == null || s.length == 0) return null;
  if (part == null || part.length == 0) return s; //nothing to remove

  while (s.includes(part)) {
    //if part still in s, go to loop otherwise return
    let part_start_index = s.indexOf(part);
    s =
      s.substring(0, part_start_index) +
      s.substring(part_start_index + part.length);
    //can use slice
  }
  return s;
};

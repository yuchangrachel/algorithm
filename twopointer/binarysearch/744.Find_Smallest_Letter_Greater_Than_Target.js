/*
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
Note that the letters wrap around.
For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"
*/
//1WAY binary search O(logn)
//if target >= [last]=> return [first]
var nextGreatestLetter = function (letters, target) {
  if (letters == null || letters.length == 0) return "";

  let low = 0,
    high = letters.length - 1;
  if (target >= letters[high]) return letters[0];

  while (low < high) {
    //find range
    let mid = parseInt((low + high) / 2);
    if (letters[mid] <= target) {
      low = mid + 1;
    } else {
      high = mid; //template
    }
  }
  return letters[low];
};

//2WAY linear O(n)
var nextGreatestLetter = function (letters, target) {
  if (letters == null || letters.length == 0) return "";

  for (const letter of letters) {
    if (letter > target) return letter;
  }
  return letters[0];
};

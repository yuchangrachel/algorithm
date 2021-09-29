//LongestSubstringWithoutRepeatingCharacters
var lengthOfLongestSubstring = function (s) {
  //corner case valid input
  if (s == null || s.length == 0) return 0;

  //declare hash
  const hash = new Array(256).fill(0); // consists of English letters, digits, symbols and spaces

  //declare variable
  let res = 0;

  for (let right = 0, left = 0; right < s.length; right++) {
    //update hash
    hash[s.charCodeAt(right)]++;

    //check valid & move left
    while (hash[s.charCodeAt(right)] != 1) {
      //has duplicates
      hash[s.charCodeAt(left)]--;
      left++;
    }

    //update res
    res = Math.max(res, right - left + 1);
  }
  return res;
};

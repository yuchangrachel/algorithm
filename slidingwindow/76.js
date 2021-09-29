/*
Minimum Window Substring

Window size change(not fix, so count no need offset)
*/
const minWindow = function (s, t) {
  //corner case check input valid or not
  if (s == null || t == null || s.length < t.length) return "";

  //because contains lower and uppercase
  const hash = new Array(256).fill(0);
  //store t into hash
  for (let i = 0; i < t.length; i++) {
    hash[t.charCodeAt(i)]++;
  }

  let left = 0,
    count = 0,
    max = s.length + 1;
  let res = "";
  for (let right = 0; right < s.length; right++) {
    //update hash
    hash[s.charCodeAt(right)]--;

    //check&update valid
    if (hash[s.charCodeAt(right)] >= 0) count++;

    //move left
    //keep removing uncessary: not exist or cur replace it
    //here not need handle count
    while (left < right && hash[s.charCodeAt(left)] < 0) {
      hash[s.charCodeAt(left)]++; //recover
      left++;
    }

    //result
    if (count == t.length && max > right - left + 1) {
      max = right - left + 1;
      res = s.substring(left, right + 1);
    }
  }
  return res;
};

console.log(minWindow("ADOBECODEBANC", "ABC")); //"BANC"

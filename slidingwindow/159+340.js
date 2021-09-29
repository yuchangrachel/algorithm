/*
#340 #159
Longest Substring with AtMost Two DistinctCharacters
Longest substring with atMost K distinct Characters


window size is changeable

refer:https://www.1point3acres.com/bbs/thread-544207-1-1.html
*/
//Two pointer O(n^2)
const lengthOfLongestSubstringKDistinct1 = function (s, k) {
  //corner case invalid input
  if (s == null || s.length == 0) return 0;

  //map store k size
  const mapping = new Map();
  let res = 0;

  //each substring start left and its substring
  for (let left = 0, right = 0; left < s.length; left++) {
    //store char in map with at most k size
    while (right < s.length && mapping.size <= k) {
      //keep adding into map
      if (mapping.has(s[right])) {
        mapping.set(s[right], mapping.get(s[right]) + 1);
      } else {
        if (mapping.size == k) break;
        //cannot add, full
        else mapping.set(s[right], 1);
      }
      right++;
    }

    //update res
    res = Math.max(res, right - left); //right already+1

    //remove left
    if (mapping.has(s[left])) {
      if (mapping.get(s[left]) > 1)
        mapping.set(s[left], mapping.get(s[left]) - 1);
      else mapping.delete(s[left]);
    }
  }
  return res;
};

//O(n) Sliding window
const lengthOfLongestSubstringKDistinct = function (s, k) {
  //corner case input
  if (s == null || s.length == 0 || k == 0) return 0;

  //declare hash
  const hash = new Array(256).fill(0); //256 include all characters in Ascii code

  //declare variable
  let count = 0,
    res = 1; //result string not empty
  for (let left = 0, right = 0; right < s.length; right++) {
    //update hash
    hash[s.charCodeAt(right)]++;

    //check valid
    if (hash[s.charCodeAt(right)] == 1) count++;

    //move left when more k diff characters
    while (count > k) {
      hash[s.charCodeAt(left)]--;
      if (hash[s.charCodeAt(left)] == 0) count--;
      left++;
    }

    //result update
    res = Math.max(res, right - left + 1);
  }
  return res;
};

console.log(lengthOfLongestSubstringKDistinct("eceba", 2));

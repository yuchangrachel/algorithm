/*
438.Find All Anagrams in a String


Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Window size is fixed: p.
Left pointer will move foward when window moves
Two pointer starting from left towards right
normally, Sliding window: T:O(n) S:O(n)
*/

const asscii = "a".charCodeAt();

var findAnagrams = function (s, p) {
  //corner case or check input valid
  if (s.length < p.length) return [];

  //use data structure eg.array, map store specific elements in window {char: freq}
  const hash = new Array(26).fill(0);
  for (let i = 0; i < p.length; i++) {
    hash[p.charCodeAt(i) - asscii]++;
  }

  //declare result, left pointer(start of window), count(current situation)
  const res = [];
  let left = 0,
    count = 0;

  //loop for window right for expanding
  for (let right = 0; right < s.length; right++) {
    //now used it, so update(deduct amount in hash) if after deduct is -1, mean not in pstr
    hash[s.charCodeAt(right) - asscii]--;

    //check valid char in pstr
    if (hash[s.charCodeAt(right) - asscii] >= 0) {
      count++;
    }

    //check if need to move left, need keep window size is p length
    if (right > p.length - 1) {
      //add it again since deduct
      hash[s.charCodeAt(left) - asscii]++;
      //deduct count since was valid
      if (hash[s.charCodeAt(left) - asscii] > 0) {
        count--;
      }

      left++;
    }

    if (count == p.length) res.push(left);
  }
  return res;
};

// console.log(findAnagrams("acba", "ab"));

/*
567.Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
*/

var checkInclusion = function (s1, s2) {
  //corner case invalid input
  if (
    s1 == null ||
    s2 == null ||
    s1.length == 0 ||
    s2.length == 0 ||
    s1.length > s2.length
  )
    return false;

  //store s1
  //if store 26 letter, need do ch - 'a'
  const hash = new Array(256).fill(0); //consist of lowercase English letters
  for (let i = 0; i < s1.length; i++) {
    hash[s1.charCodeAt(i)]++;
  }
  console.log("hash: ", hash);

  //declare variable
  let count = 0;
  for (let left = 0, right = 0; right < s2.length; right++) {
    //update hash
    hash[s2.charCodeAt(right)]--;

    //valid
    if (hash[s2.charCodeAt(right)] >= 0) count++;

    //move left
    if (right > s1.length - 1) {
      hash[s2.charCodeAt(left)]++;
      if (hash[s2.charCodeAt(left)] > 0) count--;
      left++;
    }

    //update result
    if (count == s1.length) return true;
  }
  return false;
};

console.log(checkInclusion("ab", "eidbaooo"));

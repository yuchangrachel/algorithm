// 316. Remove Duplicate Letters
//1081. Smallest Subsequence of Distinct Characters

// Given a string s, remove duplicate letters so that every letter appears once and only once.
//You must make sure your result is the smallest in lexicographical order among all possible results.
// Example 1:
// Input: s = "bcabc"
// Output: "abc"

//LOGIC:
//need count[26] lowercase store all char in string
//updateStr
//boolean[26]check if used or not, if used,continue
const a = "a".charCodeAt();
var removeDuplicateLetters = function (s) {
  if (s == null || s.length == 0) return "";

  //store hash
  const hash = new Array(26).fill(0);
  for (let i = 0; i < s.length; i++) {
    hash[s.charCodeAt(i) - a]++;
  }
  const visited = new Array(26).fill(false);

  //declare res
  let res = [];

  for (let i = 0; i < s.length; i++) {
    //update hash
    hash[s.charCodeAt(i) - a]--;
    if (visited[s.charCodeAt(i) - a]) continue;

    //if prev has duplicate and cur smaller than prev
    while (
      res.length > 0 &&
      res[res.length - 1] > s[i] &&
      hash[res[res.length - 1].charCodeAt() - a] > 0
    ) {
      //let visited false recover
      visited[res[res.length - 1].charCodeAt() - a] = false;
      res.pop();
    }

    //each time update string, visited=true
    res.push(s[i]);
    visited[s.charCodeAt(i) - a] = true;
  }

  return res.join("");
};

console.log(removeDuplicateLetters("bcbca")); //abc
// console.log(removeDuplicateLetters("cbacdcbc")); //acdb

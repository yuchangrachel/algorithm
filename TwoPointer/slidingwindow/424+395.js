/*
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
*/
//find longest repeating char, replace few of them
const capitalA = "A".charCodeAt();
var characterReplacement = function (s, k) {
  //corner case invalid input
  if (s == null || k == null || s.length < k) return 0;

  //declare hash
  const hash = new Array(26).fill(0);

  //declare variable
  let maxCount = 0,
    res = 0;
  //store hash and meanwhile update maxcount
  for (let left = 0, right = 0; right < s.length; right++) {
    //update hash
    hash[s.charCodeAt(right) - capitalA]++;

    //check valid
    maxCount = Math.max(maxCount, hash[s.charCodeAt(right) - capitalA]);

    //move left
    while (right - left + 1 - maxCount > k) {
      //window.size - maxAcount out of replace num
      hash[s.charCodeAt(left) - capitalA]--;
      left++;
    }

    //result
    res = Math.max(res, right - left + 1);
  }
  return res;
};

/*395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
*/
/*
Divide and Conquer
[a,b,a,b,b,c,a,a,b,b] k=2
map{a:4, b:5 c: 1} can see not meet k, so split there
[a,b,a,b,b]    [a,a,b,b]
map{a:2 b:3}    {a:2, b:2}  both divisions meet, so see maxlen
*/
const a = "a".charCodeAt();

var longestSubstring = function (s, k) {
  //corner case invalid input
  if (s == null || k == null || s.length < k) return 0;
  return helper(s, k, 0, s.length);
};

const helper = function (s, k, start, end) {
  //base case terminate case
  if (start > end) return 0;

  //each recursion create new hash since divide and conquer create split new two arrays
  const hash = new Array(26).fill(0); //all lowcase
  //store hash
  for (let i = start; i < end; i++) {
    //store all char in hash
    hash[s.charCodeAt(i) - a]++;
  }

  //handle and check valid
  for (let i = start; i < end; i++) {
    //find split
    if (hash[s.charCodeAt(i) - a] < k) {
      //this i is splitter, start from next, but keep check next until valid next
      let j = i + 1;
      while (j < end && hash[s.charCodeAt(j) - s] < k) {
        //still splitter
        j++;
      }

      //get split and do divide and conquer
      return Math.max(helper(s, k, start, i), helper(s, k, j, end));
    }
  }

  return end - start;
};

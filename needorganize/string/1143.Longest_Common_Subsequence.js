/*
1.brute force TLE
Explain: find longest common subsequence mean text1 may not have all chars in text2, only few or 0, or all.

Logic: subsequence mean dont need contiguous substring, but in relative order same as text2
recursion to permutate find all common subsequence, recursion can guarantee relative order
if do recursion, most of time have helper

T(n)=O(2^n) 
S(n)=O(1) if not include recursive function stack
*/

const longestCommonSubsequence = function (text1, text2) {
  //corner case When doing recursion, most of time dont need it
  // if (text1 == null || text2 == null || text1.length == 0 || text2.length == 0) return 0
  return helper(text1, text2, 0, 0);
};

const helper = function (text1, text2, p1, p2) {
  if (p1 == text1.length || p2 == text2.length) return 0;

  if (text1[p1] == text2[p2]) {
    //common char
    return 1 + helper(text1, text2, p1 + 1, p2 + 1); //count it
  }

  return Math.max(
    helper(text1, text2, p1 + 1, p2),
    helper(text1, text2, p1, p2 + 1)
  ); //goal is find more common chars
};

/*
2,Top-bottom DP
Like recursion with memorization
store result which reuse latter
T=O(MN)
S=O(MN)
*/
const longestCommonSubsequence = function (text1, text2) {
  //two pointer for two strings so 2D array size it is their length
  const dp = new Array(text1.length);
  for (let i = 0; i < dp.length; i++) {
    dp[i] = new Array(text2.length);
  }
  return helper(text1, text2, 0, 0, dp);
};

const helper = function (text1, text2, p1, p2, dp) {
  if (p1 == text1.length || p2 == text2.length) return 0;

  //dp one case
  if (dp[p1][p2] != null) return dp[p1][p2];

  if (text1[p1] == text2[p2]) {
    //common char
    dp[p1][p2] = 1 + helper(text1, text2, p1 + 1, p2 + 1, dp); //count it
    return dp[p1][p2];
  }

  dp[p1][p2] = Math.max(
    helper(text1, text2, p1 + 1, p2, dp),
    helper(text1, text2, p1, p2 + 1, dp)
  ); //goal is find more common chars
  return dp[p1][p2];
};

console.log(longestCommonSubsequence("abbbbcddda", "ace")); //2

/*
3.bottom-up
For every i in text1, j in text2, we will choose one of the following two options:
if two characters match, length of the common subsequence would be 1 plus the length of the common subsequence till the i-1 andj-1 indexes
if two characters doesn't match, we will take the longer by either skipping i or j indexes
*/

const longestCommonSubsequence = function (text1, text2) {
  if (text1 == null || text2 == null) return 0;

  //two pointer for two strings so 2D array size it is their length
  //2d dp store common longest len
  const dp = new Array(text1.length + 1).fill(0);
  for (let i = 0; i < dp.length; i++) {
    dp[i] = new Array(text2.length + 1).fill(0);
  }

  //i, j has two options: common: 1+len(commons); else: keep track
  for (let i = 1; i <= text1.length; i++) {
    for (let j = 1; j <= text2.length; j++) {
      if (text1[i - 1] == text2[j - 1]) {
        dp[i][j] = 1 + dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[text1.length][text2.length];
};

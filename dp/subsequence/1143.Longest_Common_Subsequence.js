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

//SLOW
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # subsequence order does matter, find many common as possible
        memo = [[0 for j in range(len(text2))] for i in range(len(text1))]

        def helper(i, j):
            # terminate case no common anymore
            if i == len(text1): return 0
            if j == len(text2): return 0
            # visited store in cacahe
            if memo[i][j] != 0: return memo[i][j]
            
            if text1[i] == text2[j]:
                # find one common update memo
                memo[i][j] = 1 + helper(i+1, j+1)
                return memo[i][j]
            
            memo[i][j] = max(helper(i+1, j), helper(i, j+1))
            return memo[i][j]
            
        return helper(0,0)
        
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

//583. Delete Operation for Two Strings
def minDistance(self, word1: str, word2: str) -> int:
        #TOPIC:Minimum delete times to make two string same: n1+n2-longest common subsequence*2
        #HOW:bottom-top dp, two strings compare need 2D array,size +1(because[0] is empty string)
        if not word1 or not word2: return 0
        
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1) + 1)]
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)]

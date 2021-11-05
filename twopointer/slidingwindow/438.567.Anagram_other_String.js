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
*/

/*
LOGIC: 
1.window size is fixed
2.create hash for p {c:freq}
3.'count' variable for counting valid result, since there are more than one result, so will reset 'count' while changing window(move left action)
4.when move left? i > p.length -1, out of p

Complexity: T:O(n) S:O(p)

*/
const a = "a".charCodeAt();
var findAnagrams = function (s, p) {
  if (
    p == null ||
    s == null ||
    p.length == 0 ||
    s.length == 0 ||
    p.length > s.length
  )
    return [];

  //create hash
  //only lower case
  const dic = new Array(26).fill(0);
  for (let c of p) {
    dic[c.charCodeAt() - a]++;
  }

  //create variable
  let res = [],
    count = 0,
    left = 0;
  for (let i = 0; i < s.length; i++) {
    //update hash
    dic[s.charCodeAt(i) - a]--;

    //check valid or not
    if (dic[s.charCodeAt(i) - a] >= 0) count++;

    //move left widow size is fixed
    if (i - left + 1 > s1.length) {
      dic[s.charCodeAt(left) - a]++; //recover
      if (dic[s.charCodeAt(left) - a] > 0) count--; //count reset since need use it again, > 0 since = 0 means no cha in p
      left++;
    }

    //check result
    if (count == p.length) {
      res.push(left);
    }
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
    if (right - left + 1 > s1.length) {
      hash[s2.charCodeAt(left)]++;
      if (hash[s2.charCodeAt(left)] > 0) count--;
      left++;
    }

    //update result
    if (count == s1.length) return true;
  }
  return false;
};

def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        LOGIC:
        sliding window, window size is fixed (s1 permutation)
        window = s1 all permutation
        hardest part: if find not permutated string of s1, has other chars : while i - left + 1 > len(s1):
        '''
        if len(s1) > len(s2) or not s1 or not s2 or len(s1) == 0 or len(s2) == 0: return False
        
        # create hash for s1
        a = ord('a')
        dic = [0] * 26
        for c in s1:
            dic[ord(c) - a] += 1
        
        left = 0
        count = 0

        for i in range(len(s2)):
            dic[ord(s2[i]) - a] -= 1
            
            if dic[ord(s2[i]) - a] >= 0:
                count += 1
            
            while i - left + 1 > len(s1):
                dic[ord(s2[left]) - a] += 1
                # need reset count
                if dic[ord(s2[left]) - a] > 0: # work before
                    count -= 1
                left += 1
            
            if count == len(s1):
                return True
            
        return False

console.log(checkInclusion("ab", "eidbaooo"));

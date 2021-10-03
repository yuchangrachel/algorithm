//125
var isPalindrome = function (s) {
  let regex = new RegExp("^[a-zA-Z0-9]");
  s = s.toLowerCase().replace(regex, "");
  console.log(s);
  let copy = s;
  return copy.split("").reverse().join("") == s;
};

//680
var validPalindrome = function (s) {
  if (s == null || s.length == 0 || isPalindrome(s, 0, s.length - 1))
    return true;

  //must delete some char in s
  let start = 0,
    end = s.length - 1,
    count = 0;
  while (start <= end) {
    if (s[start] != s[end]) {
      return isPalindrome(s, start, end - 1) || isPalindrome(s, start + 1, end);
    } else {
      start++;
      end--;
    }
  }
  return true;
};

const isPalindrome = function (s, start, end) {
  while (start <= end) {
    if (s[start] != s[end]) return false;
    start++;
    end--;
  }
  return true;
};

/*
1328
Break palindrome
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.
Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
Example 3:

Input: palindrome = "aa"
Output: "ab"
Example 4:

Input: palindrome = "aba"
Output: "abb"
*/
//1case: if one is not a : change non-a into a: cc->ac
//2case: if all a: change last one to b: aabaa->aabab
var breakPalindrome = function (palindrome) {
  if (palindrome == null || palindrome.length <= 1) return "";
  let p = palindrome.split("");
  let i = 0;
  while (i < parseInt(p.length / 2)) {
    //thi is palindrome so just check half
    if (p[i] != "a") {
      p[i] = "a";
      return p.join("");
    }
    i++;
  }
  //all a
  p[p.length - 1] = "b";
  return p.join("");
};

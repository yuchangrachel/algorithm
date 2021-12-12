#5. Longest Palindromic Substring
'''
    TOPIC:longest palindromic subtring:CENTER EXPAND
    STEP:
    1.create helper isPalindrome(str, left,right) expand two sides from center, return palindrome string
    2.use ispalindrome(i,i) and isplandrome(i,i+1)
'''
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0: return s
        res = ""
        for i in range(len(s)):
            if len(self.isPalindrome(s,i,i)) > len(res):
                res = self.isPalindrome(s,i,i)
            if i+1 < len(s) and len(self.isPalindrome(s,i, i+1)) > len(res):
                res = self.isPalindrome(s, i,i+1)
        return res
                
        
    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
# 125 Valid Palindrome
# 1WAY regular expression
# var isPalindrome = function(s) {
#     let pattern = /[^a-zA-Z0-9]/g
#     s = s.toLowerCase().replace(pattern, "")
#     let copy = s
#     return copy.split("").reverse().join("") == s
# };
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s.lower())
        print(s)
        copy = s
        return copy[::-1] == s

def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0: return True
        
        low = 0
        high = len(s) - 1
        s = s.lower()
        
        while low < high:
            if s[low].isalnum():
                if s[high].isalnum():
                    if s[low] != s[high]: return False
                    else:
                        low += 1
                        high -= 1
                else:
                    high -= 1
            else:
                low += 1
        
        return True

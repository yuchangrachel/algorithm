#5. Longest Palindromic Substring
def longestPalindrome(self, s: str) -> str:
        '''
        center expand, palindrome two situations: aba, abba
        b
        a -> bab
        b -> aba
        a 
        d
        '''
        res = ""
        max_len = 0
        for i in range(len(s)):
            p1 = self.isPalindrome(s, i, i)
            p2 = ""
            if i != len(s) - 1:
                p2 = self.isPalindrome(s, i, i+1)
            if len(p1) >= max_len:
                res = p1
                max_len = len(p1)
            if len(p2) >= max_len:
                res = p2
                max_len = len(p2)
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
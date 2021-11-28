# 409. Longest Palindrome
def longestPalindrome(self, s: str) -> int:
        '''
        TOPIC: rebuild string, palindrome:even len or odd len
        THINK: map{c:freq}, if freq is even, count it; if freq is odd and if c1.freq = c2.freq =c3.freq ...accumulate into even length
        HOW: use set, add when null, remove when exist, left number in set, need get rid from result
        '''
        if not s or len(s) == 0: return 0

        count = set()
        for c in s:
            if c not in count: count.add(c)
            else: count.remove(c)
        if len(count) > 0: # has odd
            return len(s) - len(count) + 1 #keep one odd as center
        else:
            return len(s)
# 680. Valid Palindrome II
def validPalindrome(self, s: str) -> bool:
        '''
        TOPIC: at most delete one time to see if valid palindrome
        HOW: two pointer, left ,right, same, two pointers update; otherwise two options: move left or move right, but may two ways works, so need to keep search rest of part.           Need while loop inside
        '''
        if not s or len(s) == 0 or self.isPalindrome(s, 0, len(s) - 1): return True

        low = 0
        high = len(s) -1

        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isPalindrome(s, low+1, high) or self.isPalindrome(s, low, high-1)
        return True

def isPalindrome(self, s, low, high):
        while low <= high:
            if s[low] != s[high]: return False
            else:
                low += 1
                high -= 1
        return True

def longestPalindrome(self, s: str) -> str:
        #TOPIC: longest palindrome substring, center spread out to both sides
        #HOW:for(recursion),i&i, i&i+1 aba, abba
        if not s or len(s) == 0: return ""
        
        res = ""
        for i in range(len(s)):
            if len(res) < len(self.expand(s, i,i)):
                res = self.expand(s,i,i)
            if len(res) < len(self.expand(s, i, i+1)):
                res = self.expand(s,i,i+1)
        return res
            
        
    def expand(self, s, low, high):
        res = ""
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -=1
            high += 1
        return s[low+1:high]
                
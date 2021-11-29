#91. Decode Ways
'''
"226"
    /\
   22 2
   /  \
  6    2
      / \
     26  6
A=>1
Z=>26
two digits:
1:0-9
2:0-6
'''
class Solution:
    def __init__(self):
        self.answer = 0
        
    #Brute force O(n^2)
    def numDecodings(self, s):
        # corner case 
        if not s or s[0] == "0": 
            return 0
    
        def helper(s):
            if not s or (len(s) <= 1 and s[0] != "0"):
                self.answer += 1
                return 
            if s[0] == "0":
                return
            if int(s[:2]) <= 26:
                helper(s[2:])
            helper(s[1:])
        
        helper(s)

        return self.answer

solution = Solution()
print(solution.numDecodings("226"))


'''
    1WAY: TLE
    BRUTE FORCE
    TIME COMPELEXITY: 2^n 
    REASON:
    T(N) = T(N-1) + T(N-2) + ... + T(0)
    T(N-1) = T(N-2) + ... + T(0)
    T(N) - T(N-1) = T(N-1)
    T(N) = 2*T(N-1)
    O(2^N)
    REFER:https://leetcode.com/problems/word-break/discuss/169383/solved-The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below
'''
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict: return False
        set_dic = set(wordDict)
        return self.rec(s, set_dic)
    
def rec(self, s, set_dic):
        if len(s) == 0:
            return True
        
        for i in range(1, len(s) + 1,1):
            if s[0:i] in set_dic and self.rec(s[i:], set_dic):
                return True
            
        return False
    
'''
    2WAY
    Bottom-top DP 
    TIME:O(N^2)
'''
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict: return False
        
        #create set than list save space
        set_dic = set(wordDict)
        
        #create dp
        dp = [False] * (len(s) + 1) #use slice, exclude last, so need extra work to add last index
        #init dp
        dp[0] = True # "" is true
        
        for i in range(1, len(s) + 1, 1): # two pointer's right
            for j in range(0, i, 1): # two pointer's left
                if dp[j] and s[j:i] in set_dic: # mean [0, j] if true, s[j: end] also true will return true
                    dp[i] = True
                    
        return dp[len(s)]
'''
    1WAY: TLE
    BRUTE FORCE
Time: O(N*N) since each time it has at most N choices and the depth (problem size) is N. (this is an upper bound)
Space: O(N) (string length and call stack depth))
'''
def wordBreak1(s, wordDict):
        if not s or not wordDict: return False
        set_dic = set(wordDict)
        return rec(s, set_dic)
    
def rec(self, s, set_dic):
        if len(s) == 0:
            return True
        
        for i in range(1, len(s) + 1,1):
            if s[0:i] in set_dic and self.rec(s[i:], set_dic):
                return True
            
        return False
    
# '''
#     2WAY
#     Bottom-top DP 
#     TIME:O(N^2) 
# '''
def wordBreak2(s, wordDict):
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

'''
3WAY
TOP-BOTTOM DP/recursion with memorization
EASY TO UNDERSTAND
TIME:O(n^2)
'''
def wordBreak3(s,wordDict):
        # recursion memo => top-bottom dp
        if not s or not wordDict: return False
        ws = set(wordDict) # not have to since all string in dict are unique
        
        memo = {} #store{startindexofS:T/F}
        def helper(s):
            if s in memo:
                return memo[s]
            
            if len(s) == 0: #to the end
                return True
            
            for i in range(1, len(s)+1):
                if s[0:i] not in ws:
                    continue
                # now s[0:i] in dict
                res = helper(s[i:])
                if res:
                    memo[s] = True
                    return True
                
            memo[s] = False
            return False

        return helper(s)
print(wordBreak2("catsandog",
["cats","dog","sand","and","cat"]))
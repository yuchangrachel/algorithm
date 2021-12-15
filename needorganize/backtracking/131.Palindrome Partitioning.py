'''
    TOPIC:show all palindrome substring combination results:backtracking
    STEP:
    1.need isPalindrome helper, dfs(curlist,startIndex of str)
'''
def partition(self, s: str) -> List[List[str]]:
        if not s or len(s) == 0: return []
        res = []
        self.dfs(s, 0, [], res)
        return res
        
def dfs(self, s, start, curls, res):
        #terminate case
        if start == len(s):
            res.append(curls.copy())
            return
        for i in range(start, len(s), 1):
            if self.isPalindrome(s, start, i) == False: 
                continue # "ab" false "aba" true
            # now is palindrome substring
            temp = s[start:i+1]
            curls.append(temp)
            # do dfs recursion
            self.dfs(s, i+1, curls, res)
            curls.pop()
    
def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]: return False
            else:
                start += 1
                end -= 1
        return True
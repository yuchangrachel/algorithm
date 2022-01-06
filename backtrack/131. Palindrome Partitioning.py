class Solution:
    '''
    TOPIC:Show palindrome substring result, use Backtracking, if need single val use DP
    STEP:backtracking template:
    1.In main method, create helper method dfs(index, temp, res)
    2.In dfs method, 
    terminate case(index=len(s)).
    recursion case(prune first check isPalindrome False continue, for i ..., get substr[index...i], add, dfs(i+1), pop)
    3.helper method isPalindrome(substr,start,end)
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(0, s, [], res)
        return res
    
    def dfs(self, index, s, temp, res):
        if index == len(s):
            res.append(temp.copy())
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i) == False: continue
            temp.append(s[index:i+1])
            self.dfs(i+1, s, temp, res) #index still start, dfs for end of substr
            temp.pop()
    
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
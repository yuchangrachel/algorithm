#72.Edit Distance
# TOP-BOTTOM DP
def minDistance(self, word1: str, word2: str) -> int:
        #TOPIC:minimum number of operations convert word1 to word2, operations include insert/delete/replace
        if len(word1) == 0: return len(word2) #insert all word2
        if len(word2) == 0: return len(word1) #delete all word1
        
        # CREATE MEMO 2D for two strings
        # memo[i][j] mean word1 ending i and word2 ending j minimum steps to match
        memo = [[0 for j in range(len(word2))] for i in range(len(word1))]
        return self.helper(memo, word1, 0, word2, 0)
        
def helper(self, memo, word1,i, word2, j):
        # terminate case 
        if i == len(word1): return len(word2) - j #still left some step becoming word2
        if j == len(word2): return len(word1) - i
        # CHECK MEMO
        if memo[i][j] > 0: return memo[i][j]
        # SET VARIABLE
        res = 0
        # CHECK VALID
        if word1[i] == word2[j]:
            #RETURN right away
            #there is no any operation
            return self.helper(memo, word1, i+1, word2, j+1) 
        else:
            #insert word2[j], skip word[j], see j+1
            insert = self.helper(memo, word1, i, word2,j+1)
            #delete word1[i] see i+1
            delete = self.helper(memo, word1, i+1, word2, j)
            #replace both move forward
            replace = self.helper(memo, word1, i+1, word2, j+1)
            res =min(insert, min(delete, replace)) + 1
        memo[i][j] = res
        return memo[i][j]
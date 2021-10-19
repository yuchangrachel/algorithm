def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n: return []
        
        res = []
        self.helper(n, k, 1, [], res)
        return res
    
def helper(self, n, k, index, inner, res):
        # terminate case
        if len(inner) == k:
            res.append(inner.copy())
            return
        
        for i in range(index, n+1):
            inner.append(i)
            # dfs 
            self.helper(n,k,i+1, inner, res)
            # remove last ele in inner
            inner.pop()
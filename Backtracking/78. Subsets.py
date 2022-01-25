'''
    TOPIC:backtracking for display all result for subsets, so use recursion backtracking
        []
        /\
     [1] [2] [3]
    /\ 
    [1.2],[1,2,3]
    COMPELEXITY:T:O(N*2^N) S:O(N) not include output array(2^N)
    STEP:
    1.create dfs helper(index,inner)
    2.in dfs, n base case to return
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, nums, [], res)
        return res
        
    def dfs(self, index, nums, inner, res):
        res.append(inner.copy())
        for i in range(index, len(nums)):
            inner.append(nums[i])
            self.dfs(i+1, nums, inner, res)
            inner.pop()
        
        
# Time Complexity O(n^k) which is the same as (n C k)
# Space Complexity O(n^k)

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
            
'''
Combination Sum
each ele can reuse
Time: O(inputArrLEN ^ Target)
We may do length of arr, |arr|, work at each recursive level, and the height of each recursive tree is at most size of target, t

var combinationSum = function(candidates, target) {
    if (candidates == null || candidates.length == 0) return []
    
    candidates.sort((a,b) => a-b)
    const res = []
    
    dfs= function(index, inner, remain){
        if (remain < 0) return
        else if  (remain == 0){
            res.push([...inner])
            return
        }
        else {
        for(let i = index; i < candidates.length; i++){
            inner.push(candidates[i])
            remain -= candidates[i]
            dfs(i, inner, remain)
            remain += candidates[i]
            inner.pop()
        }
        }
    }
    dfs(0, [], target)
    return res
};

Combination sum ii
avoid duplicate and each ele use one times
var combinationSum2 = function(candidates, target) {
    if (candidates == null || candidates.length == 0) return []
    const res = []
    candidates.sort((a,b) => a-b)
    
    dfs=function(index, inner,remain){
        if (remain < 0) return
        else if (remain == 0){
            res.push([...inner])
            return
        }
        else{
            for (let i= index; i < candidates.length; i++){
                if (i > index && candidates[i] == candidates[i-1]) continue
                else{
                    inner.push(candidates[i])
                    dfs(i+1, inner, remain -= candidates[i])
                    remain+= candidates[i]
                    inner.pop()
                }
            }
        }
        
    }
    dfs(0,[], target)
    return res
};
'''

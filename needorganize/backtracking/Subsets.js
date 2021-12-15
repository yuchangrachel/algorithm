//78.Subsets
//unique elements
var subsets = function(nums) {
    //TOPIC: backtracking
    /*
                 []
                 /\
               [1] [2] ...
              /   \ 
            [1,2] [1,3]
            /
         [1,2,3]       
COMPELEXITY:T:O(N*2^N) S:O(N) not include output array(2^N)
*/
    if (nums == null || nums.length == 0) return []
    const res = []
    dfs=function(index, inner){
        res.push([...inner])
        
        for(let i = index; i < nums.length; i++){
            inner.push(nums[i])
            dfs(i+1, inner)
            inner.pop()
        }
    }
    
    dfs(0, [])
    return res
};
console.log(subset([1, 2, 3]));


//90. Subsets II
//Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
//The solution set must not contain duplicate subsets. Return the solution in any order.



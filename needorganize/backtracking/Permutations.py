# 46.Permutation
def permute(nums):
        if not nums or len(nums) == 0: return []
        
        self.res = []
        self.visited= [False] * len(nums)
        # inner function / in JS, called closure
        def dfs(inner, index):
            # terminate case
            if index == len(nums):
                self.res.append(inner.copy())
                return
            else:
                for i in range(len(nums)):
                    if self.visited[i]: continue
                    else:
                        inner.append(nums[i])
                        self.visited[i] = True
                        dfs(inner, index+1)
                        inner.pop()
                        self.visited[i] = False     
        dfs([], 0)
        return self.res

'''
99.Subset (avoid duplicate result)
var permuteUnique = function(nums) {
    if (nums == null || nums.length == 0) return []
    
    //sort first avoid duplicate
    nums.sort((a,b)=> a-b)
    const res = []
    const visit = new Array(nums.length).fill(false)
    
    dfs = function(index, inner){
        if (index == nums.length){
            res.push([...inner])
            return
        }
        for(let i = 0; i < nums.length; i++){
            if (visit[i]) continue
            if (i > 0 && nums[i] == nums[i-1] && !visit[i-1]){ 
                //WHY? beacause 1(0i),1(1i),2 (T->T->T)(WANT) 1(1i),1(0i), 2(F, T, T)(AVOID)
                continue
            }
            else{
                visit[i] = true
                inner.push(nums[i])
                dfs(index+1, inner)
                visit[i] = false
                inner.pop()
            }
        
        }
    }
    dfs(0, [])
    return res
};

'''

'''
784. Letter Case Permutation
    LOGIC:
    if, else if for covert current char -> opposite case dfs
    no matter character cases(since need add original case) and digits, will dfs again
    T/S:O(n*2^strlen)  each letter two choices, so will have 2^letter
'''
def letterCasePermutation(s):
        res = []

        def helper(index, inner):
            if index == len(s):
                res.append(''.join(inner[:]))
                return

            if s[index] >= 'a' and s[index]<= 'z': #change lower to upper
                inner.append(s[index].upper())
                helper(index+1, inner)
                inner.pop()
            
            elif s[index] >= 'A' and s[index]<= 'Z': #change lower to upper
                inner.append(s[index].lower())
                helper(index+1, inner)
                inner.pop()
            
            # no matter letter or digit
            inner.append(s[index])
            helper(index+1, inner)
            inner.pop()

        helper(0, [])
        return res
    
print(letterCasePermutation("123"))

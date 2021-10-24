# 46.Permutation
# 1WAY
def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        
        res = []
        # need visited boolean list for mark down T/F for traverse whole array start iver
        visited = [False] * len(nums)
        self.helper(nums, 0, [], res, visited)
        return res
        
def helper(self, nums, index, inner, res, visited):
        # terminate case
        if index == len(nums):
            # 1WAY FASTER res.append(inner.copy())
            # 2WAY
            res.append(inner[:])
            return
        
        for i in range(0, len(nums), 1):
            if visited[i]: # use for traversal start over
                continue
            else:
                visited[i] = True
                inner.append(nums[i])
                self.helper(nums, index+1, inner, res, visited) # use index tracker, not i, because i for track visited and insert, index for backtrack
                inner.pop()
                visited[i] = False
#2WAY
def permute(self, nums: List[int]) -> List[List[int]]:
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
784. Letter Case Permutation
    LOGIC:
       [a1b2]
    1rec:[A] [A1] [A1B] [A1B2] pop pop
    2rec:[A1b2]....
    T/S:O(n*2^letter)  each letter two choices, so will have 2^letter
'''
def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []

        def helper(index, inner):
            if index == len(s):
                self.res.append(''.join(inner[:]))
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
        return self.res
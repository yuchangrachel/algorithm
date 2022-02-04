'''
    topic:three sum [i]+[j]+[k] < [y] index order:i<j<k<y;accept duplicate truplets
    ATT:index does matter, cannot sort, then no binary search
    Brute force: O(n^4)
    '''
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)-1, 2,-1): # target
            for j in range(i-1, 1,-1): # third
                if nums[j] >=nums[i]:
                    continue
                else:
                    for k in range(j-1, 0, -1):
                        if nums[k] >= nums[i]:
                            continue
                        else:
                            for y in range(k-1, -1, -1):
                                if nums[y] + nums[k] + nums[j] == nums[i]:
                                    res += 1
        return res
    
    # O(n^2)
    def countQuadruplets(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        l = len(nums)
        count[nums[l-1] - nums[l-2]] = 1
        res = 0
        
        for b in range(l-3, 0, -1):
            for a in range(b-1, -1, -1):
                res += count[nums[a] + nums[b]]
            
            for x in range(l-1, b, -1):
                count[nums[x] - nums[b]] += 1
        return res
    
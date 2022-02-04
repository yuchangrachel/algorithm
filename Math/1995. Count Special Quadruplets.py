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
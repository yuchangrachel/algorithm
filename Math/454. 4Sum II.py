'''
    TOPIC: like 2sum
    STEP:brute force O(n^4) -> O(n^2)store A+B in map {total:freq}, then when iterate C+D=sum, see if 0-sum already in map
    '''
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        mapping = collections.defaultdict(int)
        for n in nums1:
            for n2 in nums2:
                mapping[n+n2] += 1
        
        for n in nums3:
            for n2 in nums4:
                target = 0-(n+n2)
                res += mapping[target]
                # if mapping[target] > 0:
                #     res += 1
                #     mapping[target] -= 1
        return res
            
        
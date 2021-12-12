#560. Subarray Sum Equals K
'''
    TOPIC: prefix sum
    1WAYbrute force STEP: TLE
    1.create sum array, one loop sum[i] = cur + sum[i-1]
    2.second loop which is nested loop, find inner array may has res
    !CANNOT USE SLIDING WINDOW because have positive and negative [....-6],k=100, if > 100, but nextone is negative will cut down to 100
    2WAYhashmap STEP
    1.create map,add{0:1} case for sum-k exist
    2.check sum-k if in map, if yes, count += map.val; all cases, map.val+=1
'''
def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) ==0: return 0
        res = 0
        total = 0
        mapping = collections.defaultdict(int)
        mapping[0] = 1 # case sum-k already counted
        for n in nums:
            total += n
            if total - k in mapping:
                res += mapping[total-k]
            mapping[total] += 1
        return res
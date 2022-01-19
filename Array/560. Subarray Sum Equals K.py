'''
    TOPIC:positive/negative nums in array, find total number of subarray =k
    STEP:DONT USE SLIDING WINDOW SINCE positive/negative
    1.create hashmap {0:1} since total-k=0, here count 1
    2.iterate array, total += n, if total-k in map, res ++ 
    3.in iterate, map[total]+=1 (make subarray sum)
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = collections.defaultdict(int)
        mapping[0] = 1
        total = 0
        res = 0
        for n in nums:
            total += n
            if total - k in mapping:
                res += mapping[total-k]
            mapping[total] += 1
        return res
        
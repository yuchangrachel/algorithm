'''
    TOPIC:all positive integer prefix sum meet >= target
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        left = 0
        prefix = 0
        for i in range(len(nums)):
            # update
            prefix += nums[i]
            # handle left
            while prefix >= target:
                # meet require/get result
                res = min(res, i - left + 1)
                prefix -= nums[left]
                left += 1

        return 0 if res == len(nums) + 1 else res
                
                
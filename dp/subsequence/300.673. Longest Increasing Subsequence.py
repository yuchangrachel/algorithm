#300. Longest Increasing Subsequence
def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums), 1):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        
        return max(dp)
    
#673. Number of Longest Increasing Subsequence
def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums) # length store longest ending at nums[i]
        count = [1] * len(nums) # count store the number of longest at nums[i]
        
        for i in range(len(nums)):
            for j in range(0, i, 1):
                if nums[j] < nums[i]:
                    if length[i] < length[j] + 1:
                        # update because find longer one
                        length[i] = length[j] + 1
                        # update count
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        # another same result
                        # print(length[i], " ", length[j]+1)
                        count[i] += count[j]
        maxlen = max(length)
        print(length)
        print(count)
        return sum([count[i] for i in range(len(nums)) if maxlen == length[i]]) # consider[2,2,2,2,2] => 5
    
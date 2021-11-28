# 643. Maximum Average Subarray I
def findMaxAverage(nums,k):
        # TOPIC: find maximum average subarray k size 
        # subarray is contiguous array having start and end point, k size, so it is fixed-size window, using sliding window
        if not nums or len(nums) == 0 or k == 0: return 0.0
        
        max_sum = float("-inf")
        left = 0
        i = 0
        while i < len(nums):
            #check reach window size, if not add num into window
            if i - left + 1 == k:
                temp = sum(nums[left: i+1])
                print("sum ", nums[left: i+1])
                if temp > max_sum: max_sum = temp
                i+=1
            elif i - left + 1 < k:
                i+=1
            else:
                # move left pointer
                left += 1
        return max_sum 

print(findMaxAverage([-1],1))
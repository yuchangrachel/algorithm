'''
645.Set Mismatch.py
    TOPIC:sorted array[1..n], return[repetition, miss]
    1WAY:hashmap
    2WAY:revert +->-, or ->+ use index get previous is duplicate or not
    if nums[abs(n)-1] < 0: find duplicate, update nums[abs(n-1)] = abs(n)
    second pass, find miss, if nums[i] > 0, return i+1
'''
def findErrorNums(nums):
        res = [0] * 2
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res[0] = abs(n)
            else:
                nums[abs(n)-1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i + 1
        return res
                
print(findErrorNums([2,2]))


 '''
 287. Find the Duplicate Number
    TOPIC:find only one duplicate which appears two or more times, S:O(1) FOLLOWUP?
    STEP:No extra space, think Binary Search, think relation about index and ele
    1.left=1,right=len(nums)
    2.mid as index(also ele), check loop all nums array, count <=mid, if yes, mean duplicate on the right
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            count = 0
            
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
        
        
        
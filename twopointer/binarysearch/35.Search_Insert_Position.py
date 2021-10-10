def searchInsert(nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

print(searchInsert([1,3,5,6], 7)) #4
print(searchInsert([1], 0)) #0
print(searchInsert([1,3,5,6], 0)) #0
print(searchInsert([1,3,5,6], 2)) #1
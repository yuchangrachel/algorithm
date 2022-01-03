'''
    TOPIC:find index, sum of left side = sum of right side:prefix sum
    STEP:
    1.get wholesum, if (wholesum-curNum) =subtotal, if [...curNumIndex-1] == subtotal,return curNumIndex
'''
def pivotIndex(nums):
        total = sum(nums)
        for i in range(len(nums)):
            subtotal = (total - nums[i])
            if subtotal % 2 != 0:
                continue
            else:
                print(subtotal)
                if sum(nums[:i]) == subtotal // 2:
                    return i
        return -1
print(pivotIndex([-1,-1,-1,-1,-1,-1])) # -1
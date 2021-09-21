def sortedSquares(nums):
    # 1SOLUTION: built-in method
    for i in range(len(nums)):
        nums[i] *= nums[i]
    return sorted(nums)

# PY KNOWLEDGE
# sorted(list) return new list; list.sort(): no return, sort original list
        
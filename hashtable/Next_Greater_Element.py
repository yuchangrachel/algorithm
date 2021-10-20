# 1WAY brute force O(n^2)
# 2WAY monotonic stack
from collections import deque
class Solution:
    '''
    LOGIC:
    Monotonic stack
    use stack starting from last index of nums2, if cur > stack.top, stack.pop()(since impossible to use it)
    check stack is empty or not, if yes map[n] = -1; otherwise map[n] = top
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        
        res = [None] * len(nums1)
        stack = deque() # store greater index of nums2
        dic = {}
        
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                stack.pop()
                   
            if len(stack) <= 0:
                dic[nums2[i]] = -1
            else:
                dic[nums2[i]] = nums2[stack[-1]]
            stack.append(i)
        
        #handle result
        for i in range(len(nums1)):
            res[i] = dic[nums1[i]]
            
        return res
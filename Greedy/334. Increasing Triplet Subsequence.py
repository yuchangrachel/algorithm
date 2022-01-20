'''
    TOPIC:need three increasing subsequence i<j<k and nums[i]<nums[j]<nums[k]
    STEP:T:O(n) Number compare
    1.set n1, n2 both max, if see cur <= n1(=because count n1, not for n2), update cur; else if cur <= n2, update cur; else if cur > n1,n2, return true
    '''
    def increasingTriplet(self, nums: List[int]) -> bool:
        if nums is None or len(nums) < 3: return False
        n1 = float("inf")
        n2 = float("inf")
        for n in nums:
            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n
            elif n > n1 and n > n2:
                return True
        return False
        
              
print(increasingTriplet([5,4,3,2,1]))
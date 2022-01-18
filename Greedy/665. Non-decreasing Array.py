'''
    TOPIC:SORT,only change at most one to make non-decreasing array
    STEP:
    1.create two array one(1st option) two(2nd option), use one time reassign
    2.if compare neighbor, order not correct, let one[i] store smaller, let two[i+1] store bigger, break
    3.finally compare two array if same as sorted. one or two
    '''
    def checkPossibility(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0: return True
        one = nums[:]
        two = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = nums[i+1]
                two[i+1] = nums[i]
                break
                       
        return one == sorted(one) or two == sorted(two)
        
        
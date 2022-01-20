'''
    TOPIC: one,zero,two pointers do partitions, one as track whole input array.while one < two
    '''
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        one = 0
        two = len(nums)
        while one < two:
            if nums[one] == 2:
                #swap with two
                two -= 1
                nums[one], nums[two] = nums[two], nums[one]
            elif nums[one] == 1:
                one += 1
            elif nums[one] == 0:
                zero += 1
                nums[zero], nums[one] = nums[one], nums[zero]
                one += 1
            
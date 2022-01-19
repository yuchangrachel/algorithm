'''
        接多少水是由比较低的柱子决定的。if left shorter, move left; 对左边，记录遇到的最高的柱子leftHeight, 遇到 height[left] <= leftHeight 说明可以接到水，否则让leftHeight = height[left], 右边的柱子同理
        '''
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0: return 0
        water = 0
        left = 0
        right = len(height) -1
        leftmost = height[left]
        rightmost = height[right]
        
        while left < right:
            if height[left] <= height[right]:
                left += 1 #wanna skip first one since no two slates hold water
                if height[left] > leftmost:
                    leftmost = height[left]
                else:
                    #hold water
                    water += (leftmost - height[left])
            else:
                right -=1
                if height[right] > rightmost:
                    rightmost = height[right]
                else:
                    # hold right water
                    water += (rightmost - height[right])
        return water
        
        
'''
    TOPIC:find two lines make containers can store maximum water.
    STEP: left right pointer, updating min(height) * (right - left), who shorter, moveon until left meet right
    '''
    def maxArea(self, height: List[int]) -> int:
        if height is None or len(height) == 0: return 0
        maxi = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxi = max(maxi, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else: right -= 1
        
        return maxi
            
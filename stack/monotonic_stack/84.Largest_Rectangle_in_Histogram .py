def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        if decreasing one: if meet larger ele than top, need to handle
        In here, we use increasing one. handle smaller one. store big ele's index into stack, if meet smaller one,
        2WAY:monotonic stack
        two kinds of stack: strictly increasing monotonic stack OR strictly decreasing monotonic stack
        if increasing one: if meet smaller ele than top, need to handle 
        '''
        if not heights or len(heights) == 0: return 0
        
        stack = []
        stack.append(-1) # as left border
        res = 0
        
        for i in range(len(heights)):
            # if stack has at least two elements
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                left = stack[-1]
                # set left(top_index) and right border(i index) and remove i-index bar
                res = max(res, heights[top] * (i - left - 1))
            
            stack.append(i)
            
        # last rectangle the right border is heights.length(NOT LAST INDEX, IT IS LAST INDEX+1)
        while stack[-1] != -1:
            res = max(res, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    
        return res
        
        '''
        TLE
        1WAY:native method FIND one of peaks
        traverse height, find one peak mean [i] < [i+1], then traverse the front part; find 6 as one of peaks so far, traverse 5,1,2. min(6,5)find shorter value consisting of rectangler
        TIME:O(n^2)
        '''       
#         res = 0
#         for i in range(0, len(heights), 1):
#             if i+1 < len(heights) and heights[i] <= heights[i+1]:
#                 continue # keep looking for one of peaks
#             else:
#                 peak = heights[i]
#                 # find first one peak
#                 for j in range(i, -1, -1):
#                     peak = min(peak, heights[j])
#                     res = max(res, (i-j+1)*peak)
        
#         return res
                
#48. Rotate Image
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #TOPIC:rotate clowise from outer layer to inner layer
        #TIME:O(n*n), actually rotate is n-1, since last is second rorate
        #STEP:
        #1.l and r control outer layer, l++, r-- go to inner layer
        #2.second loop while i < r-l control, closewise operation, from one cell to another
        if not matrix or len(matrix) == 0: return
        
        l = 0
        r = len(matrix)-1
        while l < r:
            top =l
            bottom = r
            
            for i in range(r-l):
                topleft = matrix[top][l+i] # only need this one temp variable for doing anti-clockwise
                #bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                #bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                # top left to top right
                matrix[top+i][r] = topleft
            l+=1
            r-=1
        
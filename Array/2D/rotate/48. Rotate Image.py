#48. Rotate Image
'''
    TOPIC:rotate clock wise outer layer to inner layer
    STEP:
    1.first loop(l < r) :start four corner
    2.in loop, assgin top, bottom, while loop i < r-f, i is diff, i+pos point to next pos in the same layer
    3.store topleft, anticlowise replace slot
'''
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0] or len(matrix) == 0 or len(matrix[0]) == 0: return
        l = 0
        r = len(matrix) - 1
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
        
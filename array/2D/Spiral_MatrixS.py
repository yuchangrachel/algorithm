#54. Spiral Matrix
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #TOPIC:Snake-like traverse 2D array
        #STEP:
        #1.left,right,top,bottom,Think boundary
        #2.Think corner case:[1,2,3]
        if not matrix or not matrix[0] or len(matrix) == 0 or len(matrix[0]) == 0: return []
        
        res =[]
        l = 0
        r = len(matrix[0]) #corner case:[[1],[2],[3]]
        top= 0
        bottom=len(matrix) #corner case:[[1,2,3]]
        
        while l < r and top < bottom:
            # iterate first row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            
            # iterate last col
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1
            
            #consider [1,2,3],[[1],[2],[3]]
            if not l<r or not top < bottom: break
            
            # iterate last col in spiral order
            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # iterate first col in spiral order
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1
            
        return res

#59. Spiral Matrix II
def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return [[]]
        
        #create initial 2d array n*n
        matrix =[[0 for j in range(n)] for i in range(n)]
        
        l = 0
        r = len(matrix[0])
        top = 0
        bottom = len(matrix)
        start = 1
        while l < r and top < bottom:
            for i in range(l, r):
                matrix[top][i] = start
                start+= 1
            top+=1

            for i in range(top, bottom):
                matrix[i][r-1] = start
                start+=1
            r -= 1
            
            if not l < r or not top < bottom: break
                
            for i in range(r-1, l-1, -1):
                matrix[bottom-1][i] = start
                start += 1
            bottom -=1
            
            for i in range(bottom-1, top-1, -1):
                matrix[i][l] = start
                start += 1
            l += 1
            
        
        return matrix
            
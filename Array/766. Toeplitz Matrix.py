'''
    TOPIC:traverse matrix diagnosely from bottom left to top-right
    STEP:
    1 2 3 4
    5 1 2 3
    9 5 1 2
    start point track:9->5->1->2->3->4 first column meet [0,0] go first row
    STEP:
    1.outerloop handle start point, rowIndex go up(-), if meet rowIndex=0, columnIndex go right (+)
    2.innerloop iterate diagnose all val, need another two pointer(wont use in outerloop anymore)
    '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix) 
        n = len(matrix[0])
        p = m-1
        q = 0
        while p >= 0 and q < n:
            val = matrix[p][q]
            i=p+1
            j=q+1
            while i <m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
            if p > 0: #still in first column
                p -= 1
            else:
                q += 1
        return True
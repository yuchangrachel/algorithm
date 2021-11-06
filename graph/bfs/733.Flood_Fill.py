from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        LOGIC:
        1.When change color: if origin!=newcolor, and bfs, change neighbor who has same color as origin
        '''
        if not image or len(image) == 0 or image[sr][sc] == newColor: return image
        
        q = deque()
        q.append((sr, sc))
        origin = image[sr][sc]
        image[sr][sc] = newColor
        
        dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
        
        while len(q) > 0:
            size = len(q)
            index = 0
            while index < size:
                top = q.popleft()

                for d in dir:
                    x = top[0] + d[0]
                    y = top[1] + d[1]
                    
                    # check new coordinate is valid 
                    if x < 0 or y < 0 or x >= len(image) or y >=len(image[0]) or image[x][y] != origin:
                        continue
                    else:
                        image[x][y] = newColor
                        q.append((x,y))
                index += 1
        
        return image
                
#661. Image Smoother
import copy
def imageSmoother(img):
        # TOPIC： 2D array refill values, each value is average from 8 neighbors and itself
        # HOW: calculate average, change cur val
        if not img or not img[0] or len(img) == 0 or len(img[0]) == 0: return img
        
        # store copy of 2d array, change temp, keep origin 2d array
        # consider shadow copy or deep copy
        temp = copy.deepcopy(img)
        
        dir =[[1,0],[-1,0], [0,1], [0,-1], [-1,-1], [1,1], [-1, 1], [1,-1]] #8 directions
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                total = img[i][j] # count itself first
                count = 1 # count itself first
                
                for d in dir:
                    #check neighbor boundary
                    x = d[0] + i
                    y = d[1] + j
                    if x < 0 or y < 0 or x >= len(img) or y >= len(img[0]):
                        continue
                    else:
                        count +=1
                        total += img[x][y]
                
                # update val in temp
                temp[i][j] = total // count
        
        return temp
                    
print(imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
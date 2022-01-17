'''
    TOPIC:Greedy, plant flower in empty plots as much as it can.
    STEP:compare two neighbors,10001, 100, 001, Not need bidirectional. Need assign array(0->1)
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True #no flower but can place flower
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and i+1 < len(flowerbed) and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n-=1
            else:
                if i-1>= 0 and i+1< len(flowerbed):
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
        
        return n <= 0
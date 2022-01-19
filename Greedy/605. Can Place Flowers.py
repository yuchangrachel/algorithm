'''
    TOPIC:Greedy, plant flower in empty plots as much as it can.
    STEP:compare two neighbors,10001, 100, 001, Not need bidirectional. Need assign array(0->1)
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
        

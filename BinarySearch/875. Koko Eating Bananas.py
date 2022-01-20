'''
    TOPIC:Binary Search
    STEP:
    1.each hour only can eat one piles, so len(piles) <= h, maximum k is max(pile), will finish within len(piles),k=[1...max(pile)]
    2.brute force, iterate piles with k=[1...max(pile)] max(pile)times, TIME O(max(pile)times * len(pile))
    3.optimize binary search for k range TIME O(log(max(pile))time * len(pile))
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find max of pile
        low = 1
        high = max(piles) # TIME O(len(pile))
        res = high
        while low <= high:
            k = (low + high) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / k)

            if hour > h:
                low = k+1
            else:
                res = min(res, k)
                high = k-1

        return res
                    
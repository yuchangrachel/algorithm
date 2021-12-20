'''
    LOGIC:interval problem 
    STEP:
    1.Iterate over timeSeries list. At each step add to the total time the minimum between interval length and the poisoning time duration duration.
    2.return total+duration
'''
def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or len(timeSeries) == 0: return 0
        res = 0
        for i in range(len(timeSeries) - 1):
            res += min(timeSeries[i+1]-timeSeries[i], duration)
        return res + duration
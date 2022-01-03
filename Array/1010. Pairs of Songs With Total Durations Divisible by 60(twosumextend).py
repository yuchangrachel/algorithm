'''
    TOPIC:return number of pair sum up can be divisible by 60(similiar two sum)
    IDEA:math statistic: combination find same one except myself:n*(n-1)/2 times; combination find two different sum up to oneVar:a*b times
    STEP:[30,20,150,100,40] =>%60 [30,20,30,40,40], after mode 0<= <60
    [30,30,30]=>res:3 OR[90,90,90]
    1.create countmap {x%60, freq}
    2.special reminders:0, 30, can make pair by themself, freq*(freq-1) / 2(divide by 2 mean only count -> )
    3.for loop half(0,30) check other reminders:count[15] * count[45]
    '''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        counter = collections.Counter([n%60 for n in time])
        
        if 0 in counter:
            res += counter[0] * (counter[0] - 1) // 2
            del counter[0]
        if 30 in counter:
            res += counter[30] * (counter[30] - 1) // 2
            del counter[30]
        
        for i in range(30):
            if i in counter and (60-i) in counter:
                res += counter[i] * counter[60-i]
        
        return res
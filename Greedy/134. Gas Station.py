'''
    TOPIC:circlur gas station
    STEP:
    1.Total gas > 0(not must=0, can perfect use up) mean has start;otherwise return -1
    2.iterate, tempsum += gas[i]-cost[i], if tempsum < 0:find next start point
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tempsum = 0
        start = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tempsum += gas[i] - cost[i]
            if tempsum < 0:
                start = i + 1
                tempsum = 0
            
        return start if total >= 0 else -1
            
        
        
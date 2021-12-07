class MinStack:
    '''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    '''
    def __init__(self):
        self.s = []
        self.miner = [] #store min stack, top always current min

    def push(self, val: int) -> None:
        self.s.append(val)
        
        if len(self.miner) > 0:
            if val <= self.miner[-1]: #must <=!!
                self.miner.append(val)
        else:
            self.miner.append(val) 

    def pop(self) -> None:
        if self.s.pop() == self.miner[-1]:
            self.miner.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.miner[-1]

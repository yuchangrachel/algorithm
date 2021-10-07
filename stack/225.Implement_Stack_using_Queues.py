from collections import deque
class MyStack:
    # two queues
    def __init__(self):
        self.q = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        while len(self.q) > 0: # q[1]. q[2,1]
            self.q2.append(self.q.popleft()) #q[] q2[1] . q[] q2[2,1]
            
        self.q.append(x) # q[2]. q[3]
        
        while len(self.q2) > 0: #q2[]
            self.q.append(self.q2.popleft()) #q[2,1] . q[3,2,1]

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

from collections import deque
class MyStack:
    #TOPIC: use two queues, q1(main) insert new ele, q2 store existed q1's elements
    #HOW: clean q1-> store into q1 -> insert new ele in q1 -> q2 move all elements back to q1

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        #when push new into q1, clean q1, pop all into q2
        while self.q1:
            first = self.q1.popleft()
            self.q2.append(first)
        self.q1.append(x)
        #after new in q1, clean q2, pop all back into q1
        while self.q2:
            first = self.q2.popleft()
            self.q1.append(first)

    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0


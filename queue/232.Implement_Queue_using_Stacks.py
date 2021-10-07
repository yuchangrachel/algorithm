class MyQueue:
    # two stacks implement queue. stack=[1,2,3], should return 1
    # when s1 have something pop all, s2 push all. s1 add new. pop s2 , push s1
    def __init__(self):
        self.stack = [] 
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack) != 0:    
            self.stack2.append(self.stack.pop()) # s2[1] s1[]->s2[1,2]
    
        self.stack.append(x) # s1:[1] -> [] -> s1:[2] -> s1:[3]
    
        while len(self.stack2) != 0: # s2[] s1[1] -> s1[2,1] -> s1[3,2,1]
            self.stack.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
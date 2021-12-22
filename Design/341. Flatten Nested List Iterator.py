'''
TOPIC:Flatter nested List Iterator(iterator use iterate way / recursion with stack helper)
STEP:
1.create stack handle whole nested list reversely, wanna pop first ele. stack(default nested list), but later ONLY store int.NOT list.
2.for next behavior: pop top
3.for hasNext behavior:while stack loop, if find int, pop rightaway, otherwise it is list, store list reversely in stack
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        
    def next(self) -> int:
        if self.hasNext():
            if self.stack[-1].isInteger():
                return self.stack.pop().getInteger()
            else:
                #next is list, flat them store in stack
                while self.stack and not self.stack[-1].isInteger():
                    self.stack.append(self.stack.pop().getList()[::-1])
    
    def hasNext(self) -> bool:
        while len(self.stack) > 0:
            top = self.stack[-1] #need use later 
            if top.isInteger():
                return True
            self.stack.pop()
            #top is list
            for i in range(len(top.getList())-1, -1, -1):
                self.stack.append(top.getList()[i])
        return False
    
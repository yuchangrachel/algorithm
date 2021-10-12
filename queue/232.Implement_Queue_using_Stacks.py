'''
current queue=[1,2], will add 3
s1=[2,1] s2=[] => s1=[3],s2=[1,2] => s1=[3,2,1] s2=[]
class MyQueue{
    constructor(){
        this.s1=[]
        this.s2=[]
    }
    push(x){ //return void
        //handle s1, s2, push and pop here
        while(this.s1.length > 0){
            this.s2.push(this.s1.pop())
        }
        this.s1.push(x)
        while(this.s2.length > 0){
            this.s1.push(this.s2.pop())
        }
    }
    pop(){//return number
        return this.s1.pop()
    }
    peek(){//return number
        return this.s1[this.s1.length - 1]
    }
    empty(){//return boolean
        return this.s1.length == 0
    }
}
/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
'''


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
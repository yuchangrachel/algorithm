import math
'''
    TOPIC:use STACK do math operation
    ATT!str's negative.isdigit() return false "-11"->return False
    ATT!for division: if division < 0: use math.ceil 3/-123=0. if division >=0: use math.floor 12/5=2
'''
def evalRPN(tokens):
        stack = []
        
        for token in tokens:
            print(stack)
            if token in '+-*/':
                top1=stack.pop()
                top2=stack.pop()
                if token == "+":                        
                    stack.append(top1+top2)
                elif token == "-":
                    stack.append(top2-top1)
                elif token == "*":
                    stack.append(top2*top1)
                elif token == "/":
                    if top2 / top1 < 0:
                        stack.append(math.ceil(top2/top1))
                    else:
                        stack.append(math.floor(top2/top1))
            else:
                stack.append(int(token))
        
        return stack[-1]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
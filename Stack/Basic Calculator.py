'''
224. Basic Calculator I
    LOGIC:STACK
    ATT:DONT use for i in range() inside have while i+1 loop, i won't update to outerloop
    STEP:
    1.create res store add/subtrate all number, sign(1,-1), stack
    2.when meet (, store prev res and sign into stack, then reset res and sign
    3.when meet ), pop twice, think simulation:3-(11-2) 4.see sign, update sign 5.see digit, add into res
'''
def calculate(ls):
        #create res add/substract all
        res = 0
        sign = 1
        stack = []
        i = 0
        
        while i < len(ls):     
            if ls[i].isdigit():
                temp = int(ls[i])
                #check maybe multiple digits number
                while i+1 < len(ls) and ls[i+1].isdigit():
                    temp = temp*10 + int(ls[i+1])
                    i += 1
                res += temp * sign
            elif ls[i] == "+":
                sign = 1
            elif ls[i] == "-":
                sign = -1
            elif ls[i] == "(":
                # store res&sign, then reset res&sign
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ls[i] == ")": # it is valid expression,(inside must have >=2 numbers)
                res = stack.pop() * res + stack.pop() 
            
            i += 1
            
        return res

# print(calculate("1 + 1"))

'''
227. Basic Calculator II
    TOPIC:stack, have +,-,*,/
    STEP:
    1.set variable:curnumber,res,operator,stack[]
    2.when num, add cur; meanwhile also check the operator before it
'''
import math
def calculate2(s):
        res = 0
        i = 0
        stack = []
        num = 0 #each time meet operator reset
        opt = "+" #store operator before cur
        while i < len(s):
            if s[i].isdigit():
                temp = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    temp = temp*10 + int(s[i+1])
                    i += 1               
                num += temp
            if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/" or i == len(s) - 1:
                if opt == "+":
                    stack.append(num)
                elif opt == "-":
                    stack.append(-num)
                elif opt == "*":
                    stack.append(stack.pop() * num)
                elif opt == "/":
                    if stack[-1] * num < 0:
                        stack.append(math.ceil(stack.pop() / num))
                    else:
                        stack.append(math.floor(stack.pop() / num))
                
                if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                    opt = s[i]
                num = 0
            
            i += 1
            print(stack)
        while len(stack) > 0:
            res += stack.pop()
        return res

print(calculate2("14-3/2"))
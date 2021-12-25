'''
224. Basic Calculator I
    LOGIC:STACK
    ATT:DONT use for i in range() inside have while i+1 loop, i won't update to outerloop
    STEP:
    1.create res store add/subtrate all number, sign(1,-1), stack
    2.when meet (, store prev res and sign into stack, then reset res and sign
    3.when meet ), pop twice, think simulation:3-(11-2) 4.see sign, update sign 5.see digit, add into res
'''
def calculate(self, ls: str) -> int:
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

print(calculate("1 + 1"))

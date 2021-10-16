def isValid(s):
    if not s or len(s) == 0: return False
        
    stack = []
    for c in s:
        if c == '(' or '[' or '{':
            stack.append(c)
        else:
            if len(stack) == 0: 
                return False
            else:
                top = stack[-1]
                if (top =='(' and c ==')') or (top=='[' and c ==']') or (top=='{' and c=='}'):
                    stack.pop()
                else:
                    return False
    print(stack)
    return len(stack) == 0

print(isValid("()"))
def decodeString(self, s: str) -> str:
        '''
        REFER: https://www.youtube.com/watch?v=qB0zZpBJlh8
        LOGIC: k[k[k[]]] or k[k[]k[]k[]] subproblems -> do recursion, stack store do memorization
        HOW:
        k maybe more than one digits
        num is in front of [ open bracket
        stack store k, [, char, [char]result
        '''
        
        if not s or len(s) == 0: return ""
        
        stack = []
        
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr =""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #pop open bracket
                #now handle digits
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substr)
        return "".join(stack)
                
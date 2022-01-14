'''
    TOPIC:Extract Integer
    STEP:
    1.handle leading 0 and trailing 0 USE lstrip,rstrip
    2.+ - need appear first
    3.int need appear before others
    '''
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        sign = 1
        base = 0
        
        # trim leading white space and trailing white space
        s = s.lstrip()
        s = s.rstrip()
        i = 0
        digitFirst = False
        maxint = 2**31 - 1
        minint = -1*(2**31)

        while i < len(s):
            c = s[i]
            if c == "+" or c == "-": #determine positive or negative
                if i == 0:
                    if c == "-":
                        sign = -1
                else:
                    return 0                
            elif c.isdigit(): #digit, find substring will full of digits
                digitFirst = True
                while i < len(s) and s[i].isdigit():
                    base = base * 10 + int(s[i])
                    print(base)
                    i += 1
                
                break #dont need to traverse rest of string
            else:
                if digitFirst == False:
                    return 0
            i+=1
            
        if sign == 1:
            if sign * base > maxint:
                return maxint
            else:
                return sign * base
        else:
            if sign * base < minint:
                return minint
            else:
                return sign * base

print(myAtoi("words and 987"))
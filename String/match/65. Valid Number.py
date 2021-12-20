#65. Valid Number
'''
    TOPIC:Valid Number check all corner cases
    STEP:
    1.if has leading or trailing white space NOT affect valid number
    2.meet 'e':before e should numSeen. only one e
    2.meet '.':if eSeen True:False(beacause e+integer Power(not .)).only one dot
    3.meet "+" or "-":if not at index0 or [i-1]!=e: return false
'''
def isNumber(s):
        if not s or len(s) == 0: return False
        numberSeen = False
        dotSeen = False
        eSeen = False
        s = s.strip()

        for i in range(len(s)):
            print(s[i])
            if s[i].isdigit():
                
                numberSeen = True
            elif s[i] == "e" or s[i] == "E":
                if eSeen or numberSeen == False: return False
                eSeen = True
                numberSeen = False #need behind e (may not next behind)
            elif s[i] == ".":
                if eSeen or dotSeen: return False
                dotSeen = True #4.true
            elif s[i] == "+" or s[i] == "-":
                if i != 0 and s[i-1] != "e": return False
            else:
                return False #other input
        return numberSeen
                
print(isNumber("1E9"))
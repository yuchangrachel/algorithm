'''
    TOPIC:Implement check String.seperate two groups. sort
    STEP:
    1.Create two groups array, digit and letter
    2.for letter part, sort identifier first, then sort[1:]
    3.merge letter + digit
'''
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # create two groups digit and letter
        digit = []
        letter = []
        # first pass seperate two grups
        for log in logs:
            if log[-1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
                
        # sort letter group, first convert to array
        
        letter.sort(key=lambda x:x.split(" ")[0])
        letter.sort(key=lambda x:x.split(" ")[1:])
        return letter + digit
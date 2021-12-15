
def StringChallenge(strParam):
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    def getValue(temp):
        for i in range(10):
            if temp == numList[i]:
                return i
        return -1

    def numtochar(num):
        return numList[int(num)]
    
    check = ""
    number = ""
    numberlist = []
    for c in strParam:
        check += c
        val = getValue(check)
        if val >= 0 and val <= 9:
            number += str(val)
            check = ""
        if check == "plus" or check =="minus":
            numberlist.append(int(number))
            number = ""
            if check == "plus":
                numberlist.append(0)
            elif check == "minus":
                numberlist.append(1)
            check=""
    print(numberlist)            
    total = numberlist[0]
    for i in range(1, len(numberlist) - 1 , 2):
        if numberlist[i] == 0:
            total += numberlist[i+1]
        else:
            total -= numberlist[i+1]
    finalstring = ""
    if total < 0:
        finalstring += "negative"
    for i in range(len(number)):
        finalstring += numtochar(number[i])
    
    return finalstring

print(StringChallenge("onezeropluseight")) #18
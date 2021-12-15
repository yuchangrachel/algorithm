# 43. Multiply Strings
def multiply(self, num1: str, num2: str) -> str:
        #TOPIC: simulation for multiplication
        n1 = len(num1)
        n2 = len(num2)
        res = ["0"] * (n1+n2) #9*9=81
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                temp = int(res[i+j+1]) + product #cur multiple
                #update cur slot
                res[i+j+1] = str(temp % 10)
                #front slots
                res[i+j] = str(int(res[i+j]) + temp//10) #multiple alway single*single so res[i+j] must one char
        
        # now res may has leading0, eg."2"*"3"
        # how to avoid leading 0, create new result string, and check seen boolean
        result =""
        seen = False
        for c in res:
            if c == "0" and seen == False: continue
            else:
                result += c
                seen = True
        
        return result if len(result) != 0 else "0"
                
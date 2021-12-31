'''
    LOGIC:String match
    RULE:
    1.Greedy, as many words in one line as possible
    2.When Not in last line, spaces between words should distribute as evenly as possible, as left as possible
    3.In last line/only one word in the line, no extra space between words
    STEPS:
    1.Decide how many words could be put in the same line
    2.Modify space between words
    3.make space evenly, if cannot even, left most
    4.if last one/only one word
'''
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        index = 0
        while index < n:
            #1.check how many words and their gaps in one line
            totalChar = len(words[index])
                
            last = index+1 #last mean next line's first
            
            while last < n:
                if totalChar + len(words[last]) + 1 > maxWidth: break # totalchar+nextchar+ curchar's gap
                totalChar += 1 + len(words[last])
                last += 1
            #nextline index - cur index - 1 =gaps
            gaps = last - index - 1
                
            temp = []
            tempStrLen = 0

            #2.res's temp result add
            if last == n or gaps == 0: #this is last line or one word
                for i in range(index, last):
                    temp.append(words[i])
                    temp.append(" ")
                del temp[-1] #delete last char's space
                
                while len("".join(temp)) < maxWidth:
                    temp.append(" ")
            else: 
                spaces = (maxWidth - totalChar) // gaps
                rest = (maxWidth - totalChar) % gaps
                
                #adding gaps
                for i in range(index, last-1,1): #not include [last-1] because not space behind it
                    temp.append(words[i])
                    temp.append(" ")
                    #add extra more gaps
                    for i in range(0, spaces + (1 if i - index < rest else 0)):
                        temp.append(" ")
                temp.append(words[last-1])
                
            res.append("".join(temp))
            index = last
        return res
                
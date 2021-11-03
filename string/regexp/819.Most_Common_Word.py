import re
from collections import defaultdict
def mostCommonWord(paragraph,banned):
        '''
        if word !in banned, hash store{word, freq}
        max_count get most freq
        use regular expression import re, re.sub(pattern, replace, resultModify) filter " ", ?.,'
        '''
        if paragraph == None or len(paragraph) == 0: return ""
        
        paragraph_list = re.sub("[!?',;.]", ' ', paragraph.lower()).split()
        dic = defaultdict(int)

        for word in paragraph_list:
            if word not in banned:
                dic[word] += 1

        print(dic)
        max_count = 0
        res = ""

        for [k,v] in dic.items():
            if v >= max_count:
                res = k
                max_count = v
                
        return res
                    
# print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))
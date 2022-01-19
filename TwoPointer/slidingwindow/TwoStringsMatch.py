'''
438.Find All Anagrams in a String
    TOPIC: Two string, matching substring, window is fixed, USE SLIDING WINDOW
    STEP: template
    1.create hash/array store p's char:freq
    2.create variable, left,count
    3.in cur string loop, update dic, see if need move left, check valid
'''
    
def findAnagrams(self, s: str, p: str) -> List[int]:
        a = ord('a')
        if len(p) > len(s): return []
        # create hash store p{ch:frq}
        dic = [0] * 26 #only lowercase
        for c in p:
            dic[ord(c) - a] += 1
        
        res = []
        count = 0 #if find p
        left = 0
        for i in range(len(s)):
            #update dic
            dic[ord(s[i]) - a] -= 1
            if dic[ord(s[i]) - a] >= 0: #ch in p
                count += 1
            
            #see if need move left IF or WHILE? each time move once,so IF
            # > mean "cbae" e(3)+1=4 > p(3)
            if i - left + 1 > len(p): 
                dic[ord(s[left]) - a] += 1 #reset back
                if dic[ord(s[left]) - a] > 0: #valid
                    count -= 1
                left += 1
                    
            #check valid
            if count == len(p): #find one p
                res.append(left)
        
        return res
'''
    TOPIC: match pattern 2 hashmap {ch:lastIndex} pattern, keep update lastIndex
    STEP:ATT!"aaaa"=>"aa aa aa aa" TRUE, so cannot {ch:word}
'''
from collections import defaultdict
def wordPattern(pattern, s):
        if len(pattern) != len(s.split(" ")): return False
        arr = s.split(" ")
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for i in range(len(pattern)):
            if d1[pattern[i]] != d2[arr[i]]: return False
            else:
                d1[pattern[i]] = i+1
                d2[arr[i]] = i+ 1
        return True

print(wordPattern("aaa","aa aa aa aa")) #false
'''
    TOPIC:string pattern match use hashmap bi-direction since pattern match s, s also match pattern
    STEP1:two hashmaps. {ch:ch2} TWO PASSES (SLOW)
    STEP2:two hashmaps. {ch:lastestIndex} if both's v not the same, return False
    '''
    def wordPattern(self, pattern: str, s: str) -> bool:
        # corner case
        if len(pattern) != len(s.split(" ")): return False
        hash1 = collections.defaultdict(int)
        hash2 = collections.defaultdict(int)
        arr = s.split(" ")
        for i in range(len(pattern)):
            if hash1[pattern[i]] != hash2[arr[i]]:
                return False
            else:
                hash1[pattern[i]] = i + 1
                hash2[arr[i]] = i + 1
        return True
        
        
# 1WAY Two passes(SLOW)
#         # corner case
#         if len(pattern) != len(s.split(" ")): return False
#         hash1 = collections.defaultdict(int)
#         hash2 = collections.defaultdict(int)
#         arr = s.split(" ")
#         for i in range(len(pattern)):
#             if pattern[i] not in hash1:
#                 hash1[pattern[i]] = arr[i]
#             else:
#                 if hash1[pattern[i]] != arr[i]:
#                     return False
#                 else:
#                     continue
        
#         for i in range(len(arr)):
#             if arr[i] not in hash2:
#                 hash2[arr[i]] = pattern[i]
#             else:
#                 if hash2[arr[i]] != pattern[i]:
#                     return False
#                 else:
#                     continue
        
#         return True
                 
        
        

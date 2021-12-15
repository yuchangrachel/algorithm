def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        LOGIC:
        target first word as flag, let next one compare to flag, update flag which only have common prefix
        brute force:O(len(strs) * len(one word))
        '''
        if not strs or len(strs) == 0: return ""
        
        flag = strs[0]
        for k in range(1, len(strs)):
            word = strs[k]
            i = j = 0 # i tracking flag, j tracking word
            # find flag word who is shorter
            length = min(len(flag), len(word))
            while i < length and j < length:
                if flag[i] != word[j]:
                    break
                else:
                    i+=1
                    j+=1
            flag = flag[:i]
        return flag
# 28. Implement strStr()
def strStr(self, haystack: str, needle: str) -> int:
        if (not haystack and not needle) or (len(haystack) == 0 and len(needle) == 0): return 0
        if len(haystack) < len(needle): return -1
        if len(needle) == 0: return 0
        
        for i in range(len(haystack)-len(needle) + 1):
            # find first character
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle: return i
                else: continue
            else:
                continue
        return -1
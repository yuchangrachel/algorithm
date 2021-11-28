#455. Assign Cookies
def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # TOPIC: s can random to send to children, s[any j] >= g[any i] as much as possible
        # HOW: sort children in decrease order and s cookies as well. since most content should match with most cookies
        
        if not g or not s or len(g) == 0 or len(s) == 0: return 0
    
        res = 0
        
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] < g[i]:
                # cannot meet content, cur child need higher content, so find next less content
                i+=1
            else:
                res += 1
                i+=1
                j+=1
                
        return res
        
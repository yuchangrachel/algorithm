#997. Find the Town Judge
'''
    TOPIC:Direct graph, Think two directions trust and betrust
    STEP:
    1WAY:use Set store people who trust others, Map store betrusted: trusting people
    If n is not in set and n as key, its value size is N-1
'''
def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = set()
        betrusted = collections.defaultdict(list)
        for t in trust:
            trusting.add(t[0])
            betrusted[t[1]].append(t[0])
        for i in range(1, n+1):
            if i in trusting: continue
            if len(betrusted[i]) == n-1: return i
        return -1
    
#Lintcode 645 · Find the Celebrity https://www.lintcode.com/problem/645
def findCelebrity(self, n):
        know = set()
        beKnown = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i ==j:
                    continue
                else:
                    if Celebrity.knows(i, j):
                        know.add(i)
                        beKnown[j].append(i)
        
        for i in range(n):
            if i in know:continue
            if len(beKnown[i]) == n-1:
                return i
        return -1
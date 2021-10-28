from collections import deque
from collections import defaultdict

def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        '''
        Based on ui to vi, build neighbor list
        if one of path is used, cannot use again
        use queue,store[start, mid] path, [mid, mid1] ....[midn , end] 
        '''
        # build graph(build neighbor list)[[start, mid]]
        if start == end: # in original point
            return True
    
        # build bi-directional graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v) #dic{u:[v1, v2]}
            graph[v].append(u) #dic{v:[u1, u2]}

        q = deque()
        q.append(start)
        seen = [False] * n
        while len(q) > 0:
            node = q.popleft()      
        
            for nei in graph[node]: 
                if nei == end: return True
                else:
                    if seen[nei] == False:
                        q.append(nei)
            seen[node] = True
        return False      

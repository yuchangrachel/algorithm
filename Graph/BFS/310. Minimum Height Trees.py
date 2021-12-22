#310. Minimum Height Trees
'''
    TOPIC:return list of Minimum height tree's root labels(TREE:undirected connected graph)
    STEP:
    1.create hashmap store{vetex: list of another vetexs share same edges}
    2.create indegree array which count many edges link to this vetex
    3.create q(BSF) store degree = 1, each time pop(find map list cut edge degree--), and add degree == 1, in the end, last to the end it is roos meet MHT
    refer:https://www.youtube.com/watch?v=pUtxTz134qM
'''
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges or len(edges) == 0: return [0]
        res = []
        degree = [0] * n
        hashmap = collections.defaultdict(list)
        for edge in edges:
            if edge[0] not in hashmap:
                hashmap[edge[0]] = []
            hashmap[edge[0]].append(edge[1])
            if edge[1] not in hashmap:
                hashmap[edge[1]] = []
            hashmap[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            
        q = deque()
        for i, count in enumerate(degree):
            if count == 1:
                q.append(i) #store label
        
        while len(q) > 0:
            layerList = []
            size = len(q)
            index = 0
            while index < size:
                top = q.popleft()
                layerList.append(top)
                for otherConnected in hashmap[top]:
                    degree[otherConnected] -= 1
                    if degree[otherConnected] == 1: #now down to 1, add into q, for next layer
                        q.append(otherConnected)      
                index += 1
            #after one layer, store list into res temporarily
            res = layerList

        return res
            
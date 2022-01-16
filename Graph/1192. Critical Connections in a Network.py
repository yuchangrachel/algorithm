'''
    TOPIC:Tarjan/bridge algorithm
    '''
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res = []
        mapping = collections.defaultdict(list)
        time = [0] * 1 #as global varable
        
        # 0STEP:create graph
        for connection in connections:
            if connection[0] not in mapping:
                mapping[connection[0]] = []
            mapping[connection[0]].append(connection[1])
            
            if connection[1] not in mapping:
                mapping[connection[1]] = []
            mapping[connection[1]].append(connection[0])
            
        # 1STEP:dfs when iterate the nodes
        # create variable
        meet = [-1] * n #first time to visit this node
        parent = [-1] * n #check current u as his neighbor children v. dfs tree has parent, each node can as root of subtree, avoid visit again
        low = [-1] * n #lowIndexInSubtree visit this node use earliest time, if low[v]>meet[u]:[u,v] is bridge (will update)
        
        for i in range(n):
            if meet[i] == -1: #non visited 
                self.dfs(i, parent, low, meet, res, time, mapping)
        
        return res
    
    def dfs(self, u, parent, low, meet, res, time, mapping):
        if meet[u] != -1: #already visited
            return
        
        #u is first time meet,update low = meet
        meet[u] = time[0]
        low[u] = meet[u]
        time[0]+= 1
        
        #find u's neighbors
        for v in mapping[u]:
            if meet[v] == -1: #v is first time meet
                parent[v] = u #set v's parent is u
                self.dfs(v, parent, low, meet, res, time, mapping)
                
                #after dfs get if bridge
                if low[v] > meet[u]:
                    res.append([u,v])
                
                low[u] = min(low[u], low[v]) # update earlier time after dfs, if belong to same subtree, find min as low
            elif parent[u] != v: #go there v is visited but not parent of u, it is another's parent
                low[u] = min(low[u], meet[v])
                
                
print(criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
#133. Clone Graph
def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        this is connected undirected graph, so mean not spread single nodes everywhere
        clone think dic:{old:new}
        traverse and build graph, think bfs,bfs,
        find neighbor or shortest distance from one node use bfs
        '''
        if not node: return None
        
        newNode = Node(node.val, [])
        dic = {node: newNode} 
        q = collections.deque([node]) # q store old graph
        
        while len(q) > 0:
            top = q.popleft()
            
            for neighbor in top.neighbors:
                if neighbor not in dic: # if already existed, cannot build new node again
                    dic[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                dic[top].neighbors.append(dic[neighbor])
        
        return newNode
        
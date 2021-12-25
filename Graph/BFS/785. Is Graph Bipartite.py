'''
    TOPIC:Bipartite use Color. see neighbor will think BFS. This is undirected, some connected graph.
    STEP:how to divide two set, use same edges(neighbor) must be in different.
    1.ATT! in loop, to handle color array and queue(because some nodes not connected, nodes in graph already)
    2.create color array see if colored:default:0, red:1, blue:2
'''
from collections import deque
def isBipartite(graph):
        #use hashmap{vertex: list of neighbor}
        nodes = len(graph)
        color = [0] * nodes
        
        for i in range(len(graph)):
            if color[i] != 0: continue
            else:
                q = deque()
                color[i] = 1
                q.append(i)
                
                while len(q) > 0:
                   
                    cur = q.popleft()
                    
                    curColor = color[cur]
                    neighborColor = 2 if curColor == 1 else 1
                    print("q ", cur, color[cur], " ", neighborColor)

                    for v in graph[cur]:
                        if color[v] == 0:                           
                            color[v] = neighborColor
                            q.append(v)
                        elif color[v] != neighborColor:
                            return False
        return True
    
print(isBipartite(
[[1,3],[0,2],[1,3],[0,2]]))
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # connected undirect graph, no weight, only find each node's neighbors(BFS)
    # how to do deep copy, how to from old to new: hashtable{old:new}
    def cloneGraph(self, node: 'Node') -> 'Node':
        # corner case
        if not node: return node
        
        # create hash
        newNode = Node(node.val, []) #intial neighbor list is empty, need explore when doing bfs
        dic = {node: newNode}
        q = collections.deque()
        q.append(node)
        while len(q) > 0:
            cur = q.popleft() # not in while loop,only one node, each time queue only add one node, and spread out by neighbor props
            for neighbor in cur.neighbors:
                if neighbor not in dic.keys():
                    dic[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                dic[cur].neighbors.append(dic[neighbor])
        return newNode
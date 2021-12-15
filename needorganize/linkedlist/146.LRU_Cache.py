class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    # LOGIC: hashmap+double linkedlist
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} # store {key: Node(k,v)}
        self.head = Node(0, 0) # every add/update ele, it is after head
        self.tail = Node(-1, -1) # nothing real val on tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeNodeFromList(node)
            self.addAfterHead(node)
            return node.value
        else: return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # update
            node = self.dic[key]
            self.removeNodeFromList(node)
            self.addAfterHead(node)
            node.value = value
        else:
            #new 
            if len(self.dic) >= self.capacity:
                self.removeTail()
            newNode = Node(key, value)
            self.dic[key] = newNode
            self.addAfterHead(newNode)
    
    def removeNodeFromList(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
               
    def addAfterHead(self, node):
        headNext = self.head.next # store previous head
        self.head.next = node # now after head is newNode
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    
    def removeTail(self):
        if len(self.dic) == 0: return
        tailValidNode = self.tail.prev
        del self.dic[tailValidNode.key]
        self.removeNodeFromList(tailValidNode) 
        
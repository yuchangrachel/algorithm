class MyHashMap:
    #2WAY optimize space
    #create 1000 size for map first, find hash key, create another 1001 size for that hashkey, total size is 1000*1000,but second 1000 may or may not create
    def __init__(self):
        self.hashmap = [[] for _ in range(1001)]
        
    def put(self, key: int, value: int) -> None:
        hashkey = key % 1000
        if len(self.hashmap[hashkey]) == 0:
            self.hashmap[hashkey] = [-1] * 1001
        
        self.hashmap[hashkey][key//1000] = value
                  

    def get(self, key: int) -> int:
        hashkey = key % 1000
        if len(self.hashmap[hashkey]) > 0:
            return self.hashmap[hashkey][key // 1000]
        return -1

    def remove(self, key: int) -> None:
        hashkey = key % 1000
        if len(self.hashmap[hashkey]) > 0:
            self.hashmap[hashkey][key//1000] = -1

#     #1WAY 
#     def __init__(self):
#         # key, value maximum is 10^6
#         self.hashmap = [-1] * 10000001
        
#     def put(self, key: int, value: int) -> None:
#         self.hashmap[key] = value

#     def get(self, key: int) -> int:
#         return self.hashmap[key]

#     def remove(self, key: int) -> None:
#         self.hashmap[key] = -1
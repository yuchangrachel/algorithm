#706. Design HashMap
'''
    TOPIC:Hashmap 
    STEP:
    1.create 1000size for hashmap's key(10^6 size ok, but not efficient space)
    2.if one key occur, create another 1000 size for store this key's value list. if all key(1000) occur, use 1000*1000memory space
'''
    def __init__(self):
        self.hash = [[] for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        hashkey = key % 1000
        if len(self.hash[hashkey]) == 0:
            self.hash[hashkey] = [-1] * 1001
        self.hash[hashkey][key//1000] = value

    def get(self, key: int) -> int:
        hashkey = key % 1000
        if len(self.hash[hashkey]) == 0: 
            return -1
        else:
            return self.hash[hashkey][key//1000]

    def remove(self, key: int) -> None:
        #when remove, let value=-1, so get it then return -1
        hashkey = key % 1000
        if len(self.hash[hashkey]) > 0: #otherwise nothing to remove
            self.hash[hashkey][key//1000] = -1

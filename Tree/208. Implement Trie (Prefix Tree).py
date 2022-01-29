'''
TOPIC:dictionary tree, use For search word if exist
STEP:
1.create TrieNode include isEnd, children 26List of nodes, charvar
2.search/insert
'''
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.isEnd = False
        self.children = [None] * 26 #each node has 26 children node. default is None
    
class Trie:
    def __init__(self):
        #start from empty root
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        #each time insert or search, start from root
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] is None: #dictionary here only have lowercase
                #not exist yet, need create new trinode
                cur.children[ord(c) - ord('a')] = TrieNode(c)
            cur = cur.children[ord(c) - ord('a')]
        cur.isEnd = True
                  

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] is None:
                return False
            else:
                cur = cur.children[ord(c) - ord('a')]
        return cur.isEnd == True
        

    def startsWith(self, prefix: str) -> bool: # have apple, now word is app -> true
        cur = self.root
        for c in prefix:
            if cur.children[ord(c) - ord('a')] is None:
                return False
            else:
                cur = cur.children[ord(c) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
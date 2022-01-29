'''
TOPIC:trie tree for searching word
STEP:"." can mean any letter, so do DFS check if match this pattern, SO not backtracking (show all combination or permutation)
1.dfs: helper(word, index)
'''
class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.isEnd = False
        self.children = [None] * 26
        
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
        return self.dfs(word, cur, 0)
    
    def dfs(self, word, cur, index):
        # corner case /terminate
        if index == len(word):
            #search to last char of word, so see if isEnd
            return cur.isEnd
        #recursion
        if word[index] == ".": #mean can go to all of its children to search possibility
            for node in cur.children:
                if node and self.dfs(word, node, index+1):
                    return True
            #after dfs
            return False
        else:
            return cur.children[ord(word[index]) - ord("a")] and self.dfs(word, cur.children[ord(word[index]) - ord("a")], index+ 1)
        
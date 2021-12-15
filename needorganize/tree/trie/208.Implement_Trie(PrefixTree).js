/*
208.
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
*/
class TrieNode {
  constructor(val = null) {
    this.val = val;
    this.children = []; //store nodes
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    //create empty new root first
    this.root = new TrieNode(-1);
  }

  insert(word) {
    let node = this.root;
    for (let c of word) {
      if (node.children[c] == null) node.children[c] = new TrieNode(c);
      node = node.children[c];
    }
    node.isEnd = true;
  }

  search(word) {
    let node = this.root;
    for (let c of word) {
      if (node.children[c] == null) return false;
      node = node.children[c];
    }
    return node.isEnd;
  }

  startsWith(prefix) {
    let node = this.root;
    for (let c of prefix) {
      if (node.children[c] == null) return false;
      node = node.children[c];
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

1032. Stream of Characters
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = [None] * 26
        self.isEnd = False
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.history = []
        for word in words:
            #store word from last char
            cur = self.root
            for i in range(len(word)-1, -1, -1):
                if not cur.children[ord(word[i]) - ord("a")]:
                    cur.children[ord(word[i]) - ord("a")] = TrieNode(word[i])
                cur = cur.children[ord(word[i]) - ord("a")] 
            cur.isEnd = True
        
    def query(self, letter: str) -> bool:
        self.history.append(letter)
        cur = self.root
        #each time query one time
        #start from newest to oldest see if can find whole word in words
        index = len(self.history) - 1
        while index >= 0 and cur.children[ord(self.history[index]) - ord("a")]:
            cur = cur.children[ord(self.history[index]) - ord("a")] 
            if cur and cur.isEnd: return True
            index -= 1
        return False
            



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
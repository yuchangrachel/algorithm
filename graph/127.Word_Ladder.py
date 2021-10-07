'''
refer: https://www.youtube.com/watch?v=ZVJ3asMoZ18
LOGIC:
Find minimum jump from source to destination
USE BFS OR DFS?
In graph, use BFS find shortest distance since paths are not unique, polynomial time; If use DFS use exponential time
In tree: use DFS find minimum path since paths are unique.

COMPLEXITY:
T:O(26*W*N1*N2) W:eachword len N1:wordlist N2:word comparisons

KNOWLEDGE:
python set: set(list), set.add(v), set.remove(v), len(set)
python queue: collections.deque(), q.append(v), q.popleft(), len(q)
python string/array: str-> arr: a=list(s), not split(""), chr(num), ord(char), 'a'=97, 'z'=122
'''

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or len(wordList) == 0: return 0
        
        # create set for wordlist, avoid use duplicate
        canVisit = set(wordList)
        
        # corner case check if endword in set 
        if endWord not in canVisit:
            return 0
        
        # create queue doing BFS find shortest distance 
        q = collections.deque()
        q.append(beginWord)
        res = 0 # or step
        
        while len(q) > 0:
            size = len(q)
            index = 0
            while index < size:
                cur = q.popleft()
                
                # if find destionation return
                if cur == endWord:
                    return res +1
                
                # transform only one char
                for i in range(len(cur)): #h i t
                    # string-> array to modify string
                    curArr = list(cur)
                    for j in range(97, 123): #a-z ord(97)="a" ord(122)="z"                        
                        curArr[i] = chr(j)
                        newStr = "".join(curArr) # array-> string
                        if newStr in canVisit and cur != newStr:
                            q.append(newStr)
                            canVisit.remove(newStr)
                index+=1
                
            res+=1 # next layer
        
        return 0
                            
                
            